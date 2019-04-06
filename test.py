#!/usr/bin/env python3

"""
Test Cases for Conway's Game of Life sim
"""

import unittest
import main

class Test(unittest.TestCase):

    # This tests whether a dead board is printed
    #  correctly
    def test_01(self):
        raise NotImplementedError()

    # This tests whether a random board is printed
    #  correctly
    def test_02(self):
        raise NotImplementedError()

    # These test whether the next state has been
    #  calculated correctly given the initial state
    def test_03(self):
        raise NotImplementedError()

    def test_04(self):
        raise NotImplementedError()

    def test_05(self):
        raise NotImplementedError()

    def test_06(self):
        raise NotImplementedError()

if __name__ == "__main__":
    result = unittest.main(verbosity=3, exit=False)
