#!/usr/bin/env python3

"""
Test Cases for Conway's Game of Life sim
"""

import unittest
import main

class Test(unittest.TestCase):

    # These test whether a dead board is printed
    #  correctly
    def test_01(self):
        board = main.Board(5,5)
        result = board.get_dead_board()
        expected = [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
        self.assertEqual(result, expected)

    def test_02(self):
        b = main.Board(0,0)
        r = b.get_dead_board()
        e = []
        self.assertEqual(r, e)

    # This tests whether a random board is printed
    #  correctly
    def test_03(self):
        b = main.Board(5,5)
        r = b.get_random_board()
        r_height = len(r)
        e_height = 5
        self.assertEqual(r_height, e_height)

        all_cells_valid = True
        for row in r:
            for col in row:
                if col not in [0,1]:
                    all_cells_valid = False
                    break
        self.assertTrue(all_cells_valid,("cell %s is not valid" % col))

    # These test whether the next state has been
    #  calculated correctly given the initial state
    def test_04(self):
        b = main.Board(3,3)
        b.seed = [[0,0,0],
                   [0,0,1],
                   [0,0,0]]
        r = b.get_next_state()
        e = [[0,0,0],
             [0,0,0],
             [0,0,0]]
        self.assertEqual(r,e)

    def test_05(self):
        b = main.Board(3,3)
        b.seed = [[1,1,1],
                   [1,1,1],
                   [1,1,1]]
        r = b.get_next_state()
        e = [[1,0,1],
             [0,0,0],
             [1,0,1]]
        self.assertEqual(r,e)

    def test_06(self):
        b = main.Board(3,3)
        b.seed = [[1,0,1],
                   [0,0,0],
                   [1,0,1]]
        r = b.get_next_state()
        e = [[0,0,0],
             [0,0,0],
             [0,0,0]]
        self.assertEqual(r,e)

    def test_07(self):
        b = main.Board(3,3)
        b.seed = [[1,1,0],
                   [1,0,0],
                   [0,0,0]]
        r = b.get_next_state()
        e = [[1,1,0],
             [1,1,0],
             [0,0,0]]
        self.assertEqual(r,e)

    def test_08(self):
        b = main.Board(3,3)
        b.seed = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        r = b.get_next_state()
        e = [[0,0,0],
             [0,0,0],
             [0,0,0]]
        self.assertEqual(r,e)

if __name__ == "__main__":
    result = unittest.main(verbosity=3, exit=False)
