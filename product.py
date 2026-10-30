"""
Product class
    -Stores product information
    -Manages its own state
"""

class Product:
    def __init__(self, Id, name, price, stock):
        self.__Id = Id
        self.__name = name
        self.__price = price
        self.__stock = stock
       
    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self): #return product info as dict
        return {
            "ID": self.__Id, 
            "Name": self.__name, 
            "Price": self.__price, 
            "Stock": self.__stock,
        }

"""
Testing

product_info = {
    "ID": "PD004",
    "Name": "Laptop",
    "Price": 500, 
    "Stock": 10
}
product = Product(product_info)

product.display_information()
"""
