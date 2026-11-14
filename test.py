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
from DiscountStrategy import NoDiscount, PercentageDiscount, BulkDiscount


product = PhysicalProduct(
    product_id="P001",
    name="Keyboard",
    price=125.0,
    stock=10,
    weight=1.0,
)

order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(product, 2)

print(order.calculate_total())  # 230.0

order.set_discount(PercentageDiscount(10))

print(order.calculate_total())  # 225.0