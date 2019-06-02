#!/usr/bin/env python3

"""
Game of Life Renderer
Author: dowusu

 This will open a PyQt window and draw rectangles
  to the screen representing the cells of the game
  of life.
"""

import sys
import main
from PyQt4 import QtGui,QtCore

class App(QtGui.QWidget):
    """
    This is the main widget class
    """

    def __init__(self, window_dim):
        self.app = QtGui.QApplication(sys.argv)
        super(App,self).__init__()

        self.setWindowTitle("Game of Life")
        width,height = window_dim
        self.resize_window(width, height)
        self.timer = self.setup_timer()

        board_width, board_height = (30, 30)
        self.board = main.Board(board_width, board_height)
        self.pixel_width, self.pixel_height = (width/board_width, height/board_height)

        self.show()

    def setup_timer(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(100)
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
        self.draw_objects(painter)
        painter.end()

    def draw_rectangles(self, painter):
        """
        This draws rectangles to the screen.
        """

        # this will get current board to render,
        #  and draw rectangles to render it, then
        #  it will calculate the next board and
        #  reset it

        current_board = self.board.seed

        for row,_ in enumerate(current_board):
            for col,__ in enumerate(_):
                x = row*self.pixel_width
                y = col*self.pixel_height
                if __:
                    painter.setBrush(QtGui.QColor(100,0,0))
                else:
                    painter.setBrush(QtGui.QColor(0,0,100))
                painter.drawRect(x, y, self.pixel_width, self.pixel_height)

        self.board.seed = self.board.get_next_state()

    def draw_objects(self, painter):
        """
        This will draw any objects necessary to
         the screen.
        """

        self.draw_rectangles(painter)

if __name__ == "__main__":

    new_widget = App([900, 900])
    sys.exit(new_widget.app.exec_())
