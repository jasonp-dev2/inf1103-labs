"""
Inventory class
    -Stores products
    -Adds products
    -Searches products
    -Displays products
"""
import Product as pdt

class Inventory:
    def __init__(self): #inventory is a nested dictionary loaded from inventory.json
        self.__products = {}

    def add_product(self):
        product_Id = input("Product ID: ")
        product_name = input("Product Name: ")
        product_price = float(input("Price: "))
        formatted_price = f"{product_price:.2f}"
        product_stock = int(input("Stock Quantity: "))
    
        if product_stock>500:
            print("Stock limit exceeded. Cannot add product with stock greater than 500.")
            return None

        product_entry = {
            "ID": product_Id, #e.g PD001
            "Name": product_name,
            "Price": formatted_price,
            "Stock": product_stock
        }

        #product_Id = pdt.Product(product_entry) #PD001 = object
        self.__products[product_Id] = pdt.Product(product_entry)
        print("\n" + "Product added successfully!" + "\n")  


    def search_product(self):
        print("\n" + "Search Product" + "\n")
        product_id = input("Enter Product ID: ")

        if product_id in self.__products:
            product = self.__products[product_id]
            print(
                " Product Found: " + "\n",
                "-----------------------------------" + "\n"
                f"{product.display_information()}",
                "-----------------------------------" + "\n"
            )
        else:
            return False
 
    def display_all(self):
        print("\n" + "Current Inventory: " + "\n")
        print("-----------------------------------" + "\n")
        for product_info in self.__products:
            product = self.__products[product_info]
            product.display_information()
        print("\n" + "-----------------------------------" + "\n")




inventory = Inventory()

return_value = inventory.add_product()
if return_value is None:
    pass
else:
    print("\n" + "Product added successfully!" + "\n")  

inventory.display_all()

