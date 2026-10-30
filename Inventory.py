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
        self.__products = []

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
            "ID": product_Id,
            "Name": product_name,
            "Price": formatted_price,
            "Stock": product_stock
        }

        product_Id = pdt.Product(product_entry)
        self.__products.append(product_Id)
        print("\n" + "Product added successfully!" + "\n")  

        #self.__inventory[product_Id] = pdt.Product(product_entry)

    def search_product(self, product_Id):
        return {
            f"Product ID: {self.__product_Id}\n"
            f"Product Name: {self.__name}\n"
            f"Product Price: {self.__price}\n"
            f"Product Stock: {self.__stock}\n"
        }

    def display_all(self):
        pass

"""inventory = Inventory()

return_value = inventory.add_product()
if return_value is None:
    pass
else:
    print("\n" + "Product added successfully!" + "\n")  "
"""
