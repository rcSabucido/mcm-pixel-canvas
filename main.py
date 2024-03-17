import pygame
import sys
import pygame_gui
from pygame.locals import *

pygame.init()

# Dimension of pygame window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PixelCanvas")

MANAGER = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), 'json_files/theme.json')
MANAGER.get_theme().load_theme('json_files/label_theme.json')

user_text = ""

def menu():
    global user_text
    menu_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((250, 200), (300, 200)), text="", manager=MANAGER)                                     
    menu_label.set_text("ENTER DESIRED GRID DIMENSION")
    menu_label.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
    control_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((350, 360), (100, 100)), text="", manager=MANAGER)
    control_label.set_text("CONTROLS:")
    e_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((300, 390), (200, 100)), text="E = ERASE CANVAS", manager=MANAGER)
    r_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((314, 410), (100, 100)), text="R = RED", manager=MANAGER)
    g_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((322, 430), (100, 100)), text="G = GREEN", manager=MANAGER)
    b_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((318, 450), (100, 100)), text="B = BLUE", manager=MANAGER)
    v_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((322, 470), (100, 100)), text="V = BLACK", manager=MANAGER)
    c_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((326, 490), (100, 100)), text="C = ERASER", manager=MANAGER)
    esc_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((254, 510), (300, 100)), text="ESC = QUIT CANVAS", manager=MANAGER)

    control_list = [control_label, e_label, r_label, g_label, b_label, v_label, c_label, esc_label]
    for ctr in control_list:
        ctr.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)

                                                                           
    CLOCK = pygame.time.Clock()
    TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 340),
                                                                           (200, 50)), manager=MANAGER,
                                                                           object_id="#main_text_entry")
    
    
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60)/1000
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                user_text = TEXT_INPUT.get_text()
                create_canvas(user_text)

                
                
            MANAGER.process_events(event)
        
        MANAGER.update(UI_REFRESH_RATE)
        
        screen.fill("#3D405B")

        MANAGER.draw_ui(screen)

        pygame.display.update()


def create_canvas(dimension):
    # specifies the grid dimension of the canvas
    number_of_rows = int(dimension)
    number_of_columns = int(dimension)
    # creates an x/y array of 0 values based on the number of rows and columns
    # this sets the dead cells for activation when user wants to erase canvas
    grid = [[0 for x in range(number_of_rows)] for y in range(number_of_columns)]

    # calculates the specific dimensions of the individual cells
    basic_x = SCREEN_WIDTH / number_of_columns
    basic_y = SCREEN_HEIGHT / number_of_rows

    running = True

    clicking = 0

    screen.fill((255, 255, 255))

    colors = "#000000"
    

    def erase_canvas(screen, grid, basic_x, basic_y):
        for i in range(number_of_columns):
            for j in range(number_of_rows):
                if grid[i][j]:
                    pygame.draw.rect(screen, (255, 255, 255), (j * basic_x,
                                                         i * basic_y, basic_x, basic_y))


    def change_color(screen, color, x_in_cell, y_in_cell, x_size, y_size):
        # x_in_cell * x_size gives pixel position of left edge of cell
        # y_in_cell * y_size gives pixel position of top edge of cell
        pygame.draw.rect(screen, color, (x_in_cell * x_size, y_in_cell * y_size, x_size,
                                         y_size))
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_e:
                    erase_canvas(screen, grid, basic_x, basic_y)
                    pygame.display.flip()
                if event.key == K_r:
                    colors = "#93032E"
                if event.key == K_g:
                    colors = "#50C878"
                if event.key == K_b:
                    colors = "#59A5D8"
                if event.key == K_v:
                    colors = "#000000"
                if event.key == K_c:
                    colors = "#FFFFFF"
            elif event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or clicking:
                clicking = 1
                x, y = pygame.mouse.get_pos()
                x_in_grid = int(x / basic_x)
                y_in_grid = int(y/ basic_y)

                # turns the 0's on the grid array to 1's to specify which cells are alive
                grid[y_in_grid][x_in_grid] = 1

                change_color(screen, colors, x_in_grid, y_in_grid, basic_x, basic_y)        
                
                pygame.display.flip()                
            if event.type == pygame.MOUSEBUTTONUP:
                clicking = 0

            
menu()
