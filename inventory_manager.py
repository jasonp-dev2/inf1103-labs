#  Inventory Manager

import json

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
    for products, info in inventory.items():
        print(
            f"ID: {info["ID"]}", 
            f" | Name: {info["Name"]}", 
            f" | Price: ${info["Price"]}", 
            f" | Stock: {info["Stock"]}" 
        )
    print("\n" + "-----------------------------------" + "\n")

def add_product(inventory):    
    print("\n" + "Add New Product" + "\n")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = float(input("Price: "))
    formatted_price = f"{product_price:.2f}"
    product_stock = int(input("Stock Quantity: "))

    if product_stock>500:
        print("Stock limit exceeded. Cannot add product with stock greater than 500.")
        return None

    product_entry = {
        "ID": product_id,
        "Name": product_name,
        "Price": formatted_price,
        "Stock": product_stock
    }
    inventory[product_id] = product_entry
    #print(str(product_entry))
    return inventory

def update_stock(inventory):
    print("\n" + "Update Stock")
    product_id = input("Enter Product ID: ")

    try:
        for info in inventory[product_id].items():
            print(
                f"Product Found: \n", 
                f"Name: {inventory[product_id]['Name']} \n", 
                f"Current Stock: {inventory[product_id]['Stock']} \n" 
            )
            new_stock = int(input("Enter new stock quantity: "))
            inventory[product_id]["Stock"] = new_stock
            return inventory
    except:
        return None


def search_product(inventory):
    print("\n" + "Search Product" + "\n")
    product_id = input("Enter Product ID: ")
    if product_id in inventory:
        print(
            "Product Found: " + "\n",
            "-----------------------------------" + "\n"
            f" ID: {inventory[product_id]['ID']} \n", 
            f"Name: {inventory[product_id]['Name']}", 
            f"Price: ${inventory[product_id]['Price']} \n", 
            f"Stock: {inventory[product_id]['Stock']} \n",
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
    inventory = load_inventory()
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
            display_all_products(inventory)
        elif user_input == "2":
            return_value = add_product(inventory)
            if return_value is None:
                continue
            else:
                print("\n" + "Product added successfully!" + "\n")
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



