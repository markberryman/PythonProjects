import recursiveBacktracking
import unittest

class CanPlaceQueenTests(unittest.TestCase):
    def test_RowConflictReturnsFalse(self):
        # x ? o
        # o o o
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0], [1,0,0], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 1, 3)

        self.assertFalse(actual)

    def test_RowConflictToTheLeftReturnsFalse(self):
        # ? x o
        # o o o
        # o o o
        board = [[0,0,1], [0,0,0], [0,0,0], [1,0,0], [0,1,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 0, 3)

        self.assertFalse(actual)

    def test_ColConflictDirectlyAboveReturnsFalse(self):
        # x o o
        # ? o o       
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0], [1,0,0], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 1, 0, 3)

        self.assertFalse(actual)

    def test_ColConflictNotDirectlyAboveReturnsFalse(self):
        # x o o
        # o o o       
        # ? o o
        board = [[1,0,0], [0,0,0], [0,0,0], [1,0,0], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 0, 3)

        self.assertFalse(actual)

    def test_DiagConflictDownAndRightReturnsFalse(self):
        # ? o o
        # o o o     
        # o o x
        board = [[0,0,0], [0,0,0], [0,0,1], [0,0,1], [0,0,1]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 0, 3)

        self.assertFalse(actual)

    def test_DiagConflictUpAndLeftReturnsFalse(self):
        # x o o
        # o o o
        # o o ?
        board = [[1,0,0], [0,0,0], [0,0,0], [1,0,0], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 2, 3)

        self.assertFalse(actual)

    def test_DiagConflictUpAndRightReturnsFalse(self):
        # o o x
        # o o o
        # ? o o
        board = [[0,0,1], [0,0,0], [0,0,0], [1,0,0], [0,0,1]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 0, 3)

        self.assertFalse(actual)

    def test_DiagConflictDownAndLeftReturnsFalse(self):
        # o o ?
        # o o o     
        # x o o
        board = [[0,0,0], [0,0,0], [1,0,0], [0,0,1], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 2, 3)

        self.assertFalse(actual)

    def test_ExactSpaceConflictReturnsFalse(self):
        # x o o
        # o o o     
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0], [1,0,0], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 0, 0, 3)

        self.assertFalse(actual)

    def test_NoConflictReturnsTrue(self):
        # x o o
        # o o o     
        # o o o
        board = [[1,0,0], [0,0,0], [0,0,0], [1,0,0], [1,0,0]]
        sut = recursiveBacktracking.RecursiveBacktracking()

        actual = sut.can_place_queen(board, 2, 1, 3)

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
