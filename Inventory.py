"""
Inventory class
    -Stores products
    -Adds products
    -Searches products
    -Displays products
"""

from Product import Product


class Inventory:
    def __init__(self, products: dict[str, Product] | None = None) -> None:
        self.__products: dict[str, Product] = products.copy() if products else {}

    def add_product(self, product: Product) -> bool:
        product_id: str = str(product.display_information()["ID"])
        if product_id in self.__products:
            return False
        self.__products[product_id] = product
        return True

    def remove_product(self, product_id: str) -> bool:
        return self.__products.pop(product_id, None) is not None

    def find_product(self, product_id: str) -> Product | None:
        return self.__products.get(product_id)

    def display_all_products(self) -> None:    
        for product in self.__products.values():        
            product.display_information()
            product.get_fulfilment_info()