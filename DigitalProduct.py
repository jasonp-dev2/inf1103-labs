"""
DigitalProduct class
    -Subclass of Product 'parent' class
    -Stores additional 'download_size' attribute
"""

from Product import Product
from Supplier import Supplier


class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier | None = None,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self) -> dict[str, str | float | int]:
        product_info: dict[str, str | float | int] = super().display_information()
        product_info["Download_Size"] = self.__download_size
        return product_info

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."