"""
PhysicalProduct class
    -Subclass of Product 'parent' class
    -Stores additional 'weight' attribute
"""

from Product import Product
from Supplier import Supplier
from CanBeShipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier | None = None,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> dict[str, str | float | int]:
        product_info: dict[str, str | float | int] = super().display_information()
        product_info["Weight"] = self.__weight
        return product_info

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_cost: float = self.__weight * 3.0  # $3 per kg to ship
        return shipping_cost