# Inventory Manager

import csv
import json
from math import isfinite

from Product import Product
from ProductFactory import ProductFactory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Inventory import Inventory
from Order import Order


def get_valid_input() -> str | bool | None:
    user_input: str = input("Enter option: ").strip()

    if user_input in ("1", "2", "3", "4", "5", "6", "8"):
        return user_input
    elif user_input == "7":
        return False
    else:
        return None


def load_inventory() -> tuple[dict[str, Product], dict[str, Supplier]]:
    try:
        with open("inventory.json", "r") as file:
            print("inventory.json found.")
            data: dict[str, dict[str, dict]] = json.load(file)

        initialised_inventory: dict[str, Product] = {}
        suppliers: dict[str, Supplier] = {}

        extra_fields = {"Physical": "Weight", "Digital": "Download_Size"}
        for category, products in data.items():
            if category not in extra_fields:
                continue
            for product_id, item in products.items():
                supplier: Supplier | None = None
                supplier_data: dict[str, str] | None = item.get("Supplier")
                if supplier_data:
                    sup_id: str = supplier_data["ID"]
                    if sup_id not in suppliers:
                        suppliers[sup_id] = Supplier(
                            sup_id,
                            supplier_data["Name"],
                            supplier_data["Contact Email"],
                        )
                    supplier = suppliers[sup_id]

                initialised_inventory[product_id] = ProductFactory.create(
                    category.lower(),
                    item["ID"],
                    item["Name"],
                    item["Price"],
                    item["Stock"],
                    item[extra_fields[category]],
                    supplier,
                )
        print("Inventory loaded successfully.\n")
        return initialised_inventory, suppliers
    except FileNotFoundError:
        print("inventory.json not found. Creating a new inventory.json file.")
        empty_schema: dict[str, dict] = {"Physical": {}, "Digital": {}}
        with open("inventory.json", "w") as file:
            json.dump(empty_schema, file, indent=4)
        return {}, {}


def load_products(
    path: str, inventory: Inventory, supplier: Supplier | None = None
) -> dict[str, Product]:
    loaded: dict[str, Product] = {}
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            rows = csv.reader(file)
            next(rows, None)
            for row_number, row in enumerate(rows, start=2):
                try:
                    kind, product_id, name, price, stock = row
                    # The supplied CSV does not include weight or download size.
                    product = ProductFactory.create(
                        kind, product_id, name, float(price), int(stock), 0.0, supplier
                    )
                    if not inventory.add_product(product):
                        raise ValueError(f"Product ID already exists: {product_id}")
                    loaded[product_id] = product
                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")
        print(f"{len(loaded)} products loaded.")
    finally:
        print("Load attempt finished.")
    return loaded


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")
        else:
            if isfinite(value) and value > 0:
                return value
            print("Please enter a number greater than zero.")


def _print_product_details(product: Product) -> None:
    product_info: dict[str, str | float | int] = product.display_information()
    print(
        f" ID: {product_info['ID']} \n",
        f"Name: {product_info['Name']} \n",
        f"Price: ${product_info['Price']} \n",
        f"Stock: {product_info['Stock']} \n",
    )
    if product.supplier is not None:
        sup_info: dict[str, str] = product.supplier.display_information()
        print(
            f" Supplier: {sup_info['Name']} ({sup_info['ID']}) - {sup_info['Contact Email']} \n"
        )
    if isinstance(product, PhysicalProduct):
        print(
            f" Weight: {product_info['Weight']}KG \n",
            f"Cost of shipping: ${product.calculate_shipping_cost()} \n",
            f"{product.get_fulfilment_info()} \n",
        )
    elif isinstance(product, DigitalProduct):
        print(
            f"Download_Size: {product_info['Download_Size']}MB \n",
            f"{product.get_fulfilment_info()}\n",
        )


def display_all_products(
    inventory: Inventory, inventory_data: dict[str, Product]
) -> None:
    print("\nCurrent Inventory: ")
    print("-----------------------------------\n")
    try:
        inventory.display_all_products()
        for product in inventory_data.values():
            _print_product_details(product)
    except KeyError as error:
        print("Error retrieving inventory:", error)
    print("\n-----------------------------------\n")


def prompt_supplier(suppliers: dict[str, Supplier]) -> Supplier | None:
    choice: str = input("Attach a supplier? (y/n): ").strip().lower()
    if choice != "y":
        return None

    supplier_id: str = input("Supplier ID: ").strip()
    if supplier_id in suppliers:
        existing: Supplier = suppliers[supplier_id]
        print(f"Using existing supplier: {existing.display_information()['Name']}")
        return existing

    supplier_name: str = input("Supplier Name: ").strip()
    supplier_contact: str = input("Supplier Contact Email: ").strip()
    new_supplier = Supplier(supplier_id, supplier_name, supplier_contact)
    suppliers[supplier_id] = new_supplier
    return new_supplier


def add_product(
    inventory: Inventory,
    inventory_data: dict[str, Product],
    suppliers: dict[str, Supplier],
) -> bool:
    product: Product
    product_id: str
    while True:
        try:
            product_type: str = input(
                "Type '1' to enter a physical product, '2' for a digital product: "
            ).strip()

            if product_type in ("1", "2"):
                product_id = input("Product ID: ").strip()
                product_name: str = input("Product Name: ").strip()
                product_price: float = round(get_positive_float("Price: "), 2)
                product_stock: int = int(input("Stock Quantity: "))

                if product_stock > 500:
                    print("Stock limit exceeded. Cannot add product with stock greater than 500")
                    continue

                supplier: Supplier | None = prompt_supplier(suppliers)

                if product_type == "1":
                    kind = "physical"
                    extra_value = round(float(input("Weight: ")), 2)
                else:
                    kind = "digital"
                    extra_value = round(float(input("Download_Size: ")), 2)
                product = ProductFactory.create(
                    kind, product_id, product_name, product_price, product_stock,
                    extra_value, supplier,
                )
                break
            else:
                print("Invalid choice. Enter '1' or '2'.")
        except ValueError as error:
            print(f"Invalid input: {error}. Please try again.")
            continue

    if inventory.add_product(product):
        inventory_data[product_id] = product
        return True
    return False


def update_stock(inventory: Inventory) -> bool:
    print("\nUpdate Stock")
    product_id: str = input("Enter Product ID: ").strip()

    found_product: Product | None = inventory.find_product(product_id)
    if found_product is None:
        return False

    try:
        product_info: dict[str, str | float | int] = found_product.display_information()
        print(
            "\nProduct Found: \n",
            f"Name: {product_info['Name']} \n",
            f"Current Stock: {product_info['Stock']} \n",
        )
        new_stock: int = int(input("Enter new stock quantity: "))
        if new_stock > 500:
            print("Stock quantity can't be above 500. Please try again")
            return False
        found_product.update_stock(new_stock)
        return True
    except ValueError:
        return False


def search_product(inventory: Inventory) -> bool:
    print("\nSearch Product\n")
    product_id: str = input("Enter Product ID: ").strip()

    found_product: Product | None = inventory.find_product(product_id)
    if found_product is None:
        return False

    print(" Product Found: \n-----------------------------------")
    _print_product_details(found_product)
    print("-----------------------------------\n")
    return True


def create_order(inventory: Inventory) -> None:
    print("\nCreate New Order")
    order_id: str = input("Enter Order ID (e.g., ORD-001): ").strip()
    order = Order(order_id)

    while True:
        print(
            f"\n--- Order {order.order_id} Menu ---\n"
            "1. Add Item to Order\n"
            "2. Remove Item from Order\n"
            "3. View Order Summary\n"
            "4. Confirm & Checkout\n"
            "5. Cancel Order"
        )
        action: str = input("Choose action: ").strip()

        if action == "1":
            product_id: str = input("Enter Product ID to order: ").strip()
            product: Product | None = inventory.find_product(product_id)
            if product is None:
                print("Product not found in inventory.")
                continue

            try:
                qty: int = int(input("Enter quantity: "))
                current_stock: int = int(product.display_information()["Stock"])
                already_in_order: int = sum(
                    line.quantity
                    for line in order.order_lines
                    if line.product.display_information()["ID"] == product_id
                )
                if qty + already_in_order > current_stock:
                    print(f"Insufficient stock. Available: {current_stock - already_in_order}")
                    continue

                order.add_order_line(product, qty)
                print(f"Added {qty} x {product.display_information()['Name']} to order.")
            except ValueError as error:
                print(f"Invalid quantity: {error}")

        elif action == "2":
            product_id = input("Enter Product ID to remove from order: ").strip()
            if order.remove_order_line(product_id):
                print("Order line removed.")
            else:
                print("Product not found in this order.")

        elif action == "3":
            print(f"\n=== Order Summary: {order.order_id} ===")
            if not order.order_lines:
                print("Order has no items.")
            else:
                for line in order.order_lines:
                    info = line.product.display_information()
                    print(
                        f"- {info['Name']} ({info['ID']}) x{line.quantity} "
                        f"@ ${info['Price']} = ${line.calculate_subtotal():.2f}"
                    )
                print(f"Total: ${order.calculate_total():.2f}")

        elif action == "4":
            if not order.order_lines:
                print("Cannot confirm an empty order.")
                continue

            for line in order.order_lines:
                current_stock = int(line.product.display_information()["Stock"])
                line.product.update_stock(current_stock - line.quantity)

            print(
                f"\nOrder {order.order_id} confirmed! "
                f"Total charged: ${order.calculate_total():.2f}. Stock updated.\n"
            )
            break

        elif action == "5":
            print("Order cancelled.\n")
            break
        else:
            print("Invalid option.")


def save_inventory(inventory_data: dict[str, Product]) -> bool:
    try:
        categorised_data: dict[str, dict[str, dict]] = {
            "Physical": {},
            "Digital": {},
        }

        for product_id, product in inventory_data.items():
            product_record: dict = dict(product.display_information())
            if product.supplier is not None:
                product_record["Supplier"] = product.supplier.display_information()

            if isinstance(product, PhysicalProduct):
                categorised_data["Physical"][product_id] = product_record
            elif isinstance(product, DigitalProduct):
                categorised_data["Digital"][product_id] = product_record

        with open("inventory.json", "w") as file:
            json.dump(categorised_data, file, indent=4)
        return True
    except (OSError, TypeError) as error:
        print(f"Error saving inventory: {error}")
        return False


def main() -> None:
    print(
        "===================================\n"
        + "INVENTORY MANAGEMENT SYSTEM \n"
        + "===================================\n"
    )
    inventory_data, suppliers = load_inventory()
    inventory: Inventory = Inventory(inventory_data)
    print(
        "---------------MENU----------------\n"
        + "1. Display All Products\n"
        + "2. Add Product (with optional Supplier)\n"
        + "3. Update Stock\n"
        + "4. Search Product\n"
        + "5. Create Order\n"
        + "6. Save Inventory\n"
        + "7. Exit\n"
        + "8. Load Products from CSV\n"
        + "-----------------------------------\n"
    )

    while True:
        user_input: str | bool | None = get_valid_input()

        if user_input == "1":
            display_all_products(inventory, inventory_data)
        elif user_input == "2":
            if add_product(inventory, inventory_data, suppliers):
                print("\nProduct added successfully!\n")
            else:
                print("Product ID already exists. Please try again.")
        elif user_input == "3":
            if update_stock(inventory):
                print("Stock updated successfully!")
            else:
                print("Stock update failed. Please try again.")
        elif user_input == "4":
            if not search_product(inventory):
                print("Product not found.\n")
        elif user_input == "5":
            create_order(inventory)
        elif user_input == "6":
            if save_inventory(inventory_data):
                print(
                    "\nSaving inventory..."
                    "\nInventory saved successfully to inventory.json!"
                )
        elif user_input == "8":
            path = input("CSV path [products.csv]: ").strip() or "products.csv"
            inventory_data.update(load_products(path, inventory))
        elif user_input is False:
            if save_inventory(inventory_data):
                print(
                    "\nSaving inventory before exit..."
                    "\nInventory saved successfully\n\n"
                    "Thank you for using the Inventory Management System.\n"
                    "Program Terminated."
                )
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
