"""
Order class
    -Stores order information
    -Manages its own state
"""

from Product import Product
from OrderLine import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line: OrderLine = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.order_lines:
            if line.product.display_information()["ID"] == product_id:
                self.order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)