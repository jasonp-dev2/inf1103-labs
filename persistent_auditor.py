# Persistent Inventory Auditor

# python list (array) for inventory,
# inventory = [transaction count, total inventory, failed entries]
# Current inventory: in get_valid_input 

import ast

def get_valid_input():
    user_input = input("Please enter stock quantity (To quit, enter 'quit'): ")
    if user_input.lower() == "quit":
        quit = True
        return quit
    if(user_input.isdigit()):
        if(int(user_input)<0):
            return None
        else:  
            return int(user_input)
    else:
        return None

def process_delivery(current_total, new_value):
    inventory = current_total + new_value
    return inventory

def calculate_tax(amount):
    amount += amount * 0.1
    return round(amount)

def generate_Report(total_units, failed_entries):
    print("Total Deliveries Processed: ", total_units)
    print("Number of Failed/Rejected entries: ", failed_entries)

def load_inventory():
    try:
        total_qty = 0
        total_failed_entries = 0
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                record = ast.literal_eval(line)
                total_qty += record[1]
                total_failed_entries += record[2]
        return total_qty, total_failed_entries    
    
    except FileNotFoundError:
        initial_inventory = [0, 0, 0]
        with open("inventory.txt", "w") as file:
            file.write(str(initial_inventory) + "\n")
        return initial_inventory[1], initial_inventory[2]

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
    user_input = ""
    quit = False
    inventory, failedentry = load_inventory()

    while (quit==False):
        print("\nCurrent Inventory entries: " + "\n")
        with open("inventory.txt", "r") as file:
            for line in file:
                inventory_List = line.strip("[]").split(",")
                print("Entry ID: ", inventory_List[0], " | Inventory added: ", inventory_List[1], " | Failed Entries: ", inventory_List[2])
        user_input = get_valid_input()
        if user_input is not None and user_input is not True:
            taxed_user_input = calculate_tax(user_input)
            inventory = process_delivery(inventory, taxed_user_input)
            save_inventory(taxed_user_input, failedentry)
            if inventory>500:
                generate_Report(inventory, failedentry)
                break
        elif user_input is True:
            generate_Report(inventory, failedentry)
            break
        else:
            failedentry += 1
            print("No valid input received. Please try again.")

if __name__ == "__main__":
    main()
    


