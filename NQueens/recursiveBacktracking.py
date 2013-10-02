import copy


class RecursiveBacktracking(object):
    """Solving the N-Queens problem using a recursive backtracking algorithm."""
    def __init__(self):
        self.numCalcs = 0

    def print(self, board):
        for x in range(len(board)):
            print(board[x])

    def can_place_queen(self, board, row, col):
        self.numCalcs += 1

        # check for exact space conflict
        if (board[row][col] == 1):
            #print("Exact space conflict.")
            return False

        # check for row conflict
        rowToCheck = board[row]
        for i in rowToCheck:
            if (i == 1):
                #print("Row conflict.")
                return False

        # check for col conflict
        for i in range(len(board)):
            if (board[i][col] == 1):
                #print("Column conflict.")
                return False

        # check for diagonal conflict
        # check up and left
        rowIdxToCheck = row - 1
        colIdxToCheck = col - 1

        while ((rowIdxToCheck >= 0) and (colIdxToCheck >= 0)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (UL).")
                return False
            else:
                rowIdxToCheck -= 1
                colIdxToCheck -= 1

        # check up and right
        rowIdxToCheck = row - 1
        colIdxToCheck = col + 1

        while ((rowIdxToCheck >= 0) and (colIdxToCheck < len(board[0]))):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (UR).")
                return False
            else:
                rowIdxToCheck -= 1
                colIdxToCheck += 1

        # check down and right
        rowIdxToCheck = row + 1
        colIdxToCheck = col + 1

        while ((rowIdxToCheck < len(board)) and (colIdxToCheck < len(board[0]))):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (DR).")
                return False
            else:
                rowIdxToCheck += 1
                colIdxToCheck += 1

         # check down and left
        rowIdxToCheck = row + 1
        colIdxToCheck = col - 1

        while ((rowIdxToCheck < len(board)) and (colIdxToCheck >= 0)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (DL).")
                return False
            else:
                rowIdxToCheck += 1
                colIdxToCheck -= 1

        return True

    def solve(self, numQueens, board):
        if (numQueens == 0):
            # solved
            print("\nSolution:")
            self.print(board)
            return True

        # try to place a queen considering every spot on the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                # queen can be placed at row,col?
                #print("Considering [{},{}]".format(row, col))
                canPlace = self.can_place_queen(board, row, col)

                if (canPlace):
                    #print("Placing queen at [{},{}]. {} to go.".format(row, col, numQueens - 1))

                    # need to copy the board so we don't have separate
                    # solution investigations stomp on each other
                    newBoard = copy.deepcopy(board)
                    # update the board w/ the queen's placement
                    newBoard[row][col] = 1

                    #self.print(newBoard)

                    # recurse w/ one less queen
                    result = self.solve(numQueens - 1, newBoard)

                    if (result):
                        # we're done; no need trying to place queens
                        return result
                # else: continue trying to place this queen

        # couldn't place this queen
        #print("Backtracking...")
        return False