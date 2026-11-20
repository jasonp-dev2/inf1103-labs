"""
Product class
    -Stores product information
    -Manages its own state
"""

from abc import ABC, abstractmethod
from math import isfinite

from Supplier import Supplier

class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier | None = None,
    ) -> None:
        if not isfinite(price) or price <= 0:
            raise ValueError("Product price must be finite and greater than zero.")
        if stock < 0:
            raise ValueError("Product stock quantity cannot be negative.")

        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.supplier: Supplier | None = supplier

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Product stock quantity cannot be negative.")
        self.__stock = quantity

    def display_information(self) -> dict[str, str | float | int]:
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock,
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
