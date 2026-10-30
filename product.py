"""
Product class
    -Stores product information
    -Manages its own state
"""

class Product:
    def __init__(self, product):
        self.__product_Id = product["ID"]
        self.__name = product["Name"]
        self.__price = product["Price"]
        self.__stock = product["Stock"]
       
    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        return {
            "ID": self.__product_Id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }



