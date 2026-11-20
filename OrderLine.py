"""
OrderLine class
    -Represents one product and quantity of selected product in an order
"""

from Product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        price: float = float(self.product.display_information()["Price"])
        return price * self.quantity