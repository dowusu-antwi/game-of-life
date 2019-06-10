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

        # this will keep track of whether the
        #  rendering has begun, added because
        #  the first frame is skipped and not
        #  rendered for some reason...see inside
        #  draw_rectangles method below*
        self.drawn = None

        board_width, board_height = (20, 20)
        self.board = main.Board(board_width, board_height, "arrow", (2,2))
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

        # *if nothing has yet been drawn, will skip
        #  this iteration (so that the first frame
        #  is not skipped instead)
        if not self.drawn:
            self.drawn = True
            return

        current_board = self.board.seed

        for row,_ in enumerate(current_board):
            for col,__ in enumerate(_):
                y = row*self.pixel_height
                x = col*self.pixel_width
                if __:
                    painter.setBrush(QtGui.QColor(200,0,0))
                else:
                    painter.setBrush(QtGui.QColor(0,0,200))
                painter.drawRect(x, y, self.pixel_width, self.pixel_height)

        self.board.seed = self.board.get_next_state()

    def draw_objects(self, painter):
        """
        This will draw any objects necessary to
         the screen.
        """

        self.draw_rectangles(painter)

if __name__ == "__main__":

    new_widget = App([1000, 1000])
    sys.exit(new_widget.app.exec_())
