#!/usr/bin/env python3

from patterns import *

'''
Game of Life: Game Creation

author: dowusu
date: March 18th, 2020
'''

LIVING = 1
DEAD = 0

class Grid:

    def __init__(self, width, height, seed=None):
        '''
        Makes a grid with given seed grid, or an empty grid if no seed given.
         Saves a seed copy, to allow for a reset.
        
        Inputs:
         width (int): grid width in cell number,
         height (int): grid height in cell number,
         seed (2D list): represents seed grid to begin simulation from.

        Returns Grid class instance.
        '''
        grid = [[DEAD] * width for i in range(height)] if not seed else seed
        self.grid = grid
        self.seed = [row[:] for row in grid]
        self.dimensions = [width, height]
        self.cells_to_update = self.build_update_set()


    def get_grid(self):
        '''
        Returns current grid stored in grid attribute.

        No inputs.

        Returns 2D list.
        '''
        return self.grid


    def reset(self):
        '''
        Resets current grid to seed.

        No inputs.

        No returns.
        '''
        self.grid = [row[:] for row in self.seed]


    def add_pattern(self, pattern_name, anchor):
        '''
        Adds block pattern to grid (and to seed) at given anchor.

        Inputs:
            pattern_name (str): name of pattern to lookup in dictionary,
            anchor (tuple): coordinates at which to anchor the given pattern.

        No returns.
        '''

        if pattern_name not in PATTERNS:
            print("Pattern name (%s) invalid." % pattern_name)
            return

        pattern = PATTERNS[pattern_name]
        anchor_row, anchor_column = anchor
        for row_number, row in enumerate(pattern):
            new_row = row_number + anchor_row
            for column_number, state in enumerate(row):
                new_column = column_number + anchor_column
                if (state == LIVING and self.in_bounds((new_row, new_column))):
                    self.grid[new_row][new_column] = LIVING
                    self.seed[new_row][new_column] = LIVING
        

    def update_state(self):
        '''
        Updates grid cells (i.e., carries out next time step).

        No inputs.

        No returns.
        '''

        # Iterates over grid cells, getting neighbors of each cell and
        #  updating according to the neighboring states.
        grid = self.get_grid()
        new_grid = []
        for x, row in enumerate(grid):
            new_row = []
            for y, value in enumerate(row):
                cell = [x,y]
                living_neighbors_count = self.count_living_neighbors(cell)
                state = grid[x][y]
                new_state = self.update_cell(state, living_neighbors_count)
                new_row.append(new_state)
            new_grid.append(new_row)
        self.grid = new_grid

        ## TRY TO ONLY KEEP TRACK OF WHICH CELLS ARE ALIVE, IN A SET?
        ## AND THEIR NEIGHBORS...
        # cells_to_update = self.cells_to_update()
        # look at cells in the set
        #  get neighbors
        #  if living, add to set and add neighbors
        #  elif dead, remove from set (will come back later if neighbor of
        #   living
        

    def build_update_set(self):
        '''
        Iterates over grid and gets minimal set of potentially-updatable cells
         (i.e., living cells and their neighbors). We should only need to run
         this once to build the set, then we update the set per timestep.

        No Inputs.

        Returns set of potentially-updatable cells.
        '''

        # Collects every cell that is either living or has living neighbors;
        #  for the first time step, no other cells will be updated (i.e., dead
        #  cells with no living neighbors remain dead in executing a time step).
        cells_to_update = set()
        grid = self.get_grid()
        for x, row in enumerate(grid):
            for y, value in enumerate(row):
                cell = [x, y]
                if self.get_state(cell) == LIVING:
                    cells_to_update.add(cell)
                elif self.count_living_neighbors(cell):
                    cells_to_update.add(cell)
        return cells_to_update


    def count_living_neighbors(self, cell):
        '''
        Counts number of live neighboring cells, given a cell's coordinates.

        Inputs:
         cell (list): coordinates for a cell.

        Returns integer representing number of neighboring live cells.
        '''

        # Gets neighbors and counts the number of living.
        neighbors = self.get_neighbors(cell)
        living = sum([1 for neighbor in neighbors 
                        if ((neighbor != cell) and 
                            (self.get_state(neighbor) == LIVING))])
        return living


    def get_neighbors(self, cell, dimension=0, neighbors=[]):
        '''
        Gets neighboring cells (including itself), given a cell's coordinates.
         (Not strictly useful in this implementation of GoL, but this
          generalizes to any dimension, not just 2D).

        Inputs:
         cell (list): coordinates for a cell,
         dimension (int): corresponds to the cell coordinate currently being
          generated,
         neighbors (list): recursively built list of neighboring cell
                           coordinates.

        Returns list of neighbors for initial given cell.
        '''

        # Base Case: for integer, returns its line neighbors that are in bounds
        #  because out of bounds neighbors will not be present in the grid; 
        #  for empty cell, returns saved (and recursively generated) neighbors
        #  parameter.
        if type(cell) == int:
            line_neighbors = [[cell + offset] for offset in [-1,0,1] 
                              if self.in_bounds(cell + offset, dimension)]
            return line_neighbors
        if cell == []:
            return neighbors
        
        # Recursive Case: fills in line neighbors if there are none, because
        #  line neighbors are the base case; otherwise, generates all possible
        #  combinations of generated line neighbors with stored coordinates
        #  (that represent neighbors in the process of being generated).
        first = cell[0]
        rest = cell[1:]
        if not neighbors:
            line_neighbors = self.get_neighbors(first)
            return self.get_neighbors(rest, dimension, line_neighbors)
        line_neighbors = self.get_neighbors(first, dimension)
        new_neighbors = []
        for index, neighbor in enumerate(neighbors):
            for line_neighbor in line_neighbors:
                new_neighbors.append(neighbors[index] + line_neighbor)
        return self.get_neighbors(rest, dimension + 1, new_neighbors)


    def in_bounds(self, cell, dimension=0):
        '''
        Return True if given cell coordinates are in bounds; False otherwise.
         (As above, generalized to any dimension but this is not particularly
          useful in this implementation, beyond looking clean.)

        Inputs:
         cell (list): coordinates for a cell,
         dimension (int): corresponds to the cell coordinate currently being
          generated.

        Returns boolean value.
        '''
        if type(cell) == int:
            dimension_max = self.dimensions[dimension]
            return (cell >= 0 and cell < dimension_max)
        if not cell: # empty cell
            return True
        return (self.in_bounds(cell[0], dimension) and 
                self.in_bounds(cell[1:], dimension + 1))


    def get_state(self, cell, search_space=None):
        '''
        Gets state at given cell's coordinates.

        Inputs:
         cell (list): coordinates for a cell,
         search_space (list): represents list to recursively search for the
          value at the coordinates given by the cell.

        Returns one of constants LIVING or DEAD.
        '''

        if search_space == None:
            search_space = self.grid
        if cell == []:
            if type(search_space) == list:
                raise ValueError(("Given cell coordinates must be a valid"
                                  " location."))
            return grid
        first = cell[0]
        rest = cell[1:]
        return self.get_state(rest, search_space[first])


    def update_cell(self, state, living_neighbors_count):
        '''
        Gets new cell state given neighboring states.

        Inputs:
         state (LIVING or DEAD): state of a given cell,
         living_neighbors_count (int): number of living neighbors.

        Returns updated cell state, LIVING or DEAD.
        '''

        # Applies Conway's Game of Life rules:
        #  1. Living cells with 2 or 3 live neighbors survives; otherwise, dies
        #      due to underpopulation (< 2) or overpopulation (> 3),
        #  2. Dead cells with 3 live neighbors become live due to reproduction.
        if state == LIVING:
            return LIVING if ((living_neighbors_count == 2) or 
                                  (living_neighbors_count == 3)) else DEAD
        return LIVING if living_neighbors_count == 3 else state


    def render(self):
        '''
        This renders the grid, with live cells as hashes (#), dead cells as
         whitespace, and asterisks for the boundary.

        No inputs.

        No returns.
        '''

        # this prints the top and bottom boundaries,
        #  an in between renders '*' + row cells + '*'
        #  for each row on the board
        print('*'*(self.dimensions[0]+2))
        for row in self.grid:
            print(''.join(['*']+['#' if state == LIVING else ' ' 
                  for state in row]+['*']))
        print('*'*(self.dimensions[0]+2))


if __name__ == "__main__":
    pass
