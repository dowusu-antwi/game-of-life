#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class App(QtWidgets.QWidget):
    """
    Top level application window for Game of Life.
    """
    def __init__(self):
        """
        Initializes PyQt application manager and builds application components,
        before maximizing application window.
        """
        self.application_manager = QtWidgets.QApplication([])
        super().__init__()
        self.build()
        self.showMaximized()

    def build(self):
        """
        Organizes main top level layout and widgets.
        """
        toplevel_layout = QtWidgets.QHBoxLayout()
        self.setLayout(toplevel_layout)

        gameboard = GameBoard()
        dashboard_grid = Dashboard(toplevel_layout)

        GAMEBOARD_STRETCH = 3
        toplevel_layout.addWidget(gameboard, GAMEBOARD_STRETCH)

    def run(self):
        """
        Executes application.
        """
        self.application_manager.exec_()
 

class GameBoard(QtWidgets.QWidget):
    """
    Gridded game board widget.
    """
    def __init__(self):
        super().__init__()
 
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setBrush(QtGui.QColor(200,0,0))
        for index in range(14):
            painter.drawRect(0 + index*100, 0, 100, 100)
        painter.end()


class Dashboard(QtWidgets.QGridLayout):
    """
    Contains buttons and list selectors to modify contents of game board.
    """
    def __init__(self, parent_layout):
        """
        Initializes dashboard widget layout and makes dashboard control grid.
        """
        super().__init__()
        DASHBOARD_STRETCH = 1
        parent_layout.addLayout(self, DASHBOARD_STRETCH)
        self.make_grid()

    def make_grid(self):
        """
        Organizes dashboard controls (i.e., buttons, list selectors).
        """
        patterns = QtWidgets.QListWidget()
        label = QtWidgets.QLabel('Location:')
        label.setAlignment(QtCore.Qt.AlignCenter)
        editX = QtWidgets.QLineEdit()
        editY = QtWidgets.QLineEdit()
        selected_pattern_image = QtWidgets.QWidget()
        start_button = QtWidgets.QPushButton('Start')
        pause_button = QtWidgets.QPushButton('Pause')
        reset_button = QtWidgets.QPushButton('Reset')

        self.addWidget(patterns, *(0, 0, 2, 1))
        self.addWidget(selected_pattern_image, *(0, 1, 1, 3))
        self.addWidget(label, *(1, 1, 1, 1))
        self.addWidget(editX, *(1, 2, 1, 1))
        self.addWidget(editY, *(1, 3, 1, 1))
        self.addWidget(start_button, *(2, 0, 2, 1))
        self.addWidget(pause_button, *(2, 1, 1, 3))
        self.addWidget(reset_button, *(3, 1, 1, 3))
        

if __name__ == "__main__":
    gui = App()
    gui.run()
