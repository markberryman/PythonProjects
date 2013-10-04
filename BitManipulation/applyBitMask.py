class ApplyBitMask(object):
    """Given two 32-bit numbers N and M and a range from I to J,
       replace the bits in N in range I to J w/ the bits in M.
       For example:
       N = 10000000000
       M = 00000010101
       I = 2, J= 6
       Result = 10000101010"""

    def apply_mask(self, N, M, I, J):
        """Note, J and I are 1 based."""
