def process_orders(item_quantities, orders): #define order processing function, inputs are item qtys and order name
    remaining_quantities = item_quantities.copy() #remaining qtys based on input arg
    selected_quantities_per_order = {}    #selected quantities init to 0

    for order in orders:  #iterate through list of orders
        print(f"\nProcessing {order}...") #disp status
        print(f"Available quantities: {remaining_quantities}") #disp status

        selected_items = [] #init selected items to empty
        order_quantity_total = 0 #init to 0

        while True: #constantly loop for the order until  user selects done, then move on to next order
            selected_item = input(f"Select item for {order} (A, B, C, D) or 'done' to finish: ").upper()

            if selected_item == 'DONE':  #if user is done, then move on to next order
                break

            if selected_item in remaining_quantities: #if the item they select has supply, enter while loop
                while True:
                    try:
                        order_quantity = int(input(f"Enter quantity for {selected_item}: "))
                        if 0 <= order_quantity <= remaining_quantities[selected_item]:
                            break #if they order between 0 and whats left, exit while loop, otherwise print error msg
                        else:
                            print(f"Invalid quantity. Available quantity for {selected_item}: {remaining_quantities[selected_item]}")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.") #if they enter a non valid input, print error msg

                order_quantity_total += order_quantity #increment the total based on how much they ordered for this item (a,b,c,d)
                remaining_quantities[selected_item] -= order_quantity #subtract order qty. from remaining qty
                selected_items.append((selected_item, order_quantity)) #add the item they orered to the list of selected items

            else:
                print("Invalid input. Please select a valid item.")

        selected_quantities_per_order[order] = selected_items
        print(f"You selected in {order}: {', '.join([f'{item} = {qty}' for item, qty in selected_items])}")
        print(f"Remaining quantities after {order}: {remaining_quantities}")

    print(f"\nFinal remaining quantities: {remaining_quantities}")
    print(f"Quantities selected in each order: {selected_quantities_per_order}")

# Example usage:
item_quantities_available = {'A': 10, 'B': 20, 'C': 10, 'D': 5}
order_dict = {
    "Order1": 0,  # Initial values can be set to 0; the user will select the item and quantity
    "Order2": 0,
    "Order3": 0,
    "Order4": 0
}

process_orders(item_quantities_available, order_dict)
