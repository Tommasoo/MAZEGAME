from variables import *

def breadth_first_search(tab, goal):
    paths = tab.stack

    current_path = paths.pop(0)

    current = current_path[-1]

    if current == goal:
        print(current_path)
        tab.stack = current_path
        return True

    elif not current.visited:
        current.visited = True
        tab.show_cell(current, green)

        neighbors = tab.get_maze_neighs(current)

        for neigh in neighbors:
            new_path = current_path.copy()
            new_path.append(neigh)
            paths.append(new_path)

    return False
