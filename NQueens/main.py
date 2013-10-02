import recursiveBacktracking

rbt = recursiveBacktracking.RecursiveBacktracking()
boardDimension = 8
board = [[0 for x in range(boardDimension)] for x in range(boardDimension)]
result = rbt.solve(6, board)

if (result):
    print()
    print("Solution:")
    rbt.print(board)
else:
    print("No solution")

input("Done")
