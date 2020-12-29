class Puzzle:
    def __init__(self, grid):
        self.grid = grid
        self.empty_cells = []

    def check_full(self):
        """
        Checks if grid is full.
        :return: True if full, otherwise False
        """
        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid[row][col] == 0:
                    return False
        return True

    def find_empty(self):
        """
        Finds the coordinates of unassigned cells.
        :return: dictionary of row and column coordinates of empty cells
        """
        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid[row][col] == 0:
                    coordinates = {'row': row, 'col': col}
                    self.empty_cells.append(coordinates)

    def exist_row(self, num, row):
        """
        Checks if number already exists in row.
        :param num: int to check
        :param row: row to check
        :return: True if exists, otherwise False
        """
        for col in range(0, 9):
            if self.grid[row][col] == num:
                return True
        return False

    def exist_col(self, num, col):
        """
        Checks if number already exists in column.
        :param num: int to check
        :param col: col to check
        :return: True if exists, otherwise False
        """
        for row in range(0, 9):
            if self.grid[row][col] == num:
                return True
        return False

    def exist_group(self, num, start_row, start_col):
        """
        Checks if number already exists in group (a 3x3 section of the grid).
        :param num: int to check
        :param start_row: starting row of group
        :param start_col: starting row of column
        :return: True if exists, otherwise False
        """
        for row in range(0, 3):
            for col in range(0, 3):
                if self.grid[row + start_row][col + start_col] == num:
                    return True
        return False

    def exist_constraints(self, num, row, col):
        """
        Checks number against all the constraints above.
        :param num: int to check
        :param row: row to check
        :param col: col to check
        :return: True if exists in row, column, or group, otherwise False
        """
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

        if self.exist_row(num, row) == True:
            return True
        if self.exist_col(num, col) == True:
            return True
        if self.exist_group(num, start_row, start_col) == True:
            return True

        return False

    def solve(self, iterator):
        """
        Solves grid.
        :param iterator: an int, has to be with 0
        :return: solved grid
        """
        if self.check_full() == True:
            return True

        else:
            cur_row = self.empty_cells[iterator]['row']
            cur_col = self.empty_cells[iterator]['col']
            for num in range(1, 10):
                if self.exist_constraints(num, cur_row, cur_col) == False:
                    self.grid[cur_row][cur_col] = num
                    iterator += 1
                    if self.solve(iterator) == True:
                        return True
                    self.grid[cur_row][cur_col] = 0
                    iterator -= 1

            return False

    def print_grid(self):
        """
        Pretty printing.
        :return: a better-looking grid
        """
        self.solve(0)
        for row in range(0, 9):
            if row % 3 == 0 and row != 0:
                print("-------------------------")

            for col in range (0, 9):
                if col % 3 == 0:
                    print("|", end=' ')
                if col == 8:
                    print(self.grid[row][col], end=' ')
                    print("|", end='\n')
                else:
                    print(self.grid[row][col], end=' ')

        print('\n')

