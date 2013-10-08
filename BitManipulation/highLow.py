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

    def move_down_ones(self, n, onesStartIdx, numOnesToMove):
        result = n

        # replace the 1's w/ 0's
        for x in range(onesStartIdx, onesStartIdx + numOnesToMove):
            n = self.set_bit(n, x, 0)

        # move down the one's by replacing the beginning 0's w/ 1's
        for x in range(0, numOnesToMove):
            n = self.set_bit(n, x, 1)

        return n

    def find_higher(self, n):
        result = n
        bitToTargetForSwapIdx = 0
        onesStartIdx = 0
        numOnesToMoveDown = 0

        while (n != 0):
            if (self.get_lsb(n) != 0):
                # found a '1'
                n = n >> 1
                onesStartIdx = bitToTargetForSwapIdx
                bitToTargetForSwapIdx += 1

                while (n != 0):
                    if (self.get_lsb(n) != 1):
                        # found a '0'
                        # we've found the "01" flip (remember, scanning RTL)
                        result = self.swap_msbs(result, bitToTargetForSwapIdx)
                        # taking away 1 b/c we don't need to move down the
                        # 1 we just swapped
                        numOnesToMoveDown -= 1
                    else:
                        # keep looking
                        n = n >> 1                    
                        bitToTargetForSwapIdx += 1
                        numOnesToMoveDown += 1

                # if we've run out of bits, we've crossed the "01" flip
                if (n == 0):
                    result = self.swap_msbs(result, bitToTargetForSwapIdx)

            else:
                # keep looking
                n = n >> 1
                bitToTargetForSwapIdx += 1

        result = self.move_down_ones(result, onesStartIdx, numOnesToMoveDown)

        return result
