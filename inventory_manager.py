#  Inventory Manager

import json
from Product import Product
from Inventory import Inventory

def get_valid_input():
    user_input = input("Enter option: ")

    if user_input == "1":
        return user_input
    elif user_input == "2":
        return user_input
    elif user_input == "3":
        return user_input
    elif user_input == "4":
        return user_input
    elif user_input == "5":
        return user_input
    elif user_input == "6":
        return False
    else:
        return None

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            print("inventory.json found.")
            inventory = json.load(file)
        for product_id, product in inventory.items():
            product_Object = Product(*product.values())
            inventory[product_id] = product_Object
        print("Inventory loaded successfully." + "\n")
        return inventory
    except FileNotFoundError:
        print("inventory.json not found. Creating a new inventory.json file.")
        initial_inventory = {}
        with open("inventory.json", "w") as file:
            json.dump(initial_inventory, file)
        return initial_inventory

def add_product(inventory):    
    product_Id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = round(float(input("Price: ")),2)
    product_stock = int(input("Stock Quantity: "))
    
    if product_stock>500:
        print("Stock limit exceeded. Cannot add product with stock greater than 500. Please try again")
        return False

    product = Product(product_Id, product_name, product_price, product_stock) #create product using product_Id as name
    result = inventory.add_product(product_Id, product)
    return result

def update_stock(inventory):
    print("\n" + "Update Stock")
    product_id = input("Enter Product ID: ")

    try: 
        found_product = inventory.search_product(product_id)
        product_info = found_product.display_information()
        print(
            "\n" + 
            f"Product Found: \n", 
            f"Name: {product_info['Name']} \n", 
            f"Current Stock: {product_info['Stock']} \n" 
        )
        new_stock = int(input("Enter new stock quantity: "))
        if new_stock > 500:
            print("Stock quantity can't be above 500. Please try again")
            return False
        found_product.update_stock(new_stock)
        return True
    except:
        return False

def search_product(inventory):
    print("\n" + "Search Product" + "\n")
    product_id = input("Enter Product ID: ")

    try: 
        found_product = inventory.search_product(product_id)
        product_info = found_product.display_information()
        print(
            " Product Found: " + "\n",
            "-----------------------------------" + "\n"
            f" ID: {product_info['ID']} \n", 
            f"Name: {product_info['Name']} \n", 
            f"Price: ${product_info['Price']} \n", 
            f"Stock: {product_info['Stock']} \n",
            "-----------------------------------" + "\n"
        )
    except:
        return False

def save_inventory(inventory):
    try:
        inventory_Data = inventory.get_Inventory()
        
        with open("inventory.json", "w") as file:
            json.dump(inventory_Data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving inventory: {e}")
    
def main():
    print(
        "===================================" + "\n" 
        + "INVENTORY MANAGEMENT SYSTEM " + "\n" + 
        "===================================" + "\n" 
    )
    inventory_data = load_inventory() 
    inventory = Inventory(inventory_data)
    print(
        "---------------MENU----------------" + "\n"
        + "1. Display All Products" + "\n"
        + "2. Add Product" + "\n"
        + "3. Update Stock" + "\n"
        + "4. Search Product" + "\n"
        + "5. Save Inventory" + "\n"      
        + "6. Exit" + "\n" +
        "-----------------------------------" + "\n"
    )

    while True:
        user_input = get_valid_input()

        if user_input == "1":
            try:
                inventory.display_all()
            except:
                print("Error occurred. Please try again")
                continue
        elif user_input == "2":
            return_value = add_product(inventory)
            if return_value is False:
                continue
            elif return_value:
                print("\n" + "Product added successfully!" + "\n")   
            else:
                print("Unexpected error occurred adding product. Please try again")
        elif user_input == "3":
            return_value = update_stock(inventory)
            if return_value:
                print("Stock updated successfully!")
            else:
                print("Stock update failed. Please try again.")
        elif user_input == "4":
            return_value = search_product(inventory)
            if return_value is False:
                print("Product not found." + "\n")
        elif user_input == "5":
            return_value = save_inventory(inventory)
            if return_value:
                print(
                    "\n" + "Saving inventory..." 
                    "\n" + "Inventory saved successfully to inventory.json!"
                )
        elif user_input is False:
            return_value = save_inventory(inventory)
            if return_value:
                print(
                    "\n" + "Saving inventory before exit..." 
                    "\n" + "Inventory saved successfully"
                    "\n" + 
                    "\n" + "Thank you for using the Inventory Management System."
                    "\n" + "Program Terminated."
                )
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()



