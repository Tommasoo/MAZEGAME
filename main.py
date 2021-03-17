import pygame
from pygame.locals import *
import random
from maze_builder import run_game
from buttons import button, mouse_on_button
from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search
from variables import *
import ctypes

#query DPI awareness
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))

#set DPI awareness
errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)

fps_clock = pygame.time.Clock
pygame.init()

while True:
    mouse = pygame.mouse.get_pos()

    if start_screen_bool:
        limit_CPU = True
        #start button hoover
        button(mouse, display_surf, button_hoover_color, start_button_rect, start_button_text)

        #options button hoover
        button(mouse, display_surf, button_hoover_color, options_button_rect, options_button_text)

        #quit button hoover
        button(mouse, display_surf, button_hoover_color, quit_button_rect, quit_button_text)

        #maze logo start screen text
        display_surf.blit(maze_text, (maze_logo_x, maze_logo_y))

    elif options_tab:
        limit_CPU = True
        #menu button
        button(mouse, display_surf, button_hoover_color, options_menu_button_rect, options_menu_button_text)

        #breadth first search button
        if breadth_first_search_bool:
            button(mouse, display_surf, black, breadth_first_search_button_rect, line_width = 8, button_colour = black)
        else:
            button(mouse, display_surf, button_hoover_color, breadth_first_search_button_rect, line_width = 8)
        #breadth first search text
        display_surf.blit(breadth_first_search_text_obj, (options_buttons_width_offset, options_buttons_height_offset))

        #depth first search button
        if depth_first_search_bool:
            button(mouse, display_surf, black, depth_first_search_button_rect, line_width = 8, button_colour = black)
        else:
            button(mouse, display_surf, button_hoover_color, depth_first_search_button_rect, line_width = 8)
        #depth first search text
        display_surf.blit(depth_first_search_text_obj, (options_buttons_width_offset, options_buttons_height_offset * 2))


    elif setup_game:
        setup_game = False

        starting_x = random.randint(0, cell_number_width)
        starting_y = random.randint(0, cell_number_height)

        starting_index = table.get_index(starting_x, starting_y)
        table.current = table.tab[starting_index]
        table.current.visited = True

        maze_done = False
        run_game_bool = True
        sidebar_bool = True
        limit_CPU = False

    elif run_game_bool and not maze_done:
        maze_done = run_game(table, maze_colour)

    elif maze_done:
        #table.draw_table(red)
        run_game_bool = False
        allow_start_search = True
        maze_done = False
        limit_CPU = True

    elif allow_start_search and solve_bool:
        starting_x, starting_y = table.get_random_border_index()
        starting_index = table.get_index(starting_x, starting_y)
        starting = table.tab[starting_index]
        starting.visited = True


        goal_index = table.get_index(cell_number_width - starting_x - 1, cell_number_height - 1)
        goal = table.tab[goal_index]

        #table.show_cell(starting, green)
        table.show_cell(goal, red)

        table.table_reset(False)

        if depth_first_search_bool:
            table.stack.append(starting)
        elif breadth_first_search_bool:
            table.stack.append([starting])

        allow_start_search = False
        solve_bool = False
        search = True
        limit_CPU = False


    if search and not done_search:
        if depth_first_search_bool:
            done_search = depth_first_search(table, green, goal)

        elif breadth_first_search_bool:
            done_search = breadth_first_search(table, goal)

    if done_search:
        search = False
        done_search = False
        draw_path = True
        draw_path_cycle_counter = 0
        limit_CPU = True

        #faster path drawing
        fps = fps * 3

    if draw_path:
        if len(table.stack) > 0:
            cell = table.stack.pop(0)
            table.show_cell(cell, blue)
        else:
            draw_path = False

    if sidebar_bool:
        #sidebar menu button hoover
        button(mouse, display_surf, button_hoover_color, sidebar_menu_button_rect, sidebar_menu_button_text)

        #sidebar solve button hover
        if allow_start_search:
            button(mouse, display_surf, button_hoover_color, sidebar_solve_button_rect, sidebar_solve_button_text)


    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #if we are on the main menu
            if start_screen_bool:
                #if the mouse is clicked on the button the game is started
                if mouse_on_button(mouse, start_button_rect):
                    display_surf.fill(white)
                    setup_game = True
                    start_screen_bool = False

                #if the button is clicked the application is quitted
                if mouse_on_button(mouse, quit_button_rect):
                    pygame.quit()
                    sys.exit()

                #options button
                if mouse_on_button(mouse, options_button_rect):
                    display_surf.fill(white)

                    start_screen_bool = False
                    options_tab = True

            #if we are in the options tab
            if options_tab:
                #back to menu button
                if mouse_on_button(mouse, options_menu_button_rect):
                    display_surf.fill(white)

                    options_tab = False
                    start_screen_bool = True

                #breadth first search button
                if mouse_on_button(mouse, breadth_first_search_button_rect):
                    breadth_first_search_bool = True
                    depth_first_search_bool = False

                #depth first search button
                if mouse_on_button(mouse, depth_first_search_button_rect):
                    depth_first_search_bool = True
                    breadth_first_search_bool = False

            #if we are on the sidebar menu
            if sidebar_bool:
                #sidebar menu button
                if mouse_on_button(mouse, sidebar_menu_button_rect):
                    display_surf.fill(white)
                    table.table_reset(True)

                    start_screen_bool = True
                    search = False
                    run_game_bool = False
                    sidebar_bool = False
                    draw_path = False
                    setup_game = False
                    options_tab = False
                    maze_done = False
                    solve_bool = False
                    allow_start_search = False

                #solve button
                if mouse_on_button(mouse, sidebar_solve_button_rect):
                    solve_bool = True

    pygame.display.update()

    if limit_CPU:
        pygame.time.Clock().tick(fps)
