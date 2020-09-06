#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui

'''
Game of Life: GUI Layout

author: dowusu
date: March 18th, 2020

'''

'''
BREAKDOWN:
1. create launch page, with launch button,
2. open main GUI window,
3. adds title section, with:
    (i) live/dead cell count,
    (ii) time step count,
4. adds game window, linking to side panel buttons...
5. adds side panel with:
    (i) Start button (change to pause/play + reset on button press)
    (ii) Load Seed button,
    (iii) Add Pattern button with pattern Position textbox, reflect/rotate
    (iv) List of patterns to select from for Add Pattern button.
'''

class App(QtGui.QWidget):
    '''
    Standard application window
    '''
    def __init__(self):
        self.qapp = QtWidgets.QApplication(sys.argv)
        super().__init__()

    ## Contains application objects:
    ##  1. Buttons (Start, Load Seed, Add Pattern),
    ##  2. Title with header: Live/Dead/TS updating labels,
    ##  3. Game window with updating cells.

class GamePage(App):
    '''
    The main game application.
    '''

    def __init__(self):
        self.header = self.make_header()
        self.game_window = self.make_game_window()
        self.side_panel = self.make_side_panel()

    def make_header(self):
        pass

    def update_header(self):
        pass

    def make_game_window(self):
        pass

    def update_game(self):
        pass

    def make_side_panel(self):
        pass

    def update_side_panel(self):
        pass

def start():
    '''
    Begins the simulation, storing the current Seed for a reset, and waits for
     a Pause (for which, stores the current Seed for reloading). 
    '''
    pass

def pause():
    '''
    Pauses the simulation, storing the current Seed for reloading on Play.
    '''
    pass

def play():
    '''
    Plays a paused simulation, retrieving the stored Seed and reloading it.
    '''
    pass

if __name__ == "__main__":
    game = App()
    game.showMaximized()
    sys.exit(game.qapp.exec_())
