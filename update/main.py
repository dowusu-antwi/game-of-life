#!/usr/bin/env python3

from game import *
from gui import *
import time

'''
Conway's Game of Life Update (Design)

author: dowusu
date: March 18th, 2020

Modules:
    1. Game Creation
    2. GUI Layout
    3. Main: Build GUI and Create Game
'''

WIDTH = 80
HEIGHT = 80

def add_patterns(game):
    for i in range(0, 40, 4):
        anchor = (i, i)
        game.add_pattern("glider", anchor)
    game.add_pattern("toad", (30, 10))
    game.add_pattern("toad", (10, 30))
    game.add_pattern("beacon", (25, 12))
    game.add_pattern("arrow", (60, 10))

def play():
    '''
    Creates game and builds GUI.
    '''
    grid = Grid(WIDTH, HEIGHT)
    while True:
        time.sleep(0.5)
        grid.update_state()
        grid.render()

def launch():
    '''
    Creates launch page GUI, with button taking user to the game.
    '''
    launch_page = LaunchPage()
    game_page = GamePage()

if __name__ == "__main__":
    game = Grid(WIDTH, HEIGHT)
    add_patterns(game)
    gui = App(game)
    gui.run()
