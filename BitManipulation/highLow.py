import math

# todo - implement the next lowest # portion of the code
class HighLow(object):
    """Given an integer, return the next highest and 
    lowest number that includes the same number of 1's
    as the integer's binary representation."""
    def get_bit(self, n, index):
        """Returns a boolean w/ True equaling 1."""
        return (n & (1 << index)) > 0

    def set_bit(self, n, index, bit):
        """Sets the bit at the given index."""
        print("Setting bit at index {} to {}".format(index, bit))

        if (bit == 0):
            mask = ~(1 << index)
            n = n & mask
        else:
            n = n | (1 << index)

        return n

    def find_higher(self, n):
        if (n <= 0):
            return 0

        # scan RTL looking for "01" which we'll flip
        index = 0
        # number of 1's to push down
        onesCount = 0
        # eat 0's
        while (self.get_bit(n, index) is False):
            index += 1

        #print("Found first '1' at index " + str(index))

        # we've found a 1, eat 1's; next 0 is the "01" flip
        while (self.get_bit(n, index) is True):
            onesCount += 1
            index += 1

        #print("Found the next '0' at index " + str(index))
        
        # at the flipping point
        n = self.set_bit(n, index, 1)
        n = self.set_bit(n, index - 1, 0)
        #print("Post msb bit swap, value is " + str(n))

        # as part of the swap, we'll whack one of the 1's we
        # counted as needing to move down
        onesCount -= 1

        #print("Number of 1's to possibly move down: " + str(onesCount))

        # move down 1's
        # first we'll turn their spots
        # to zero and then we'll put them back
        for x in range(index - onesCount - 1, index - 1):
            n = self.set_bit(n, x, 0)

        for x in range(0, onesCount):
            n = self.set_bit(n, x, 1)

        return n
