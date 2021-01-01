from methods import Puzzle


def check_size(grid):
    """
    Checks if user input grid is 9x9.
    """
    row_count = 0
    col_count = 0

    for row in range(len(grid)):
        row_count += 1
        for col in range(len(grid[row])):
            col_count += 1
        if col_count != 9:
            return False
        else:
            col_count = 0

    if row_count != 9:
        return False

    return True


def main():
    print("This program solves 9x9 grid Sudoku puzzles.")
    print("You will be asked to enter 9 numbers at a time.")
    print("Enter 0 for empty cells, separate each cell with a space.")
    lst1 = [int(i) for i in input("Enter cell values for row 1: ").split()]
    lst2 = [int(i) for i in input("Enter cell values for row 2: ").split()]
    lst3 = [int(i) for i in input("Enter cell values for row 3: ").split()]
    lst4 = [int(i) for i in input("Enter cell values for row 4: ").split()]
    lst5 = [int(i) for i in input("Enter cell values for row 5: ").split()]
    lst6 = [int(i) for i in input("Enter cell values for row 6: ").split()]
    lst7 = [int(i) for i in input("Enter cell values for row 7: ").split()]
    lst8 = [int(i) for i in input("Enter cell values for row 8: ").split()]
    lst9 = [int(i) for i in input("Enter cell values for row 9: ").split()]

    grid = [lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9]
    if check_size(grid) == False:
        print("Grid is not 9x9.")

    else:
        solve = Puzzle(grid)
        solve.find_empty()
        solve.print_grid()


if __name__ == "__main__":
    main()
