# ModularvSmart Inventory Auditor

def get_valid_input():
    failedentry = 0
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

def main():
    user_input = ""
    quit = False
    inventory = 0
    failedentry = 0

    while (quit==False):
        user_input = get_valid_input()
        if user_input is not None and user_input is not True:
            print("Incoming delivery: ", user_input)
            print("Inventory before processing delivery: ", inventory)
            inventory = process_delivery(inventory, user_input)
            print("Inventory after processing delivery: ", inventory)
            inventory = calculate_tax(inventory)
            if inventory>500:
                print("Inventory limit exceeded.")
                generate_Report(inventory, failedentry)
                break
            print("Inventory after tax calculation: ", inventory)
        elif user_input is True:
            generate_Report(inventory, failedentry)
        else:
            failedentry += 1
            print("Failed entries so far: ", failedentry)
            print("No valid input received. Please try again.")

if __name__ == "__main__":
    main()
    


