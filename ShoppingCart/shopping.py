def get_order():
    print("[command] [item] (command is 'a' to add, 'd' to delete, 'q' to quit): ")

    line = input()

    command = line[:1]
    item = line[2:]

    # returning a tuple
    return (command, item)

def process_order(order, cart):
    command, item = order

    if command == "a":
        if item not in cart:
            cart[item] = 1
        else:
            cart[item] += 1
            
    elif command == "d" and item in cart:
        cart[item] -= 1

        if cart[item] == 0:
            del cart[item]
        
    elif command == "q":
        return False

    return True
    
def go_shopping():
    cart = dict()

    while True:
        order = get_order()

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")

go_shopping()
