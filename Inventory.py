"""
Inventory class
    -Stores products
    -Adds products
    -Searches products
    -Displays products
"""

class Inventory:
    def __init__(self, data): #constructor using data loaded from inventory.json
        self.__products = data

    def add_product(self, product_Id, product):
        try:
            self.__products[product_Id] = product
            return True
        except:
            return "Error"

        """"
        product_Id = input("Product ID: ")
        product_name = input("Product Name: ")
        product_price = float(input("Price: "))
        formatted_price = f"{product_price:.2f}"
        product_stock = int(input("Stock Quantity: "))
    
        if product_stock>500:
            print("Stock limit exceeded. Cannot add product with stock greater than 500.")
            return False

        product_entry = {
            "ID": product_Id, #e.g PD001
            "Name": product_name,
            "Price": formatted_price,
            "Stock": product_stock
        }

        #product_Id = pdt.Product(product_entry) #PD001 = object
        self.__products[product_Id] = pdt.Product(product_entry)
        """

    def search_product(self, product_Id):
        try:
            product = self.__products[product_Id]
            return product
        except:
            return False
        
 
    def display_all(self):
        print("\n" + "Current Inventory: " + "\n")
        print("-----------------------------------" + "\n")
        for product_info in self.__products:
            product = self.__products[product_info]
            product.display_information()
        print("\n" + "-----------------------------------" + "\n")



"""
#Testing

import Product as pdt

data = {}
inventory = Inventory(data)

Id = "PD001"
Name = "lappy"
Price = 500.00
Stock = 10

product = pdt.Product(Id, Name, Price, Stock)

inventory.add_product(Id, product)

product_Id = "PD001"

inventory.search_product(product_Id)


#inventory.display_all()
"""