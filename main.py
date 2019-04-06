#!/usr/bin/env python3

"""
Conway's Game of Life
author: dowusu-antwi

 Each cell on the board will look at its neighbors
  and update according to rules based on the number
  of living and dead neighbors

"""

import random
import time

class Board:

    def __init__(self, width, height):
        self.dimensions = [height, width]
        self.width = width
        self.height = height
        self.seed = self.get_random_board()

    def get_random_board(self):
        """
        This returns a board of dimensions given by
         width and height attributes, with each cell
         set to 1 (alive) or 0 (dead) randomly
        """
        return [[random.randint(0,1) for x in range(self.width)]
                for x in range(self.height)]        

    def get_dead_board(self):
        """
        This returns a board of dimensions given by
         width and height attributes, with each cell
         set to 0 (dead)
        """
        return [[0 for x in range(self.width)]
                for x in range(self.height)]

    def render_board(self):
        """
        This renders the board, treating alives (1)
         as hashes (#) and deads (0) as spaces, and
         uses asterisks for the boundary
        """

        # this prints the top and bottom boundaries,
        #  an in between renders '*' + row cells + '*'
        #  for each row on the board
        print('*'*(self.width+2))
        for row in self.seed:
            print(''.join(['*']+['#' if cell else ' ' for cell in row]+['*']))
        print('*'*(self.width+2))

    def coordinates_in_bounds(self, coordinates):
        """
        This checks if given coordinates are in the
         boundaries of the board
        """

        (row, col) = coordinates
        return ((row >= 0 and row < self.height) and
                (col >= 0 and col < self.width))

    def get_next_state(self):
        """
        This will look at the current state of the board
         and update each cell according to Conway's rules:

        1. live cell with < 2 live neighbours dies          -> underpopulation.
        2. live cell with > 3 live neighbours dies          -> overpopulation.
        3. live cell with 2 or 3 live neighbours survives
        4. dead cell with == 3 live neighbours becomes live -> reproduction.
        """

        # this gets all neighboring cells of the given
        #  cell coordinates so that the next cell state
        #  can be updated given the states of its
        #  neighbors, recursively
        #
        # (recursive solution is more efficient and makes
        #  higher dimensions easy to integrate...!)
        def get_cell_neighbors(coordinates, neighbors=[], original_coordinates=None):

            # this keeps track of original coordinates so
            #  that it can be removed from neighbors at the end,
            #  since we will not consider a cell its own neighbor
            if not original_coordinates:
                original_coordinates = coordinates

            # BC: no coordinates remain
            if coordinates == ():
                # this eliminates all out of bounds cells
                #  before returning it
                neighbors_in_bounds = []
                for neighbor in neighbors:
                    if self.coordinates_in_bounds(neighbor):
                        neighbors_in_bounds.append(neighbor)

                # this removes the original coordinates (since
                #  a cell is not its own neighbor)
                if neighbors_in_bounds:
                    neighbors_in_bounds.remove(original_coordinates)
                return neighbors_in_bounds

            # Recursive: iterates over neighbors and
            #  returns new list
            else:
                first_coord = coordinates[0]
                other_coords = coordinates[1:]
                first_neighbors = [(first_coord-1,),
                                   (first_coord,),
                                   (first_coord+1,)]

                # the first set of neighbors has already been
                #  generated, if neighbors is currently empty
                if not neighbors:
                    return get_cell_neighbors(other_coords, first_neighbors,
                                              original_coordinates)

                # otherwise, iterates over current neighbors
                #  and gets new neighbors from them by adding
                #  on coordinate neighbors of the coordinate
                #  in focus
                else:
                    new_neighbors = []
                    for neighbor in neighbors:
                        new_neighbors.extend([neighbor + new_coord
                                              for new_coord in first_neighbors])
                    return get_cell_neighbors(other_coords, new_neighbors,
                                              original_coordinates)

        # this helper function gets an updated cell
        #  value given its neighboring cell coords
        def get_updated_cell(cell, neighbors):

            # this counts live neighbors
            live = 0
            for neighbor in neighbors:
                row, column = neighbor
                if self.seed[row][column]:
                    live += 1

            # this applies rules to get whether cell
            #  is live or dead in next state, conditioned
            #  on its current status (live or dead)
            if cell:
                if live < 2:    # dies by underpopulation
                    return 0
                if live <= 3:   # lives to next generation
                    return 1
                if live > 3:    # dies by overpopulation
                    return 0        
 
            else:
                if live == 3:   # lives by reproduction 
                    return 1
            return cell

        # this generates an empty (dead) board and
        #  for each cell, gets the updated cell status
        #  and updates the empty board, then returns it
        next_state = self.get_dead_board()
        for row, row_of_cells in enumerate(self.seed):
            for col, cell in enumerate(row_of_cells):
                coordinates = (row, col)

                neighbors = get_cell_neighbors(coordinates)
                updated_cell = get_updated_cell(cell, neighbors)

                next_state[row][col] = updated_cell

        return next_state

    # this will run an infinite game of life
    def play_game(self):
        while True:
            self.render_board()
            time.sleep(0.3)
            self.seed = self.get_next_state()

if __name__ == "__main__":

    b = Board(6,6)
    b.play_game()

    toad = [[0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,1,1,1,0],
            [0,1,1,1,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]

