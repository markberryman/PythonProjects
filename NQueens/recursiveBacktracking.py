class RecursiveBacktracking(object):
    """Solving the N-Queens problem using a recursive backtracking algorithm."""
    def print(self, board):
        for x in range(len(board)):
            print(board[x])

    def can_place_queen(self, board, row, col):
        # check for exact space conflict
        if (board[row][col] == 1):
            return False

        # check for row conflict
        rowToCheck = board[row]
        for i in rowToCheck:
            if (i == 1):
                return False

        # check for col conflict
        for i in range(len(board)):
            if (board[i][col] == 1):
                return False

        # check for diagonal conflict
        # check up and left
        rowIdxToCheck = row - 1
        colIdxToCheck = col - 1

        while ((rowIdxToCheck >= 0) and (colIdxToCheck >= 0)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                return False
            else:
                rowIdxToCheck -= 1
                colIdxToCheck -= 1

        # check up and right
        rowIdxToCheck = row - 1
        colIdxToCheck = col + 1

        while ((rowIdxToCheck >= 0) and (colIdxToCheck < len(board[0]))):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                return False
            else:
                rowIdxToCheck -= 1
                colIdxToCheck += 1

        # check down and right
        rowIdxToCheck = row + 1
        colIdxToCheck = col + 1

        while ((rowIdxToCheck < len(board)) and (colIdxToCheck < len(board[0]))):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                return False
            else:
                rowIdxToCheck += 1
                colIdxToCheck += 1

         # check down and left
        rowIdxToCheck = row + 1
        colIdxToCheck = col - 1

        while ((rowIdxToCheck < len(board)) and (colIdxToCheck >= 0)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                return False
            else:
                rowIdxToCheck += 1
                colIdxToCheck -= 1

        return True

    def solve(self, numQueens, board):
        if (numQueens == 0):
            # solved
            return True 

        # try to place a queen considering every spot on the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                # queen can be placed at row,col?
                print("Considering [{},{}]".format(row, col))
                canPlace = self.can_place_queen(board, row, col)

                if (canPlace):
                    print("Placing queen at [{},{}]".format(row, col))
                    # update the board w/ the queen's placement
                    board[row][col] = 1

                    self.print(board)

                    # recurse w/ one less queen
                    result = self.solve(numQueens - 1, board)

                    if (result):
                        # we're done; no need trying to place queens
                        return result
                # else: continue trying to place this queen

        # couldn't place this queen
        return False