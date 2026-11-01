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

    def search_product(self, product_Id):
        try:
            product = self.__products[product_Id]
            return product
        except:
            return False
        
    def display_all(self):
        print("\n" + "Current Inventory: " + "\n")
        print("-----------------------------------" + "\n")
        for product in self.__products.values():
            product_info = product.display_information()
            try:
                print(
                    f" ID: {product_info['ID']} \n", 
                    f"Name: {product_info['Name']} \n", 
                    f"Price: ${product_info['Price']} \n", 
                    f"Stock: {product_info['Stock']} \n",
                )
            except:
                print("Error retrieving inventory")
                pass
        print("\n" + "-----------------------------------" + "\n")

    def get_Inventory(self):
        export_Inventory = {}
        for product_id, product in self.__products.items():
            export_Inventory[product_id] = product.display_information()

        return export_Inventory

