# Smart Inventory Auditor

inventory = 0
quit = False
failedentry = 0
quit_or_continue = ""

while (quit==False):
    stockqty = input("Please enter stock quantity:")
    if(stockqty.isdigit()):
        if(int(stockqty)<0):
            print("Stock quantity cannot be negative.")
            failedentry = failedentry + 1
            continue
        else:  
            inventory = inventory+int(stockqty)
    else:
        print("Stock quantity must be a number.")
        failedentry = failedentry + 1
        continue
    if inventory>500:
        print("Inventory limit exceeded.")
        break
    quit_or_continue = input("To quit, enter 'quit'. Otherwise, to continue adding entries, press Enter:")
    if quit_or_continue == "quit":
        quit = True
    elif quit_or_continue != "":
        quit_or_continue = input("Invalid input. Please enter 'quit' to exit or press Enter to continue.")

print("Total Units Processed: ", inventory)
print("Total Failed entries: ", failedentry)

