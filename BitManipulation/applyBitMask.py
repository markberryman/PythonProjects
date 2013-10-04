import math


class ApplyBitMask(object):
    """Given two 32-bit numbers N and M and a range from I to J,
       replace the bits in N in range I to J w/ the bits in M.
       For example:
       N = 10000000000
       M = 10101
       I = 2, J= 6
       Result = 10000101010"""

    def create_sub_mask(self, I, J):
        """Creates a bit mask of all 1's except for
        a range of 0's as specified in the range
        between I and J. Note, they're 1-based."""
        # start w/ all 1's
        num = int(math.pow(2, 32) - 1)

        # slap in the 0's
        while (J >= I):
            num -= int(math.pow(2, J - 1))
            J -= 1

        return num
       
    def apply_mask(self, N, M, I, J):
        """Note, J and I are 1 based and J >= I."""
        assert J >= I

        # create mask that 0's out portion of N to replace w/ M
        mask = self.create_sub_mask(I, J)

        # apply mask
        nPrime = N & mask

        # scoot M over to the range area
        mPrime = M << (I - 1)

        return nPrime | mPrime
