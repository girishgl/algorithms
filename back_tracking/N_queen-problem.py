# Python program to solve N Queen Problem using backtracking

# # A utility function to check if a queen can be placed on board[row][col]. Note that this
# # function is called when "col" queens are  already placed in columns from 0 to col -1.
# # So we need to check only left side for attacking queens


def is_safe(x, y):
    # Check this row on left side
    for column in range(y):
        if board[x][column] == 1:
            return False

    row = x - 1
    column = y - 1

    # Check upper diagonal on left side
    while row > -1 and column > -1:
        if board[row][column] == 1:
            return False
        row = row - 1
        column = column - 1

    # Check lower diagonal on left side
    row = x + 1
    column = y - 1

    while row < ROW and column > -1:
        if board[row][column] == 1:
            return False
        row = row + 1
        column = column - 1

    return True


def solve_n_queen(column):
    if column == COLUMN:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for row in range(ROW):
        if is_safe(row, column):
            board[row][column] = 1
            if solve_n_queen(column + 1):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution, then backtrack
            board[row][column] = 0
    return False


ROW = 6
COLUMN = 6

board = []
for i in range(ROW):
    board.append([0] * COLUMN)

print(board)

result = solve_n_queen(0)
print(board)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in board]))
