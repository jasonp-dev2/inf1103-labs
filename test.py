import inspect
from typing import get_type_hints
from unittest.mock import patch

from CanBeShipped import CanBeShipped
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from OrderLine import OrderLine
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


def show_product_details(product: Product) -> None:
    print(product.display_information())
    print(product.get_fulfilment_info())
    print("-" * 40)


def test_supplier_product_association() -> None:
    # 1. Supplier and Product exist independently (Association)
    supplier = Supplier("S001", "TechCorp", "contact@techcorp.com")
    laptop = PhysicalProduct("P001", "Laptop", 500.0, 25, 5.0, supplier)

    # Product stores reference to Supplier
    assert laptop.supplier is supplier
    assert laptop.supplier.display_information()["Name"] == "TechCorp"

    # Deleting standalone reference to Supplier leaves Product's reference intact
    del supplier
    assert laptop.supplier is not None
    assert laptop.supplier.display_information()["ID"] == "S001"

    # Deleting Product leaves another standalone Supplier intact
    supplier_2 = Supplier("S002", "SoftWorks", "info@softworks.com")
    antivirus = DigitalProduct("D001", "Anti-hack", 50.0, 10, 50.0, supplier_2)
    del antivirus
    assert supplier_2.display_information()["Name"] == "SoftWorks"
    print("[PASS] 1. Supplier & Product association and independent lifecycles.")


def test_inventory_aggregation() -> None:
    # 2. Inventory aggregates Product objects; removing does not destroy them
    supplier = Supplier("S001", "TechCorp", "contact@techcorp.com")
    laptop = PhysicalProduct("P001", "Laptop", 500.0, 25, 5.0, supplier)

    inv_a = Inventory()
    inv_b = Inventory()

    assert inv_a.add_product(laptop) is True
    assert inv_a.add_product(laptop) is False  # Duplicate ID prevented
    assert inv_a.find_product("P001") is laptop

    # Remove from Inventory A and verify Product still works
    assert inv_a.remove_product("P001") is True
    assert inv_a.find_product("P001") is None
    laptop.update_stock(20)
    assert laptop.display_information()["Stock"] == 20

    # Add same Product instance to Inventory B
    assert inv_b.add_product(laptop) is True
    assert inv_b.find_product("P001") is laptop

    # Remove from Inventory B; Product remains intact
    assert inv_b.remove_product("P001") is True
    assert laptop.display_information()["Name"] == "Laptop"
    print("[PASS] 2. Inventory aggregation and independent Product lifecycle.")


def test_order_composition_and_totals() -> None:
    # 3. Order creates/manages OrderLines (Composition); OrderLine refers to Product
    supplier = Supplier("S001", "TechCorp", "contact@techcorp.com")
    laptop = PhysicalProduct("P001", "Laptop", 500.0, 25, 5.0, supplier)
    antivirus = DigitalProduct("D001", "Anti-hack", 50.0, 10, 50.0, supplier)

    order_1 = Order("ORD-001")
    order_1.add_order_line(laptop, 2)     # 500.0 * 2 = 1000.0
    order_1.add_order_line(antivirus, 3)  # 50.0 * 3 = 150.0

    assert len(order_1.order_lines) == 2
    assert isinstance(order_1.order_lines[0], OrderLine)
    assert order_1.calculate_total() == 1150.0

    # Add same Product to a second Order -> creates a separate OrderLine
    order_2 = Order("ORD-002")
    order_2.add_order_line(laptop, 1)

    line_1 = order_1.order_lines[0]
    line_2 = order_2.order_lines[0]
    assert line_1 is not line_2
    assert line_1.product is line_2.product is laptop

    # Removing an OrderLine or deleting an Order does not destroy Product
    assert order_1.remove_order_line("D001") is True
    assert order_1.calculate_total() == 1000.0
    del order_2
    assert laptop.display_information()["ID"] == "P001"
    print("[PASS] 3. Order composition, OrderLine association, and total calculation.")


def test_polymorphism_and_substitutability() -> None:
    # 4. Inventory handles PhysicalProduct & DigitalProduct via Product abstraction
    supplier = Supplier("S001", "TechCorp", "contact@techcorp.com")
    laptop: Product = PhysicalProduct("P001", "Laptop", 500.0, 25, 5.0, supplier)
    antivirus: Product = DigitalProduct("D001", "Anti-hack", 50.0, 10, 50.0, supplier)

    # Test Liskov Substitutability via helper accepting Product
    show_product_details(laptop)
    show_product_details(antivirus)

    assert isinstance(laptop, Product) and isinstance(laptop, CanBeShipped)
    assert isinstance(antivirus, Product) and not isinstance(antivirus, CanBeShipped)

    inventory = Inventory()
    assert inventory.add_product(laptop) is True
    assert inventory.add_product(antivirus) is True

    with (
        patch.object(laptop, "display_information", wraps=laptop.display_information) as p_info,
        patch.object(laptop, "get_fulfilment_info", wraps=laptop.get_fulfilment_info) as p_fulfil,
        patch.object(antivirus, "display_information", wraps=antivirus.display_information) as d_info,
        patch.object(antivirus, "get_fulfilment_info", wraps=antivirus.get_fulfilment_info) as d_fulfil,
    ):
        inventory.display_all_products()
        p_info.assert_called_once()
        p_fulfil.assert_called_once()
        d_info.assert_called_once()
        d_fulfil.assert_called_once()

    assert laptop.display_information()["Weight"] == 5.0
    assert laptop.get_fulfilment_info() == "This product requires physical shipping."
    assert antivirus.display_information()["Download_Size"] == 50.0
    assert antivirus.get_fulfilment_info() == "This product is delivered digitally."
    print("[PASS] 4. Polymorphism & Liskov substitutability through Product.")


def test_type_hints_present() -> None:
    # 5. Verify type hints exist on key methods and abstract contracts
    assert get_type_hints(Inventory.add_product) == {"product": Product, "return": bool}
    assert get_type_hints(Inventory.remove_product) == {"product_id": str, "return": bool}
    assert get_type_hints(Inventory.find_product) == {"product_id": str, "return": Product | None}
    assert get_type_hints(Inventory.display_all_products) == {"return": type(None)}
    assert get_type_hints(Order.add_order_line) == {"product": Product, "quantity": int, "return": type(None)}
    assert get_type_hints(Order.remove_order_line) == {"product_id": str, "return": bool}
    assert get_type_hints(Order.calculate_total) == {"return": float}
    assert get_type_hints(OrderLine.calculate_subtotal) == {"return": float}
    assert not inspect.isabstract(PhysicalProduct)
    assert not inspect.isabstract(DigitalProduct)
    assert inspect.isabstract(Product)
    assert inspect.isabstract(CanBeShipped)
    print("[PASS] 5. Type hints and abstract class contracts verified.")


if __name__ == "__main__":
    test_supplier_product_association()
    test_inventory_aggregation()
    test_order_composition_and_totals()
    test_polymorphism_and_substitutability()
    test_type_hints_present()
    print("\nAll verification checks passed!")
    
