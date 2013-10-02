import recursiveBacktracking
import time

rbt = recursiveBacktracking.RecursiveBacktracking()
boardDimension = 8
board = [[0 for x in range(boardDimension)] for x in range(boardDimension)]

startTime = time.clock()

result = rbt.solve(8, board)

if (result is False):
    print("No solution")

print("\nNumber of calculations = {:,}".format(rbt.numCalcs))

print("\nTime taken (seconds): " + str(time.clock() - startTime))

#input("Done")
