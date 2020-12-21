"""
Check methods (for user input grid)
"""


def check_size(grid):
    """
    Checks if grid is 9x9.
    """
    row_count = 0
    col_count = 0

    for row in grid:
        row_count += 1
        for col in grid[row]:
            col_count += 1
        if col_count != 9:
            return False
        else:
            col_count = 0

    if row_count != 9:
        return False

    return True


def check_full(grid):
    """
    Checks if grid is filled.
    """
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    return True


def check_valid(grid):
    """
    Checks if a completely filled grid is correct.
    """
    return False


"""
Solve methods
"""


def exist_row(grid, num, row):
    for col in range(0, 9):
        if grid[row][col] == num:
            return True
    return False


def exist_col(grid, num, col):
    for row in range(0, 9):
        if grid[row][col] == num:
            return True
    return False


def exist_group(grid, num, start_row, start_col):
    for row in range(0, 3):
        for col in range(0, 3):
            if grid[row + start_row][col + start_col] == num:
                return True
    return False


def exist_constraints(grid, num, row, col):
    if row % 3 == 1:
        start_row = row - 1
    elif row % 3 == 2:
        start_row = row - 2
    else:
        start_row = row

    if col % 3 == 1:
        start_col = col - 1
    elif col % 3 == 2:
        start_col = col - 2
    else:
        start_col = col

    if exist_row(grid, num, row) == True:
        if exist_col(grid, num, col) == True:
            if exist_group(grid, num, start_row, start_col) == True:
                return True

    return False


def solve(grid):
    """
    Solves sudoku puzzle with a backtracking algorithm.
    Returns the completed grid.
    """
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if exist_constraints(grid, num, row, col) == False:
                        grid[row][col] == num

                        if solve(grid) == True:
                            return True

                        grid[row][col] == 0

    return False


def main():
    """A grid is basically an array of arrays."""

    grid = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]

    solve(grid)

    print(grid)


if __name__ == "__main__":
    main()
