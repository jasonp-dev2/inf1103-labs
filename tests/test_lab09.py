import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from DigitalProduct import DigitalProduct
from DiscountStrategy import BulkDiscount, PercentageDiscount, StudentDiscount
from Inventory import Inventory
from Order import Order
from OrderLine import OrderLine
from PhysicalProduct import PhysicalProduct
from ProductFactory import ProductFactory
from Supplier import Supplier
from main import get_positive_float, load_products


SAMPLE_CSV = Path(__file__).resolve().parents[1] / "products.csv"


class DiscountTests(unittest.TestCase):
    def setUp(self):
        product = ProductFactory.create("physical", "P100", "Keyboard", 125, 10, 1)
        self.order = Order("O001")
        self.order.add_order_line(product, 2)

    def test_default_discount(self):
        self.assertEqual(self.order.calculate_total(), 250)

    def test_switch_discounts(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230)
        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.calculate_total(), 225)

    def test_bulk_threshold(self):
        strategy = BulkDiscount(200, 20)
        self.assertEqual(strategy.apply(199), 199)
        self.assertEqual(strategy.apply(200), 180)

    def test_student_discount(self):
        self.order.set_discount(StudentDiscount())
        self.assertEqual(self.order.calculate_total(), 237.50)

    def test_orders_can_share_a_strategy(self):
        strategy = PercentageDiscount(10)
        self.order.set_discount(strategy)
        other_order = Order("O002", strategy)
        self.assertIs(self.order.discount, other_order.discount)


class ProductTests(unittest.TestCase):
    def test_factory_creates_each_type_with_extra_value_and_supplier(self):
        supplier = Supplier("S001", "Example", "supplier@example.com")
        for kind, expected_type, field in (
            ("physical", PhysicalProduct, "Weight"),
            ("digital", DigitalProduct, "Download_Size"),
        ):
            with self.subTest(kind=kind):
                product = ProductFactory.create(kind, "P100", "Item", 30, 10, 2, supplier)
                self.assertIsInstance(product, expected_type)
                self.assertEqual(product.display_information()[field], 2)
                self.assertIs(product.supplier, supplier)

    def test_unknown_factory_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S100", "Setup", 30, 5, 0)

    def test_nonpositive_and_nonfinite_product_prices(self):
        for price in (0, -1, float("nan"), float("inf")):
            with self.subTest(price=price):
                with self.assertRaisesRegex(ValueError, "greater than zero"):
                    ProductFactory.create("physical", "P100", "Item", price, 0, 1)

    def test_negative_stock_is_rejected_by_digital_products(self):
        with self.assertRaisesRegex(ValueError, "stock quantity cannot be negative"):
            ProductFactory.create("digital", "D100", "App", 30, -1, 1)
        product = ProductFactory.create("digital", "D100", "App", 30, 0, 1)
        with self.assertRaisesRegex(ValueError, "stock quantity cannot be negative"):
            product.update_stock(-1)
        self.assertEqual(product.display_information()["Stock"], 0)

    def test_order_line_rejects_nonpositive_quantity(self):
        product = ProductFactory.create("physical", "P100", "Item", 30, 10, 1)
        for quantity in (0, -1):
            with self.subTest(quantity=quantity):
                with self.assertRaisesRegex(ValueError, "Quantity must be greater than zero"):
                    OrderLine(product, quantity)


class InputAndCSVTests(unittest.TestCase):
    def test_price_retries_until_valid(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]) as prompt:
            with redirect_stdout(output):
                self.assertEqual(get_positive_float("Price: "), 12.50)
        self.assertEqual(prompt.call_count, 3)
        self.assertEqual(output.getvalue().splitlines(), [
            "Please enter a valid number, e.g. 12.50",
            "Please enter a number greater than zero.",
        ])

    def test_csv_skips_invalid_rows_and_continues(self):
        inventory = Inventory()
        output = io.StringIO()
        with redirect_stdout(output):
            loaded = load_products(str(SAMPLE_CSV), inventory)
        self.assertEqual(list(loaded), ["P001", "D001", "P003"])
        for product_id, product in loaded.items():
            self.assertIs(inventory.find_product(product_id), product)
        messages = output.getvalue().splitlines()
        self.assertEqual(messages[0], "Row 4 skipped: Unknown product type: service")
        self.assertIn("abc", messages[1])
        self.assertEqual(messages[2:], ["3 products loaded.", "Load attempt finished."])

    def test_missing_csv(self):
        inventory = Inventory()
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(output):
            missing = str(Path(directory) / "products.csv")
            self.assertEqual(load_products(missing, inventory), {})
        self.assertEqual(output.getvalue().splitlines(), [
            f"Products file not found: {missing}",
            "Load attempt finished.",
        ])


if __name__ == "__main__":
    unittest.main()
