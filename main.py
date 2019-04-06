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
        self.board = self.get_random_board()

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
        for row in self.board:
            print(''.join(['*']+['#' if cell else ' ' for cell in row]+['*']))
        print('*'*(self.width+2))

    def get_next_state(self):
        pass

if __name__ == "__main__":

    b = Board(5,5)
    b.render_board()
