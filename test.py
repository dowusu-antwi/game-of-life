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
        raise NotImplementedError()

    # These test whether the next state has been
    #  calculated correctly given the initial state
    def test_04(self):
        raise NotImplementedError()

    def test_05(self):
        raise NotImplementedError()

    def test_06(self):
        raise NotImplementedError()

    def test_07(self):
        raise NotImplementedError()

if __name__ == "__main__":
    result = unittest.main(verbosity=3, exit=False)
