#  Inventory Manager

#data structure is ID: 001 | Name: Laptop | Price: $100.5 | Stock: 50


import ast
import json
import pprint

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
        return inventory
    except FileNotFoundError:
        print("inventory.json not found. Creating a new inventory.json file.")
        initial_inventory = {}
        with open("inventory.json", "w") as file:
            json.dump(initial_inventory, file)
        return initial_inventory

def display_all_products(inventory):
    print("Current Inventory: " + "\n")
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
    print("Add Product" + "\n")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = float(input("Product Price: "))
    formatted_price = f"${product_price:.2f}"
    product_stock = int(input("Product Stock: "))
    taxed_stock = calculate_tax(product_stock)
    if product_stock>500:
        print("Stock limit exceeded. Cannot add product with stock greater than 500.")
        return None

    product_entry = {
        "ID": product_id,
        "Name": product_name,
        "Price": formatted_price,
        "Stock": taxed_stock
    }
    inventory[product_id] = product_entry
    #print(str(product_entry))
    return inventory

def update_stock(inventory):
    print("Update Stock" + "\n")
    product_id = input("Enter Product ID: ")
    print("Searching for product in inventory...", inventory[product_id])

    try:
        for product_id, selected_product in inventory.items():
            print("Selected Product: ", selected_product["ID"] + "\n")
            print(
                f"Product Found: \n", 
                f"Selected Product: {selected_product["Name"]} \n", 
                f"Stock: {selected_product["Stock"]} \n" 
            )
            new_stock = int(input("Enter new stock quantity: "))
            selected_product["Stock"] = calculate_tax(new_stock)
            print("Stock updated successfully for product ID: ", selected_product["ID"])
            print("Updated Stock: ", selected_product["Stock"])
            return inventory
    except:
        return None


def search_product():
    pass

def process_delivery(current_total, new_value):
    inventory = current_total + new_value
    return inventory

def calculate_tax(amount):
    amount += amount * 0.1
    return round(amount)

def generate_Report(total_units, failed_entries):
    print("Total Deliveries Processed: ", total_units)
    print("Number of Failed/Rejected entries: ", failed_entries)

def save_inventory(taxed_user_input, failed_entries):
    with open("inventory.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]
    if lines:
        last_record = ast.literal_eval(lines[-1])
        new_entryId = last_record[0] + 1

    new_record = [new_entryId, taxed_user_input, failed_entries]
    with open("inventory.txt", "a") as file:
        file.write(str(new_record) + "\n")
        print("New inventory entry added: ")
        print("Entry ID: ", new_record[0], " | Inventory added: ", new_record[1], " | Failed Entries: ", new_record[2])
        print("\n" + "Inventory updated successfully to inventory.txt")
        
def main():
    print(
        "===================================" + "\n" 
        + "INVENTORY MANAGEMENT SYSTEM " + "\n" + 
        "===================================" + "\n" 
    )
    print("Inventory loaded successfully.")
    inventory = load_inventory()

    while True:
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
        user_input = get_valid_input()
        if user_input == "1":
            display_all_products(inventory)
        elif user_input == "2":
            return_value = add_product(inventory)
            if return_value is None:
                continue
            else:
                print("\n" + "Product added successfully!")
        elif user_input == "3":
            return_value = update_stock(inventory)
            if return_value:
                print("Stock updated successfully!")
            else:
                print("Stock update failed. Please try again.")
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        elif user_input is False:
            generate_Report(inventory)
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


"""taxed_user_input = calculate_tax(user_input)
            inventory = process_delivery(inventory, taxed_user_input)
            save_inventory(taxed_user_input, failedentry)
            if inventory>500:
                generate_Report(inventory, failedentry)
                break"""


