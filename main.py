import pygame
import sys
import pygame_gui
from pygame.locals import *

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MANAGER = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), 'json_files/theme.json')
MANAGER.get_theme().load_theme('json_files/label_theme.json')

user_text = ""

def menu():
    global user_text
    menu_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((250, 200), (300, 200)), text= "", manager=MANAGER)                                     
    menu_label.set_text("ENTER DESIRED GRID DIMENSION")
                                                                           
    CLOCK = pygame.time.Clock()
    TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 350),
                                                                           (200, 50)), manager=MANAGER,
                                                                           object_id="#main_text_entry")
    
    
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
        
        screen.fill("#3D405B")

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

    colors = "#000000"
    
    def erase_screen(screen, grid, basic_x, basic_y):
        for i in range(number_of_columns):
            for j in range(number_of_rows):
                if grid[i][j]:
                    pygame.draw.rect(screen, (255, 255, 255), (j * basic_x,
                                                         i * basic_y, basic_x, basic_y))
                    
    def change_color(screen, color, x_cell, y_cell, x_pos, y_pos):
        pygame.draw.rect(screen, color, (x_cell * x_pos, y_cell * y_pos, x_pos,
                                         y_pos))
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_e:
                    erase_screen(screen, grid, basic_x, basic_y)
                    pygame.display.flip()
                if event.key == K_r:
                    colors = "#E07A5F"
                if event.key == K_g:
                    colors = "#81B29A"
                if event.key == K_b:
                    colors = "#3D405B"
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
                change_color(screen, colors, x_in_grid, y_in_grid, basic_x, basic_y)        
                
                pygame.display.flip()                
            if event.type == pygame.MOUSEBUTTONUP:
                clicking = 0

            

menu()
