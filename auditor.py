# Smart Inventory Auditor

inventory = 0
quit = False
quit_or_continue = ""

while (quit==False):
    stockqty = input("Please enter stock quantity:")
    if(stockqty.isdigit()):
        if(int(stockqty)<0):
                print("Stock quantity cannot be negative.")
                continue
        else:  
            inventory = inventory+int(stockqty)
    else:
        print("Stock quantity must be a number.")
        continue
    quit_or_continue = input("To quit, enter 'quit'. Otherwise, to continue adding entries, press Enter:")
    if quit_or_continue == "quit":
        quit = True
    elif quit_or_continue != "":
        quit_or_continue = input("Invalid input. Please enter 'quit' to exit or press Enter to continue.")

