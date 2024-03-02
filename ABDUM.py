def process_order(order_number, available_quantities):

# Display of current order and available quantities
    print(f"\nProcessing {order_number}...")
    print(f"Available quantities: {available_quantities}")

    selected_quantities = {}
    while True:
        item = input(f"Select item for {order_number} (A, B, C, D, E, F) or 'done' to finish: ").upper()
        if item == 'DONE':
            break

        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if 0 <= quantity <= available_quantities[item]:
                selected_quantities[item] = quantity
            else:
                print(f"Invalid quantity. Available quantity for {item}: {available_quantities[item]}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    # Display the review of the order
    print(f"\nReview of {order_number}:")
    for item, quantity in selected_quantities.items():
        print(f"{item} = {quantity}")

    # Update available quantities based on selected quantities
    for item, quantity in selected_quantities.items():
        available_quantities[item] -= quantity

    # Display the available quantities after the order is completed
    print(f"\nAvailable quantities after {order_number}: {available_quantities}")

    return available_quantities

def process_orders(item_quantities, orders):
    remaining_quantities = item_quantities.copy()
    selected_quantities_per_order = {}

    # Process each order and update available quantities
    for order in orders:
        remaining_quantities = process_order(order, remaining_quantities.copy())
        selected_quantities_per_order[order] = remaining_quantities.copy()

    # Display final remaining quantities
    print("\nFinal remaining quantities:")
    for item, quantity in sorted(remaining_quantities.items()):
        print(f"{item}: {quantity}")

    # Display quantities selected in each order
    print("\nQuantities selected in each order:")
    for order, items in sorted(selected_quantities_per_order.items()):
        items_str = ', '.join([f'{item} = {qty}' for item, qty in sorted(items.items())])
        print(f"{order}: {items_str}")

# Initialization of quantities available in each group:
item_quantities_available = {'A': 7, 'B': 7, 'C': 7, 'D': 7, 'E': 7, 'F': 7}
order_dict = {
    "Order1": 0,
    "Order2": 0,
    "Order3": 0,
    "Order4": 0
}

process_orders(item_quantities_available, order_dict)
