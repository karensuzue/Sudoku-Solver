from methods import Puzzle

"""
Check methods (for user input grid)
CHANGE THIS INTO
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


def check_valid(grid):
    """
    Checks if a completely filled grid is correct.
    """
    return False


"""
Solve methods
"""


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

    solve_puzzle = Puzzle(grid)
    print("Check exist_constraints work")
    check = solve_puzzle.exist_constraints(5, 0, 2)
    print(check)
    check = solve_puzzle.exist_constraints(6, 0, 0)
    print(check)

    print("Check empty cell array")
    solve_puzzle.find_empty()
    print(solve_puzzle.empty_cells)

    solve_puzzle.print_grid()


if __name__ == "__main__":
    main()
