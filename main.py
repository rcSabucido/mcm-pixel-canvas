import pygame
from pygame.locals import *

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


number_of_rows = 50
number_of_columns = 50
grid = [[0 for x in range(number_of_rows)] for y in range(number_of_columns)]

basic_x = SCREEN_WIDTH / number_of_columns
basic_y = SCREEN_HEIGHT / number_of_rows


running = True

clicking = 0

screen.fill((255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN or clicking:
            clicking = 1
            x, y = pygame.mouse.get_pos()
            x_in_grid = int(x / basic_x)
            y_in_grid = int(y/ basic_y)
            grid[y_in_grid][x_in_grid] = 1
            pygame.draw.rect(screen, (0, 0, 0), (x_in_grid * basic_x,
                                                 y_in_grid * basic_y, basic_x,
                                                 basic_y))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            clicking = 0