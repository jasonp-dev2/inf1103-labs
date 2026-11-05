"""
PhysicalProduct class
    -Subclass of Product 'parent' class
    -Stores additional 'weight' attribute
"""
from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, Id, name, price, stock, weight):
        super().__init__(Id, name, price, stock)
        self.__weight = weight

    def display_information(self): #return product info as dict
        product_info = super().display_information() #receive parent product info, which is a dict
        product_info["Weight"] = self.__weight #adds weight detail to dict
        return product_info

    def get_fulfilment_info():
        return "This product requires physical shipping."

    def calculate_shipping_cost(weight):
        return super().calculate_shipping_cost()


"""""
#Testing
PP1 = PhysicalProduct("PD002", "Anvil", 150.50, 30, 500)

print(PP1.display_information())
"""