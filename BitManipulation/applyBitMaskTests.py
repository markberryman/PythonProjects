import applyBitMask
import math
import unittest


class CreateSubMaskTests(unittest.TestCase):
    def test_i1j1(self):
        I = 1
        J = 1
        all1s = int(math.pow(2, 32) - 1)
        expected = int(all1s - math.pow(2, 0))
        sut = applyBitMask.ApplyBitMask()

        actual = sut.create_sub_mask(I, J)

        self.assertEqual(expected, actual)

    def test_i1j2(self):
        I = 1
        J = 2
        all1s = int(math.pow(2, 32) - 1)
        expected = int(all1s - math.pow(2, 1) - math.pow(2, 0))
        sut = applyBitMask.ApplyBitMask()

        actual = sut.create_sub_mask(I, J)

        self.assertEqual(expected, actual)

    def test_i4j6(self):
        I = 4
        J = 6
        all1s = int(math.pow(2, 32) - 1)
        expected = int(all1s - math.pow(2, 5) - math.pow(2, 4) - math.pow(2, 3))
        sut = applyBitMask.ApplyBitMask()

        actual = sut.create_sub_mask(I, J)

        self.assertEqual(expected, actual)

    def test_i2j6(self):
        I = 2
        J = 6
        all1s = int(math.pow(2, 32) - 1)
        expected = int(all1s - math.pow(2, 5) - math.pow(2, 4) - math.pow(2, 3) - math.pow(2, 2) - math.pow(2, 1))
        sut = applyBitMask.ApplyBitMask()

        actual = sut.create_sub_mask(I, J)

        self.assertEqual(expected, actual)

class ApplyMaskTests(unittest.TestCase):
    def test_BaseCase(self):
        # N = 10000000000
        # M = 10101
        # I = 2, J= 6
        # R = 10000101010
        N = int(math.pow(2, 10))
        M = int(math.pow(2, 4) + math.pow(2, 2) + math.pow(2, 0))
        I = 2
        J = 6
        expected = int(math.pow(2, 10) + math.pow(2, 5) + math.pow(2, 3) + math.pow(2, 1))
        sut = applyBitMask.ApplyBitMask()

        actual = sut.apply_mask(N, M, I, J)

        self.assertEqual(expected, actual)

    def test_TotalReplace(self):
        # N = 10000000000
        # M = <32 1's>
        # I = 1, J= 32
        # R = <all 1's>
        N = int(math.pow(2, 10))
        M = int(math.pow(2, 32) - 1)
        I = 1
        J = 32
        expected = M
        sut = applyBitMask.ApplyBitMask()

        actual = sut.apply_mask(N, M, I, J)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
