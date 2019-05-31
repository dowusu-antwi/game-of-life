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

    def __init__(self, width, height):
        self.app = QtGui.QApplication(sys.argv)
        super(App,self).__init__()
        self.setWindowTitle("Game of Life")
        self.resize_window(width, height)
        self.show()

    def resize_window(self, width, height):
        """
        This changes the window dimensions
        """
        self.setGeometry(0,0,width,height)

    def paintEvent(self, e):
        """
        This method is required for PyQt to paint
         elements to the screen. 
        """

        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawObjects(painter)
        painter.end()

    def drawObjects(self, painter):
        """
        This will draw any objects necessary to
         the screen.
        """

        self.drawRectangles(painter)

    def drawRectangles(self, painter):
        """
        This draws rectangles to the screen.
        """
        painter.drawRect(0,0,100,100)
        painter.drawRect(100,100,100,100)

if __name__ == "__main__":

    new_widget = App(500, 250)
    sys.exit(new_widget.app.exec_())
