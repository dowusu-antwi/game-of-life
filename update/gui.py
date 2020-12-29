#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
from patterns import PATTERNS
from random import randint

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
        self.game = game
        self.build(game)
        self.showMaximized()

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
        
        dashboard_grid = Dashboard(toplevel_layout, gameboard)

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
                    x = column * pixel_width
                    y = row * pixel_height
                    painter.drawRect(x, y, pixel_width, pixel_height)
                elif cell_state == DEAD_VAL:
                    pass


class PatternImage(QtWidgets.QWidget):
    """
    Custom widget (currently, for selected pattern's image).
    """
    def __init__(self):
        """
        Saves pattern and initializes widget for painting pattern to screen.
        """
        super().__init__()
        self.pattern = None

    def draw_pattern(self, selected_items):
        """
        Draws pattern to widget, updating screen.
        """
        if not selected_items:
            print("No items selected.")
        else:
            pattern_name = selected_items[0].text()
            print("Pattern selected: %s" % pattern_name)
            print("Pattern grid:")
            print("=========================================")
            print(PATTERNS[pattern_name])
            self.pattern = PATTERNS[pattern_name]
            print("=========================================")
            self.update()

    def paintEvent(self, event):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        painter = QtGui.QPainter()
        painter.begin(self)
        if self.pattern == None:
            # Paints random color to widget.
            R, G, B = randint(0, 255), randint(0, 255), randint(0, 255)
            painter.setBrush(QtGui.QColor(R, G, B))
            painter.drawRect(0, 0, width, height)
        else:
            # Scales pattern to widget and paints to it.
            pattern = self.pattern
            pattern_height = len(pattern)
            pattern_width = len(pattern[0])
            pixel_width = width / pattern_width
            pixel_height = height / pattern_height
            painter.setBrush(QtGui.QColor(100, 0, 0))
            for row, pixels in enumerate(pattern):
                for column, pixel in enumerate(pixels):
                    if pixel == LIVING_VAL:
                        x = column * pixel_width
                        y = row * pixel_height 
                        painter.drawRect(x, y, pixel_width, pixel_height)
        painter.end()


class Dashboard(QtWidgets.QGridLayout):
    '''
    Contains buttons and list selectors to modify contents of game board.
    '''
    def __init__(self, parent_layout, gameboard):
        '''
        Initializes dashboard widget layout and makes dashboard control grid.
        '''
        super().__init__()
        DASHBOARD_STRETCH = 1
        parent_layout.addLayout(self, DASHBOARD_STRETCH)
        self.gameboard = gameboard
        self.timer = self.setup_timer()
        self.make_grid()

    def setup_timer(self):
        '''
        Sets up timer for updating gameboard, with milliseconds for timer count.

        Returns QTimer object.
        '''
        gameboard = self.gameboard

        timer = QtCore.QTimer(gameboard)
        timer.timeout.connect(gameboard.update)
        return timer

    def make_grid(self):
        '''
        Organizes dashboard controls (i.e., buttons, list selectors).
        '''

        # Create dashboard items
        patterns_list = QtWidgets.QListWidget()
        label = QtWidgets.QLabel('Pattern Anchor:')
        label.setAlignment(QtCore.Qt.AlignCenter)
        editX = QtWidgets.QLineEdit()
        editY = QtWidgets.QLineEdit()
        #selected_pattern_image = QtWidgets.QWidget()
        selected_pattern_image = PatternImage()
        start_button = QtWidgets.QPushButton('Start')
        toggle_button = QtWidgets.QPushButton('Pause')
        reset_button = QtWidgets.QPushButton('Reset')
        reflect_button = QtWidgets.QPushButton('Reflect')
        rotate_button = QtWidgets.QPushButton('Rotate')
        invert_button = QtWidgets.QPushButton('Invert')
        add_pattern_button = QtWidgets.QPushButton('Add Pattern')

        # Changes dashboard item properties
        #patterns_list.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
        #                            QtWidgets.QSizePolicy.Expanding)
        patterns_list.setSelectionMode(QtWidgets.QAbstractItemView. \
                                       SingleSelection)
        patterns_list.addItems(PATTERNS.keys())

        #selected_pattern_image.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
        #                                     QtWidgets.QSizePolicy.Expanding)

        start_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                   QtWidgets.QSizePolicy.Expanding)
        toggle_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                    QtWidgets.QSizePolicy.Expanding)
        reset_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        reflect_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                     QtWidgets.QSizePolicy.Expanding)
        rotate_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                    QtWidgets.QSizePolicy.Expanding)
        invert_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                    QtWidgets.QSizePolicy.Expanding)
        add_pattern_button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                         QtWidgets.QSizePolicy.Expanding)
        

        # Initial button states...
        toggle_button.setEnabled(False)
        reset_button.setEnabled(False)

        # Button functions...
        patterns_list.itemSelectionChanged.connect(lambda : selected_pattern_image.draw_pattern(patterns_list.selectedItems()))
        start_button.clicked.connect(lambda : self.start_sim(start_button,
                                                             toggle_button))
        toggle_button.clicked.connect(lambda : self.toggle_sim(toggle_button,
                                                               reset_button))
        reset_button.clicked.connect(lambda : self.reset_sim(start_button,
                                                             reset_button,
                                                             toggle_button))

        # Position dashboard items
        self.addWidget(start_button, *(0, 0, 1, 4))
        self.addWidget(toggle_button, *(1, 0, 1, 1))
        self.addWidget(reset_button, *(1, 1, 1, 3))
        self.addWidget(patterns_list, *(2, 0, 5, 1))
        self.addWidget(selected_pattern_image, *(2, 1, 1, 3))
        self.addWidget(label, *(3, 1, 1, 1))
        self.addWidget(editX, *(3, 2, 1, 1))
        self.addWidget(editY, *(3, 3, 1, 1))
        self.addWidget(reflect_button, *(4, 1, 1, 3))
        self.addWidget(rotate_button, *(5, 1, 1, 3))
        self.addWidget(invert_button, *(6, 1, 1, 3))
        self.addWidget(add_pattern_button, *(7, 0, 1, 4))

        self.setRowStretch(0, 1)
        self.setRowStretch(1, 1)
        self.setRowStretch(2, 3)
        self.setRowStretch(3, 1)
        self.setRowStretch(4, 2)
        self.setRowStretch(5, 2)
        self.setRowStretch(6, 2)
        self.setRowStretch(7, 2)
        self.setColumnStretch(1, 1)
        self.setColumnStretch(2, 1)
        self.setColumnStretch(3, 1)

    def start_sim(self, start_button, toggle_button):
        '''
        Begins timer for gameboard, with milliseconds.

        No inputs.

        No returns.
        '''
        self.timer.start(80)
        start_button.setEnabled(False)
        toggle_button.setEnabled(True)

        
    def toggle_sim(self, toggle_button, reset_button):
        '''
        Toggles pause / resume on gameboard grid.

        Inputs:
            gameboard (QtWidgets.QWidget): gameboard widget for simulation.

        No returns.
        '''
        timer = self.timer
        if timer.isActive():
            reset_button.setEnabled(True)
            timer.stop()
            toggle_button.setText('Resume')
        else:
            reset_button.setEnabled(False)
            timer.start()
            toggle_button.setText('Pause')


    def reset_sim(self, start_button, reset_button, toggle_button):
        '''
        Resets gameboard to initial seed.

        Inputs:
            start_button (QPushButton):
            reset_button (QPushButton):
            toggle_button (QPushButton):

        No returns.
        '''
        self.gameboard.game.reset()
        self.gameboard.update()
        reset_button.setEnabled(False)
        start_button.setEnabled(True)
        toggle_button.setText('Pause')
        toggle_button.setEnabled(False)

if __name__ == "__main__":
    pass
