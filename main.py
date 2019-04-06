#!/usr/bin/env python3

"""
Conway's Game of Life
author: dowusu-antwi

 Each cell on the board will look at its neighbors
  and update according to rules based on the number
  of living and dead neighbors

"""

import random

class Board:

    def __init__(self, width, height):
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

    def get_next_state(self):
        """
        """

        # this gets all neighboring cells of the given
        #  cell coordinates so that the next cell state
        #  can be updated given the states of its
        #  neighbors
        def get_cell_neighbors(cell_coordinates, neighbors=[]):

            pass

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

if __name__ == "__main__":

    b = Board(5,5)
    b.render_board()
