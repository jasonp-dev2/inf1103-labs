"""
Order class
    -Stores order information
    -Manages its own state
"""

from Product import Product
from OrderLine import OrderLine
from DiscountStrategy import DiscountStrategy, NoDiscount, PercentageDiscount, BulkDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        if discount == None:
            self.discount = NoDiscount()
        else:
            self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line: OrderLine = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.order_lines:
            if line.product.display_information()["ID"] == product_id:
                self.order_lines.remove(line)
                return True
        return False

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

