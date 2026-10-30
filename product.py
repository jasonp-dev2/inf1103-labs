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
        print(
            f" ID: {self.__product_Id} \n", 
            f"Name: {self.__name} \n", 
            f"Price: ${self.__price} \n", 
            f"Stock: {self.__stock} \n",
        )

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
