import pygame


class Grid:
    def __init__(self, cell_array, screen, grid_size):
        self.grid = [[0 for col in range(0, 9)] for row in range(0, 9)]
        self.empty_cells = []
        self.cell_array = cell_array
        self.iterator = 0

        self.grid_size = grid_size
        self.cell_size = self.grid_size / 9

        self.screen = screen
        self.border_color = (0, 0, 0)

    def convert_grid(self):
        """
        Take values of each cell from cell_array and place them into the grid
        array.
        :return: a complete grid array
        """
        for row in range(0, 9):
            for col in range(0, 9):
                self.grid[row][col] = self.cell_array[row][col].num

    def convert_cell(self):
        """
        Place values from grid array back into cell array.
        :return: updated cell array
        """
        for row in range(0, 9):
            for col in range(0, 9):
                cell = self.cell_array[row][col]
                cell.num = self.grid[row][col]
                cell.text = str(cell.num)
                cell.active = False
                cell.txt_area = cell.font.render(cell.text, True, (0, 0, 0))

    def draw_grid_lines(self):
        """
        Draw the lines of the grid on the screen.
        :return: grid lines drawn
        """
        for i in range(0, 10):
            if i % 3 == 0:
                thick = 5
            else:
                thick = 1

            pygame.draw.line(self.screen, self.border_color,
                             (0, i * self.cell_size),
                             (self.grid_size, i * self.cell_size), thick)
            pygame.draw.line(self.screen, self.border_color,
                             (i * self.cell_size, 0),
                             (i * self.cell_size, self.grid_size), thick)

    def draw_cells(self):
        """
        Draw each cell in the grid.
        :return: all cells drawn
        """
        for row in range(0, 9):
            for col in range(0, 9):
                self.cell_array[row][col].draw_cell()

    def reset(self):
        """
        Remove all numbers in the grid.
        :return: empty grid
        """
        for row in range(0, 9):
            for col in range(0, 9):
                cell = self.cell_array[row][col]
                cell.num = 0
                cell.text = ''
                cell.active = False
                cell.txt_area = cell.font.render(cell.text, True, (0, 0, 0))

        for row in range(0, 9):
            for col in range(0, 9):
                self.grid[row][col] = 0

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


class Cell:
    def __init__(self, row, col, size, screen):
        self.screen = screen

        self.num = 0
        self.text = ''
        self.font = pygame.font.Font(None, 40)
        self.txt_area = self.font.render(self.text, True, (0, 0, 0))

        self.row = row
        self.col = col
        self.x = self.col * size
        self.y = self.row * size

        self.width = size
        self.height = size

        self.active = False

        self.color_active = (173, 216, 230)
        self.color_inactive = (255, 255, 255)
        self.color = self.color_inactive

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_cell(self):
        """
        Draw the cell on the screen. Blit value if not equal to 0.
        :return: cell drawn, with text if value is 1-9
        """
        # Draw the box
        pygame.draw.rect(self.screen, self.color, self.rect)
        # Blit the text/number onto the text surface
        if self.num != 0:
            self.screen.blit(self.txt_area, (self.rect.x + 18, self.rect.y + 13))

    def cell_event(self, event):
        """
        Handle the cell-related events.
        :param event: event
        :return: event handled
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            if self.active == True:
                self.color = self.color_active
            else:
                self.color = self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active == True:
                if event.key == pygame.K_BACKSPACE:
                    self.text = ''
                    self.num = 0
                if event.key == pygame.K_0:
                    self.text = ''
                    self.num = 0
                if event.key == pygame.K_1:
                    self.text = '1'
                    self.num = 1
                if event.key == pygame.K_2:
                    self.text = '2'
                    self.num = 2
                if event.key == pygame.K_3:
                    self.text = '3'
                    self.num = 3
                if event.key == pygame.K_4:
                    self.text = '4'
                    self.num = 4
                if event.key == pygame.K_5:
                    self.text = '5'
                    self.num = 5
                if event.key == pygame.K_6:
                    self.text = '6'
                    self.num = 6
                if event.key == pygame.K_7:
                    self.text = '7'
                    self.num = 7
                if event.key == pygame.K_8:
                    self.text = '8'
                    self.num = 8
                if event.key == pygame.K_9:
                    self.text = '9'
                    self.num = 9
            # re-render
            self.txt_area = self.font.render(self.text, True, (0, 0, 0))








