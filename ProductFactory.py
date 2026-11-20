"""Create physical and digital products in one place."""

from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        extra_value: float,
        supplier: Supplier | None = None,
    ) -> Product:
        if product_type == "physical":
            return PhysicalProduct(
                product_id, name, price, stock_quantity, weight=extra_value, supplier=supplier
            )
        if product_type == "digital":
            return DigitalProduct(
                product_id, name, price, stock_quantity, download_size=extra_value, supplier=supplier
            )
        raise ValueError(f"Unknown product type: {product_type}")
