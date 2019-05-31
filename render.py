#!/usr/bin/env python2

"""
Game of Life Renderer
Author: dowusu

 This will open a PyQt window and draw rectangles
  to the screen representing the cells of the game
  of life.
"""

import sys
from PyQt4 import QtGui

class App(QtGui.QMainWindow):
    """
    This is the main widget class
    """

    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        super(App,self).__init__()
        self.create_window()
        self.show()

    def create_window(self):
        self.setWindowTitle("Game of Life")
        self.setGeometry(0,0,100,100)


if __name__ == "__main__":

    new_widget = App()
    sys.exit(new_widget.app.exec_())
