import pygame
from random import *


def check_neighbours(x, y, grid, r, c):
    count = 0
    if 0 < x < r - 1 and 0 < y < c - 1:
        if grid[x - 1][y] == 1:
            count += 1
        if grid[x][y - 1] == 1:
            count += 1
        if grid[x + 1][y] == 1:
            count += 1
        if grid[x][y + 1] == 1:
            count += 1
        if grid[x - 1][y - 1] == 1:
            count += 1
        if grid[x - 1][y + 1] == 1:
            count += 1
        if grid[x + 1][y - 1] == 1:
            count += 1
        if grid[x + 1][y + 1] == 1:
            count += 1
    return count


def game():
    # Define some colors
    Black = (0, 0, 0)
    White = (225, 225, 225)
    Red = (255, 0, 0)
    quit_color1 = Black
    quit_color2 = Black
    quit_color3 = Black
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 5
    HEIGHT = 5

    # This sets the margin between each cell
    MARGIN = 1

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    # Append a cell
    grid = []
    r = 60
    c = 60
    for row in range(r):
        grid.append([])
        for column in range(c):
            grid[row].append(randint(0, 1))

    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    Window_Size = [400, 460]
    screen = pygame.display.set_mode(Window_Size)
    # Set title of screen
    pygame.display.set_caption("Sunny game")
    background_image = pygame.image.load("game_stop.jfif").convert()
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    fps = 40
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 360 and 0 < pos[1] < 180:
                    quit_color1 = White
                else:
                    quit_color1 = Black
                if pos[0] > 360 and 360 > pos[1] > 180:
                    quit_color2 = White
                else:
                    quit_color2 = Black
                # if pos[0] > 360 and 200 > pos[1] > 160:
                #     quit_color3 = White
                # else:
                #     quit_color3 = Black
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound = pygame.mixer.Sound("laser5.ogg")
                click_sound.play()
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if pos[1] <= 360 and pos[0] <= 360:
                    # Set that location to one
                    grid[row][column] = 1
                if pos[1] > 360:
                    done = True
                    pygame.quit()
                if pos[0] > 360 and pos[1] <= 180:
                    fps += 5
                    if fps >= 80:
                        fps = 80
                    print("fps", fps)
                if pos[0] > 360 and pos[1] > 180:
                    fps -= 5
                    if fps <= 5:
                        fps = 5
                    print("fps",  fps)
                # if pos[0] > 360 and 160 <= pos[1] <= 200:
                #     pygame.quit()
                #     game()
                print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill(Black)
        pygame.draw.rect(screen, quit_color1, [360, 0, 40, 180])
        # pygame.draw.rect(screen, quit_color3, [360, 160, 40, 40])
        pygame.draw.rect(screen, quit_color2, [360, 181, 40, 180])
        screen.blit(background_image, [0, 360])
        # Draw the grid
        B = []
        W = []

        for row in range(r):
            for column in range(c):
                color = Black
                no_of_neighbours = check_neighbours(row, column, grid, r, c)
                if grid[row][column] == 1 and no_of_neighbours < 2:
                    color = Black
                    B.append([row, column])
                if grid[row][column] == 1 and (no_of_neighbours == 2 or no_of_neighbours == 3):
                    color = White
                    W.append([row, column])
                if grid[row][column] == 1 and no_of_neighbours >= 4:
                    color = Black
                    B.append([row, column])
                if grid[row][column] == 0 and no_of_neighbours == 3:
                    color = White
                    W.append([row, column])
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        for i in B:
            grid[i[0]][i[1]] = 0
        for i in W:
            grid[i[0]][i[1]] = 1

        # Limit to 60 frames per second
        clock.tick(fps)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


game()
