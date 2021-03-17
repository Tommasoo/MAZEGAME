import pygame, sys
from pygame.locals import *
from table import  table_obj

pygame.init()

#settings
settings_file = open("settings.txt", "r")

def get_new_word(file):
    temp = file.readline()
    temp = [int(i) for i in temp.split() if i.isdigit()]
    return temp[0]

#colori
white = (255, 255, 255)
red = (255, 0, 0)
green = (125, 255, 125)
black = (0, 0, 0)
grey = (225, 225, 225)
blue = (125, 125, 255)


#window setup
surf_width = get_new_word(settings_file) #window width
surf_height = get_new_word(settings_file) #window height

display_surf = pygame.display.set_mode((surf_width, surf_height))
pygame.display.set_caption('path') #titolo finestra
display_surf.fill(white)

fps = 20


#button setup
button_width = surf_width // 4
button_height = surf_height // 10

button_line_width = 6
button_hoover_color = grey

mini_button_side = surf_width // 30
button_height_offset = surf_height // 10


#start button
start_button_rect = (surf_width // 2 - button_width // 2, surf_height // 2 - button_height_offset, button_width, button_height)
start_button_text = 'START'


#options
#options button
options_button_rect = (surf_width // 2 - button_width // 2, surf_height // 2 + button_height_offset, button_width, button_height)
options_button_text = 'OPTIONS'

#options menu button
options_menu_button_rect = (surf_width // 2 - button_width // 2, surf_height // 2 + 3 * button_height_offset, button_width, button_height)
options_menu_button_text = 'MENU'
options_buttons_width_offset = surf_width // 4
options_buttons_height_offset = surf_height // 8
options_text_font_size = surf_width // 40

#options menu font
options_font = pygame.font.SysFont('arial', options_text_font_size, bold = False)


#breadth first search options
breadth_first_search_text = 'BREADTH FIRST SEARCH: '
breadth_first_search_text_obj = options_font.render(breadth_first_search_text, True, black)
breadth_first_search_text_width, breadth_first_search_text_height = options_font.size(breadth_first_search_text)

mini_button_text_offset = (mini_button_side - breadth_first_search_text_height) // 2
breadth_first_search_button_rect = (surf_width - options_buttons_width_offset - mini_button_side, options_buttons_height_offset - mini_button_text_offset, mini_button_side, mini_button_side)


#breadth first search options
depth_first_search_text = 'DEPTH FIRST SEARCH: '
depth_first_search_text_obj = options_font.render(depth_first_search_text, True, black)
depth_first_search_button_rect = (surf_width - options_buttons_width_offset - mini_button_side, (options_buttons_height_offset  * 2 ) - mini_button_text_offset, mini_button_side, mini_button_side)


#quit button
quit_button_rect = (surf_width // 2 - button_width // 2, surf_height // 2 + 3 * button_height_offset, button_width, button_height)
quit_button_text = 'QUIT'


#maze logo start screen
maze_logo_text = 'MAZE GENERATOR'
font_size = surf_height // 10
maze_logo_font = pygame.font.SysFont('arial', font_size, bold=True)  # font
maze_text = maze_logo_font.render(maze_logo_text, True, black)  #testo
maze_text_width, maze_text_height = maze_logo_font.size(maze_logo_text)
maze_logo_x = (surf_width - maze_text_width) // 2
maze_logo_y = surf_height // 6


#side window game
side_window = surf_width // 4 #lateral window for menu bar
sidebar_button_width = side_window - side_window // 4
sidebar_button_height = sidebar_button_width // 4
#sidebar_height_offset = surface_height // 2 * 2 #(n buttons)

sidebar_menu_button_rect = (surf_width - sidebar_button_width - side_window // 8, surf_height - button_height_offset * 2, sidebar_button_width, sidebar_button_height)
sidebar_menu_button_text = 'MENU'

sidebar_solve_button_rect = (surf_width - sidebar_button_width - side_window // 8, button_height_offset, sidebar_button_width, sidebar_button_height)
sidebar_solve_button_text = 'SOLVE'


#table setup
cell_number_width = get_new_word(settings_file) #cell number
cell_side = (surf_width - side_window) // cell_number_width #lenght of the side of the cell
cell_number_height = surf_height // cell_side #mumber of cells on the y axis
cell_border_width = get_new_word(settings_file) #width of the border of the cell


#maze setup
table = table_obj(cell_number_width, cell_number_height, cell_side, display_surf, cell_border_width)
stack = []
maze_colour = (255, 120, 120)


#breadth first search variables
distances = [0] * (cell_number_width * cell_number_height)
breadth_first_search_bool = 0


#depth first search variables
done_search = False
depth_first_search_bool = not breadth_first_search_bool


#game bools
limit_CPU = True

setup_game = False
run_game_bool = False

sidebar_bool = False

options_tab = False

maze_done = False

solve_bool = False

start_screen_bool = True

allow_start_search = False
search = False

draw_path = False

