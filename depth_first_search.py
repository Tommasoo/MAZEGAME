
def depth_first_search(tab, colour, goal):

    queue = tab.stack

    if (len(queue) > 0):
        tab.current = queue[-1]

        if (tab.current == goal):
            return True

        tab.current.visited = True
        tab.show_cell(tab.current, colour)

        neighbours = tab.get_maze_neighs(tab.current)

        for neigh in neighbours:
            if not neigh.visited:
                neigh.visited = True
                queue.append(neigh)
                break
        else:
            queue.pop(-1)



    else:
        return False