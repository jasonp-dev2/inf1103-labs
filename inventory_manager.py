#  Inventory Manager

import json
import Product
import Inventory

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
            print("Inventory loaded successfully." + "\n")
        return inventory
    except FileNotFoundError:
        print("inventory.json not found. Creating a new inventory.json file.")
        initial_inventory = {}
        with open("inventory.json", "w") as file:
            json.dump(initial_inventory, file)
        return initial_inventory

def display_all_products(inventory):
    print("\n" + "Current Inventory: " + "\n")
    print("-----------------------------------" + "\n")
    for info in inventory.values():
        print(
            f"ID: {info['ID']}", 
            f" | Name: {info['Name']}", 
            f" | Price: ${info['Price']}", 
            f" | Stock: {info['Stock']}" 
        )
    print("\n" + "-----------------------------------" + "\n")

def add_product(inventory):    
    product_Id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = float(input("Price: "))
    formatted_price = f"{product_price:.2f}"
    product_stock = int(input("Stock Quantity: "))
    
    if product_stock>500:
        print("Stock limit exceeded. Cannot add product with stock greater than 500. Please try again")
        return False

    product = Product(product_Id, product_name, formatted_price, product_stock) #create product using product_Id as name
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
            f"Name: {product_info["Name"]} \n", 
            f"Current Stock: {product_info["Stock"]} \n" 
        )
        new_stock = int(input("Enter new stock quantity: "))
        found_product.update_stock(new_stock)

    for products in inventory:
        product_info = products.display_information()
        if product_info["ID"] == product_id:
            found_product = product_info
            #product = inventory[product_id]
            print(
                "\n" + 
                f"Product Found: \n", 
                f"Name: {found_product["Name"]} \n", 
                f"Current Stock: {found_product["Stock"]} \n" 
            )
            new_stock = int(input("Enter new stock quantity: "))

            #product["Stock"] = new_stock
            return inventory 
        
    else:
        return None


def search_product(inventory):
    print("\n" + "Search Product" + "\n")
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        product = inventory[product_id]
        #product.displayinformation()
        print(
            " Product Found: " + "\n",
            "-----------------------------------" + "\n"
            f"ID: {product['ID']} \n", 
            f"Name: {product['Name']}", 
            f"Price: ${product['Price']} \n", 
            f"Stock: {product['Stock']} \n",
            "-----------------------------------" + "\n"
        )
    else:
        return False

def save_inventory(inventory):
    try:
        with open("inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving inventory: {e}")
    
def main():
    print(
        "===================================" + "\n" 
        + "INVENTORY MANAGEMENT SYSTEM " + "\n" + 
        "===================================" + "\n" 
    )
    #inventory_data = load_inventory() old code
    inventory = Inventory(load_inventory)
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
            #display_all_products(inventory) old code
            inventory.display_all()
        elif user_input == "2":
            return_value = add_product(inventory)
            if return_value is False:
                continue
            elif return_value is True:
                print("\n" + "Product added successfully!" + "\n")   
            else:
                print("Unexpected error occurred adding product. Please try again")
            """
            old code
            return_value = add_product(inventory)
            if return_value is None:
                continue
            else:
                print("\n" + "Product added successfully!" + "\n")
                """
        elif user_input == "3":
            return_value = update_stock(inventory_data)
            if return_value:
                print("Stock updated successfully!")
            else:
                print("Stock update failed. Please try again.")
        elif user_input == "4":
            return_value = search_product(inventory_data)
            if return_value is False:
                print("Product not found." + "\n")
        elif user_input == "5":
            return_value = save_inventory(inventory_data)
            if return_value:
                print(
                    "\n" + "Saving inventory..." 
                    "\n" + "Inventory saved successfully to inventory.json!"
                )
        elif user_input is False:
            return_value = save_inventory(inventory_data)
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



