import pygame
import random

class table_obj:
    tab = []

    #number of cells on both sides
    n_cells_width = None
    n_cells_height = None

    #lenght in pixels of the side of the cell
    cell_side = None

    #surface on which the table has to be drawn
    surface = None

    #multi purpose stack/queue
    stack = []

    #multi purpose current
    current = None

    #border width of the cells when drawing
    border_width = None

    def __init__(self, n_width, n_height, cell_width, sup, border_width):
        self.n_cells_width = n_width
        self.n_cells_height = n_height
        self.cell_side = cell_width
        self.surface = sup
        self.border_width = border_width

        #table creation
        for y in range(n_height):
            for x in range(n_width):
                cell = self.cell_obj(x, y)
                self.tab.append(cell)


    #all cells are marked as unvisited
    def table_reset(self, newWalls):
        for i in range(self.n_cells_width * self.n_cells_height):
            self.tab[i].visited = False

            if newWalls:
                self.tab[i].walls = [True] * 4

        self.stack.clear()


    #returns index of specific cell, if no cell is found, index returned is -1
    def get_index(self, x, y):
        if (x >= 0 and x < self.n_cells_width and y >= 0 and y < self.n_cells_height):
            return x + (y * self.n_cells_width)
        else:
            return -1


    #returns the neighbours of a cell
    def get_neighbours(self, cell):
        x = cell.x
        y = cell.y

        neighs = []
        neigh_coords = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

        for coords in neigh_coords:
            index = self.get_index(*coords)
            if not (index == -1):
                neighbour = self.tab[index]
                if not (neighbour.visited):
                    neighs.append(neighbour)

        return neighs


    #gets a random neighbor
    def get_random_neigh(self, cell):
        neighs = self.get_neighbours(cell)

        if (len(neighs) > 0):
            random_index = random.randint(0, len(neighs) - 1)
            return neighs[random_index]
        else:
            return -1


    def get_maze_neighs(self, cell):
        x = cell.x
        y = cell.y

        neighs = []
        neigh_coords = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]


        for i in range(4):
            coords = neigh_coords[i]
            index = self.get_index(*neigh_coords[i])

            if not (index == -1):
                neighbour = self.tab[index]
                if not (neighbour.visited):

                    if coords == (x, y - 1) and not cell.walls[0] or coords == (x + 1, y) and not cell.walls[1] or coords == (x, y + 1) and not cell.walls[2] or coords == (x - 1, y) and not cell.walls[3]:
                        neighs.append(neighbour)

        return neighs

    def draw_table(self, colour):
        for cell in self.tab:
            self.show_cell(cell, colour)

    #removes walls between two cells
    def remove_walls(self, cell, neigh):
        x_axis = cell.x - neigh.x
        y_axis = cell.y - neigh.y

        #right wall
        if (x_axis == -1):
            cell.walls[1] = False
            neigh.walls[3] = False

        #left wall
        elif (x_axis == 1):
            cell.walls[3] = False
            neigh.walls[1] = False

        #upper wall
        if (y_axis == 1):
            cell.walls[0] = False
            neigh.walls[2] = False

        #lower wall
        elif (y_axis == -1):
            cell.walls[2] = False
            neigh.walls[0] = False


    #show the cell
    def show_cell(self, cell, cell_colour, border_colour = (0, 0, 0)):
        side = self.cell_side

        x_coord = cell.x * side
        y_coord = cell.y * side

        upper_side = ((x_coord, y_coord), (x_coord + side, y_coord))
        right_side = ((x_coord + side, y_coord), (x_coord + side, y_coord + side))
        bottom_side = ((x_coord, y_coord + side), (x_coord + side, y_coord + side))
        left_side = ((x_coord, y_coord), (x_coord, y_coord + side))

        sides = [upper_side, right_side, bottom_side, left_side]

        # filling the cell
        rect = (x_coord, y_coord, side, side)

        if cell.visited:
            pygame.draw.rect(self.surface, cell_colour, rect, 0)  # visited

        # drawing the sides of the cell
        for i in range(len(cell.walls)):
            if (cell.walls[i]):
                pygame.draw.line(self.surface, border_colour, *sides[i], self.border_width)

    def get_random_border_index(self):
        rand_side = random.randint(0, 3)
        #upper side
        if (rand_side == 0):
            y = 0
            x = random.randint(0, self.n_cells_width - 1)
        #left side
        elif(rand_side == 1):
            y = random.randint(0, self.n_cells_height - 1)
            x = self.n_cells_width - 1
        #bottom side
        elif(rand_side == 2):
            y = self.n_cells_height - 1
            x = random.randint(0, self.n_cells_width - 1)
            #right side
        elif(rand_side == 3):
            y = random.randint(0, self.n_cells_height - 1)
            x = 0

        return x, y

    #inner table class cell
    class cell_obj():
        x = None
        y = None

        visited = False

        walls = None

        def __init__(self, x_coord, y_coord):
            self.x = x_coord
            self.y = y_coord

            self.walls = [True] * 4




