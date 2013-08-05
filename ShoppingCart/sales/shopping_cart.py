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
