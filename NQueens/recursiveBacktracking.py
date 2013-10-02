import copy


class RecursiveBacktracking(object):
    """Solving the N-Queens problem using a recursive backtracking algorithm."""
    def __init__(self):
        self.numCalcs = 0

    def print(self, board):
        # accounting for our two add'l rows of meta-data
        for x in range(len(board) - 2):
            print(board[x])

    def can_place_queen(self, board, row, col, boardDimension):
        self.numCalcs += 1

        # check for exact space conflict
        if (board[row][col] == 1):
            #print("Exact space conflict.")
            return False

        # check for row conflict
        rowMetaData = board[boardDimension]
        if (rowMetaData[row] == 1):
            return False

        # check for col conflict
        colMetaData = board[boardDimension + 1]
        if (colMetaData[col] == 1):
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

        while ((rowIdxToCheck >= 0) and (colIdxToCheck < boardDimension)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (UR).")
                return False
            else:
                rowIdxToCheck -= 1
                colIdxToCheck += 1

        # check down and right
        rowIdxToCheck = row + 1
        colIdxToCheck = col + 1

        while ((rowIdxToCheck < boardDimension) and (colIdxToCheck < boardDimension)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (DR).")
                return False
            else:
                rowIdxToCheck += 1
                colIdxToCheck += 1

         # check down and left
        rowIdxToCheck = row + 1
        colIdxToCheck = col - 1

        while ((rowIdxToCheck < boardDimension) and (colIdxToCheck >= 0)):
            if (board[rowIdxToCheck][colIdxToCheck] == 1):
                #print("Diagonal conflict (DL).")
                return False
            else:
                rowIdxToCheck += 1
                colIdxToCheck -= 1

        return True

    def solve(self, numQueens, board, boardDimension):
        if (numQueens == 0):
            # solved
            print("\nSolution:")
            self.print(board)
            return True

        # try to place a queen considering every spot on the board
        for row in range(boardDimension):
            for col in range(boardDimension):
                # queen can be placed at row,col?
                #print("Considering [{},{}]".format(row, col))
                canPlace = self.can_place_queen(board, row, col, boardDimension)

                if (canPlace):
                    #print("Placing queen at [{},{}]. {} to go.".format(row, col, numQueens - 1))

                    # need to copy the board so we don't have separate
                    # solution investigations stomp on each other
                    newBoard = copy.deepcopy(board)
                    # update the board w/ the queen's placement
                    newBoard[row][col] = 1
                    # update the board row meta-data
                    newBoard[boardDimension][row] = 1
                    # update the board column meta-data
                    newBoard[boardDimension + 1][col] = 1

                    #self.print(newBoard)

                    # recurse w/ one less queen
                    result = self.solve(numQueens - 1, newBoard, boardDimension)

                    if (result):
                        # we're done; no need trying to place queens
                        return result
                # else: continue trying to place this queen

        # couldn't place this queen
        #print("Backtracking...")
        return False