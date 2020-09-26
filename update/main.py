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

WIDTH = 6
HEIGHT = 6
SEED = [[DEAD_VAL]*6,
        [DEAD_VAL, LIVING_VAL, LIVING_VAL, LIVING_VAL, DEAD_VAL, DEAD_VAL],
        [DEAD_VAL, DEAD_VAL, LIVING_VAL, LIVING_VAL, LIVING_VAL, DEAD_VAL],
        [DEAD_VAL]*6,
        [DEAD_VAL]*6,
        [DEAD_VAL]*6]

def play():
    '''
    Creates game and builds GUI.
    '''
    grid = Grid(WIDTH, HEIGHT, SEED)
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
    game = Grid(WIDTH, HEIGHT, SEED)
    gui = App(game)
    gui.run()
