# Smart Vending Machine

dispense_counter = 0

def dispense_drink(drink_name):
    print(f"Dispensing {drink_name}")

while True:
    user_input = input("Please enter the drink you would like (Coke, Juice, Water): ")
    if user_input.lower() in ["coke", "juice", "water"]:
        dispense_drink(user_input.capitalize())
        dispense_counter += 1
    else:
        print("Drink not available.")
        break

print(f"Total drinks dispensed: {dispense_counter}")  