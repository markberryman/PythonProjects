import recursiveBacktracking
import unittest

class CanPlaceQueenTests(unittest.TestCase):
    def test_RowConflictReturnsFalse(self):
        # x o o
        # o o o
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 1)

        self.assertFalse(actual)

    def test_RowConflictReturnsFalse(self):
        # o x o
        # o o o
        # o o o
        board = [[0,0,1], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 0)

        self.assertFalse(actual)

    def test_ColConflictReturnsFalse(self):
        # x o o
        # o o o       
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 1, 0)

        self.assertFalse(actual)

    def test_ColConflictReturnsFalse(self):
        # x o o
        # o o o       
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 0)

        self.assertFalse(actual)

    def test_DiagConflictDownAndRightReturnsFalse(self):
        # x o o
        # o o o     
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 1, 1)

        self.assertFalse(actual)

    def test_DiagConflictUpAndLeftReturnsFalse(self):
        # x o o
        # o o o
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 2)

        self.assertFalse(actual)


    def test_ExactSpaceConflictReturnsFalse(self):
        # x o o
        # o o o     
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 0)

        self.assertFalse(actual)

    def test_NoConflictReturnsTrue(self):
        # x o o
        # o o o     
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 1)

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
