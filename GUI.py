import pygame
from methods import Puzzle
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

def user_input(pos_dict):
    """
    Places user input values into a dictionary.
    :param pos_dict:
    :return:
    """
    pass
#probbaly gonna have to do a class for the cubes, have them each store their xy coordinate, row and column coordinates,  and value
#should also contain drawing functions maybe
#you could have an array of Cube type objects
#set it all to whatever coordinates it has, but w n = 0
#thats like 1-81 cube objects
#or [[x9]x9] so just like the grid you've been using but replce it with cube objects, that way even the row and col are the same
def form_grid(pos_dict):
    """
    Places values collected in a dictionary into the grid array.
    :param pos_dict:
    :return:
    """
    grid = [9]
    for cell in pos_dict:
        row = cell['row']
        col = cell['col']
        grid[row][col] = cell['n']
    return grid


def main():
    # Create the screen
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE, GRID_SIZE + 100))
    pygame.display.set_caption("Sudoku Solver")

    #Create the solve button
    button = pygame.Rect(0, 450, 450, 100)

    #Position and value of each cell (n, x, y, row, col)
    cell_pos = {}



    close = False
    while close == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        screen.fill(WHITE)
        draw_grid(screen)

        #Clicking the solve button
        pygame.draw.rect(screen, (0, 128, 0), button)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                print("pressed at {0}".format(mouse_pos))

        pygame.display.update()


if __name__ == "__main__":
    main()




