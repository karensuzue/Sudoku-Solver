import pygame
from GUI_methods import Cell
from GUI_methods import Grid

GRID_SIZE = 450
CELL_SIZE = GRID_SIZE / 9
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

    #2 dimensional cell class obj array here
    #grid object with the cell array arg here
    #also button rect creation here


    #inside while loop, handle the event, after the event draw (before display flip)
    #then click on solve button, which triggers the convert function, then
# solve() function of the grid, then the other convert function
    #


def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE, GRID_SIZE + 60))
    pygame.display.set_caption("Sudoku Solver")

    #Create the solve button
    s_button = pygame.Rect(GRID_SIZE - 92, GRID_SIZE + 17, 80, 30)
    #Create the reset button
    r_button = pygame.Rect(12, GRID_SIZE + 17, 80, 30)

    cell_array = []
    for row in range(0, 9):
        arr = []
        for col in range(0, 9):
            arr.append(Cell(row, col, CELL_SIZE, screen))
        cell_array.append(arr)

    grid_obj = Grid(cell_array, screen)

    close = False
    while close == False:
        for event in pygame.event.get():
            #Quit button event
            if event.type == pygame.QUIT:
                close = True

            #Handle cell events
            for row in range(0, 9):
                for col in range(0, 9):
                    cell_array[row][col].cell_event(event)

            # Solve button event
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if s_button.collidepoint(mouse_pos):
                    print("pressed at {0}".format(mouse_pos))

        #Fill screen
        screen.fill((255, 255, 255))

        #Blit buttons on screen
        pygame.draw.rect(screen, (0, 128, 0), s_button)
        pygame.draw.rect(screen, (240, 0, 0), r_button)
        #Blit button text
        s_text = "Solve"
        r_text = "Reset"
        font = pygame.font.Font(None, 20)
        s_surface = font.render(s_text, True, (255, 255, 255))
        r_surface = font.render(r_text, True, (255, 255, 255))
        screen.blit(s_surface, (GRID_SIZE - 69, GRID_SIZE + 25))
        screen.blit(r_surface, (35, GRID_SIZE + 25))

        #Blit cells on screen
        for row in range(0, 9):
            for col in range(0, 9):
                cell_array[row][col].draw_cell()

        #Blit grid lines
        grid_obj.draw_grid_lines()
        pygame.display.update()


if __name__ == "__main__":
    main()




