#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
import sys

LIVING_VAL = 1
DEAD_VAL = 0

class App(QtWidgets.QWidget):
    """
    Top level application window for Game of Life.
    """
    def __init__(self, game):
        """
        Initializes PyQt application manager and builds application components,
        before maximizing application window.
        """
        self.application_manager = QtWidgets.QApplication([])
        super().__init__()
        self.build(game)
        self.setup_timer()
        self.showMaximized()

    def setup_timer(self):
        """
        Sets up timer for updating main app, with milliseconds for timer count.
        """
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)

    def build(self, game):
        """
        Organizes main top level layout and widgets.

        Inputs:
            game: Grid class instance from game.py
        """
        toplevel_layout = QtWidgets.QHBoxLayout()
        self.setLayout(toplevel_layout)

        # Adds gameboard and dashboard widgets to top level layout.
        gameboard = GameBoard(game)
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
    def __init__(self, game):
        super().__init__()
        self.game = game
 
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.game.update_state()
        self.display_state(painter)
        painter.end()

    def display_state(self, painter):
        """
        Draw current game (grid) state, with painter, to main app window.
        """
        grid = self.game.get_grid()
        game_dimensions = self.game.dimensions

        frame_width = self.frameGeometry().width()
        frame_height = self.frameGeometry().height()
        grid_width, grid_height = game_dimensions
        pixel_width = frame_width / grid_width
        pixel_height = frame_height / grid_height

        RED = 200

        for column in range(0, grid_width):
            for row in range(0, grid_height):
                cell_state = self.game.get_state([row, column])
                if cell_state == LIVING_VAL:
                    painter.setBrush(QtGui.QColor(RED, 0, 0))
                elif cell_state == DEAD_VAL:
                    painter.setBrush(QtGui.QColor(200, 200, 200))
                x = column * pixel_width
                y = row * pixel_height
                painter.drawRect(x, y, pixel_width, pixel_height)


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
        painter.setBrush(QtGui.QColor(100, 10, 90))
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
    pass
