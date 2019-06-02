#!/usr/bin/env python3

"""
Game of Life Renderer
Author: dowusu

 This will open a PyQt window and draw rectangles
  to the screen representing the cells of the game
  of life.
"""

import sys
import gen
from PyQt4 import QtGui,QtCore

class App(QtGui.QWidget):
    """
    This is the main widget class
    """

    def __init__(self, width, height):
        self.app = QtGui.QApplication(sys.argv)
        super(App,self).__init__()
        self.setWindowTitle("Game of Life")
        self.resize_window(width, height)
        self.timer = self.setup_timer()
        self.rectangle_counter = gen.gen()
        self.show()

    def setup_timer(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(50)
        return timer
        
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

    def drawRectangles(self, painter):
        """
        This draws rectangles to the screen.
        """

        counter = next(self.rectangle_counter)
        print(counter)
        if counter:
            painter.drawRect(0,0,100,100)
        else:
            painter.drawRect(100,100,100,100)

    def drawObjects(self, painter):
        """
        This will draw any objects necessary to
         the screen.
        """

        self.drawRectangles(painter)

if __name__ == "__main__":

    new_widget = App(500, 250)

    """
    timer = QtCore.QTimer()
    timer.timeout.connect(new_widget.tick)
    timer.start(1000)
    """ 
    sys.exit(new_widget.app.exec_())
