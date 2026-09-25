# Persistent Inventory Auditor

# python list (array) for inventory,
# inventory = [transaction count, total inventory, failed entries]
# Current inventory: in get_valid_input 
# 

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
        with open("inventory.txt", "r") as file:
            for line in file:
                inventory_List = line.strip("[]").split(",")
                inventory_Qty = int(inventory_List[1])
                inventory_FailedEntries = int(inventory_List[2])
                return sum(int(inventory_Qty)), sum(int(inventory_FailedEntries))
    except FileNotFoundError:
        initial_inventory = [0, 20, 0]
        with open("inventory.txt", "w") as file:
            file.write(str(initial_inventory) + "\n")
        return initial_inventory[1], initial_inventory[2]

        

def save_inventory(inventory, failed_entries):
    inventory_List = [inventory, failed_entries]

    with open("inventory.txt", "a") as file:
        with open("inventory.txt", "r") as f:
            last_entry = f.readlines()[-1]
        last_entryId = last_entry.strip("[]").split(",")[0]
        new_entryId = int(last_entryId) + 1
        inventory_List.insert(0, new_entryId)
        file.write(str(inventory_List) + "\n")
        
def main():
    user_input = ""
    quit = False
    inventory, failedentry = load_inventory()
    print("Current Inventory: ", inventory)
    print("Current Failed Entries: ", failedentry)

    while (quit==False):
        user_input = get_valid_input()
        if user_input is not None and user_input is not True:
            inventory = process_delivery(inventory, calculate_tax(user_input))
            save_inventory(inventory, failedentry)
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
    


