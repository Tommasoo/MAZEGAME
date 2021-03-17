

def run_game(tab, maze_colour):

    #picking random neighor
    next = tab.get_random_neigh(tab.current)


    if not (next == -1):
        next.visited = True
        #merging cells
        tab.remove_walls(tab.current, next)

        #showing current cell
        tab.show_cell(tab.current, maze_colour)
        tab.show_cell(next, maze_colour)

        #adding current cell to stack
        tab.stack.append(tab.current)

        #set current as next
        tab.current = next

    elif (len(tab.stack) > 0):
        tab.current = tab.stack.pop() #if stuck, get new neighbor

    else:
        return True #return true when the maze is done

    return False