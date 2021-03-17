from table import table_obj
from variables import *


def breadth_first_search_2(tab, dist, cell_side, colour, font = font_dist):

    queue = tab.stack

    if (len(queue) > 0):
        tab.current = queue.pop(0)
        tab.show_cell(tab.current, colour)

        x = tab.current.x
        y = tab.current.y
        current_index = tab.get_index(x, y)

        text_x = (x * cell_side) + cell_side // 4
        text_y = (y * cell_side) + cell_side // 4

        text = str(dist[current_index])

        text_obj = font.render(text, True, black)  # testo
        #display_surf.blit(text_obj, (text_x, text_y))

        neighbours = tab.get_maze_neighs(tab.current)

        for neigh in neighbours:
            if neigh.visited == False:
                neigh.visited = True
                queue.append(neigh)

                x = neigh.x
                y = neigh.y
                index = tab.get_index(x, y)

                dist[index] = dist[current_index] + 1
