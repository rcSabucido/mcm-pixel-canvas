import pygame
import sys
import pygame_gui
from pygame.locals import *

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 100),
                                                                           (500, 50)), manager=MANAGER,
                                                                           object_id="#main_text_entry")
                                                 
user_text = ""

def menu():
    global user_text
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60)/1000
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                user_text = TEXT_INPUT.get_text()
                actual_canvas(user_text)

                
                
            MANAGER.process_events(event)
        
        MANAGER.update(UI_REFRESH_RATE)
        
        screen.fill("white")

        MANAGER.draw_ui(screen)

        pygame.display.update()


# specifies the grid dimension of the canvas

def actual_canvas(text):
    number_of_rows = int(text)
    number_of_columns = int(text)
    grid = [[0 for x in range(number_of_rows)] for y in range(number_of_columns)]

    # calculates the specific dimensions of the individual cells
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
            if event.type == pygame.MOUSEBUTTONDOWN or clicking:
                clicking = 1
                x, y = pygame.mouse.get_pos()
                x_in_grid = int(x / basic_x)
                y_in_grid = int(y/ basic_y)
                grid[y_in_grid][x_in_grid] = 1

                # x_in_grid * basic_x gives pixel position of left edge of cell
                # y_in_grid * basic_y gives pixel position of top edge of cell
                pygame.draw.rect(screen, (0, 0, 0), (x_in_grid * basic_x,
                                                    y_in_grid * basic_y, basic_x,
                                                    basic_y)) 
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONUP:
                clicking = 0

menu()
