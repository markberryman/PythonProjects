class Cart:
    def __init__(self):
        self._contents = dict()

    # controls behavior of "print" method call
    def __repr__(self):
        # the __dict__ property contains the internal
        # contents of an object
        return "{0} {1}".format(Cart, self.__dict__)

    def process(self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 1
            else:
                self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1

                if self._contents[order.item] == 0:
                    del self._contents[order.item]
        

class Order:
    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] (command is 'a' to add, 'd' to delete, 'q' to quit): ")

        line = input()

        command = line[:1]
        self.item = line[2:]

        if command == "a":
            self.add = True
        elif command == "d":
            self.delete = True
        elif command == "q":
            self.quit = True


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

    while True:
        order = get_order()

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished!")

cart = Cart()
order = Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = Order()
    order.get_input()

print(cart)
