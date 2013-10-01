class RecursiveBacktracking(object):
    """Solving the N-Queens problem using a recursive backtracking algorithm."""
    def can_place_queen(self, board, row, col):
        result = False

        # check for exact space conflict

        # check for row conflict
        # check for col conflict
        # check for diagonal conflict

        return result

    def solve(self, numQueens, board):
        result = False

        if (numQueens == 0):
            # solved
            return True 

        # try to place a queen considering every spot on the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                # queen can be placed at row,col?
                canPlace = self.can_place_queen(board, row, col)

                if (canPlace):
                    # update the board w/ the queen's placement
                    board[row][col] = 1
                    # recurse w/ one less queen
                    result = self.solve(numQueens - 1, board)

                    if (result):
                        # we're done
                        break;
                else:
                    # stop processing this board
                    pass

        return False