#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import random

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
        self.setup_timer()
        self.showMaximized()

    def setup_timer(self):
        """
        Sets up timer for updating main app, with milliseconds for timer count.
        """
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(500)

    def build(self):
        """
        Organizes main top level layout and widgets.
        """
        toplevel_layout = QtWidgets.QHBoxLayout()
        self.setLayout(toplevel_layout)

        # Adds gameboard and dashboard widgets to top level layout.
        gameboard = GameBoard()
        GAMEBOARD_STRETCH = 3
        toplevel_layout.addWidget(gameboard, GAMEBOARD_STRETCH)
        
        dashboard_grid = Dashboard(toplevel_layout)

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
        self.display_state(painter)
        painter.end()

    def display_state(self, painter):
        """
        """
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        red = random.random() * 200
        green = random.random() * 200
        blue = random.random() * 200
        painter.setBrush(QtGui.QColor(red, green, blue))
        painter.drawRect(0, 0, width, height)


class CustomWidget(QtWidgets.QWidget):
    """
    Custom widget (currently, for selected pattern's image).
    """
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        painter = QtGui.QPainter()
        painter.begin(self)
        red = random.random() * 200
        green = random.random() * 200
        blue = random.random() * 200
        painter.setBrush(QtGui.QColor(red, green, blue))
        painter.drawRect(0, 0, width, height)
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
        #selected_pattern_image = QtWidgets.QWidget()
        selected_pattern_image = CustomWidget()
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
