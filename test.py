from methods import Puzzle

def check_size(grid):
    """
    Checks if user input grid is 9x9.
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


def main():
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

    grid2 = [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ]

    grid3 = [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
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

    solve_puzzle2 = Puzzle(grid2)
    solve_puzzle2.find_empty()
    solve_puzzle2.print_grid()

    solve_puzzle3 = Puzzle(grid3)
    solve_puzzle3.find_empty()
    solve_puzzle3.print_grid()


if __name__ == "__main__":
    main()
