import math


class HighLow(object):
    """Given an integer, return the next highest and 
    lowest number that includes the same number of 1's
    as the integer's binary representation."""
    def set_bit(self, n, index, bit):
        """Sets the bit at the given index."""
        if (bit == 0):
            mask = ~(1 << index)
            n = n & mask
        else:
            n = n | (1 << index)

        return n

    def get_lsb(self, n):
        """Gets the least significant bit."""
        # todo - look at how to change this to get a bit at an index
        result = 0

        # if # is odd, lsb is 1; otherwise it's 0
        if ((n % 2) != 0):
            # odd
            result = 1

        return result

    def is_out_of_bits(self, n):
        return (n == 0)
    
    def swap_msbs(self, n, bitToTargetForSwapIdx):
        """01... -> 10..."""
        n = self.set_bit(n, bitToTargetForSwapIdx, 1)
        n = self.set_bit(n, bitToTargetForSwapIdx - 1, 0)

        return n

    def find_higher(self, n):
        result = n
        bitToTargetForSwapIdx = 0
        foundFirstOneIdx = 0
        foundLastOneIdx = 0
        # todo - do i need this?
        needToMoveDownOnes = False

        while (n != 0):
            if (self.get_lsb(n) != 0):
                # found a '1'
                n = n >> 1
                foundFirstOneIdx = bitToTargetForSwapIdx
                bitToTargetForSwapIdx += 1

                while (n != 0):
                    if (self.get_lsb(n) != 1):
                        # found a '0'
                        # we've found the "01" flip (remember, scanning RTL)
                        result = self.swap_msbs(result, bitToTargetForSwapIdx)                        
                    else:
                        # keep looking
                        n = n >> 1                    
                        bitToTargetForSwapIdx += 1

                # if we've run out of bits, we've crossed the "01" flip
                if (n == 0):
                    result = self.swap_msbs(result, bitToTargetForSwapIdx)

            else:
                # keep looking
                n = n >> 1
                bitToTargetForSwapIdx += 1
                needToMoveDownOnes = True

        # move down preceeding 1's
        foundLastOneIdx = bitToTargetForSwapIdx - 2

        if (needToMoveDownOnes):
            # set to '0' all bits in the range of foundLastOneIdx to foundFirstOneIdx
            for x in range(foundFirstOneIdx, foundLastOneIdx + 1):
                self.set_bit(x, 0)

            # add the '1's by "or'ing" in a number equal to math.pow(foundLastOneIdx - foundFirstOneIdx)
            orNumber = 0

            if ((foundLastOneIdx - foundFirstOneIdx) == 0):
                orNumber += 1
            else:
                for x in range(foundLastOneIdx - foundFirstOneIdx):
                    orNumber += math.pow(2, x - 1)

            result = int(result) | orNumber

        return result