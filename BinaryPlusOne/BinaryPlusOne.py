class BinaryPlusOne(object):
    @staticmethod
    def add_one(num):
        """Pass in an array representing an array of bits."""
        result = None
        # start from rightmost bit
        bitIndex = len(num) - 1
        
        # look at rightmost bit
        rBit = num[bitIndex]
        # if it's a zero, replace w/ a one
        if (rBit == 0):
            num[bitIndex] = 1
        else:
            # if it's a one, replace w/ a zero
            num[bitIndex] = 0
            # now we're in the "carry" phase
            while (True):
                # look at next digit (going left)
                bitIndex -= 1
                # if it's a zero, replace w/ a one
                if (num[bitIndex] == 0):
                    num[bitIndex] = 1
                    break
                else:
                    # if it's a one, replace w/ a zero; continue
                    num[bitIndex] = 0