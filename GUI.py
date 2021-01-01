import pygame
from GUI_methods import Cell
from GUI_methods import Grid

GRID_SIZE = 450
CELL_SIZE = GRID_SIZE / 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_grid(screen):
    for i in range(0, 10):
        if i % 3 == 0:
            line = 5
        else:
            line = 1

        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (GRID_SIZE, i * CELL_SIZE), line)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_SIZE), line)

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE, GRID_SIZE + 60))
    pygame.display.set_caption("Sudoku Solver")

    #2 dimensional cell class obj array here
    #grid object with the cell array arg here
    #also button rect creation here


    #inside while loop, handle the event, after the event draw (before display flip)
    #then click on solve button, which triggers the convert function, then
# solve() function of the grid, then the other convert function
    #


    #new = Cell(2, 5, CELL_SIZE, screen)
    cell_array = [[Cell(row, col, CELL_SIZE, screen) for col in range(0, 9)] for row in range(0, 9)]
    grid = Grid(cell_array, screen)

    close = False
    while close == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            #new.cell_event(event)
            for row in range(0, 9):
                for col in range(0, 9):
                    cell_array[row][col].cell_event(event)

        screen.fill((255, 255, 255))
        #new.draw_cell()
        for row in range(0, 9):
            for col in range(0 ,9):
                cell_array[row][col].draw_cell()

        #draw_grid(screen)
        grid.draw_grid_lines()
        pygame.display.update()

    for i in range(0, 9):
        print(cell_array[0][i].num)


if __name__ == "__main__":
    main()




