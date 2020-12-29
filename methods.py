class Puzzle:
    def __init__(self, grid):
        self.grid = grid
        self.empty_cells = []

    def check_full(self):
        """
        Checks if grid is filled.
        """
        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid[row][col] == 0:
                    return False
        return True

    def find_empty(self):
        """
        Finds the coordinates of unassigned cells
        """
        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid[row][col] == 0:
                    coordinates = {'row': row, 'col': col}
                    self.empty_cells.append(coordinates)

    def exist_row(self, num, row):
        for col in range(0, 9):
            if self.grid[row][col] == num:
                return True
        return False

    def exist_col(self, num, col):
        for row in range(0, 9):
            if self.grid[row][col] == num:
                return True
        return False

    def exist_group(self, num, start_row, start_col):
        for row in range(0, 3):
            for col in range(0, 3):
                if self.grid[row + start_row][col + start_col] == num:
                    return True
        return False

    def exist_constraints(self, num, row, col):
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
        if self.check_full() == True:
            print("Grid is full.")
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
        self.solve(0)
        print(self.grid)
