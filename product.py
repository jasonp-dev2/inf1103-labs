"""
Product class
    -Stores product information
    -Manages its own state
"""

class Product:
    def __init__(self, product_Id, name, price, stock):
        self.__product_Id = product_Id
        self.__name = name
        self.__price = price
        self.__stock = stock
       
    def update_stock(self, quantity):
        self.__stock = quantity
        print(f"Product Stock is now {self.__stock}")

    def display_information(self):
        return {
            f"Product ID: {self.__product_Id}\n"
            f"Product Name: {self.__name}\n"
            f"Product Price: {self.__price}\n"
            f"Product Stock: {self.__stock}\n"
        }

product = Product("P001", "laptop", 10.00, 50)

print(product.display_information())

product.update_stock(70)

print(product.display_information())

