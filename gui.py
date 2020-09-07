#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        self.application_manager = QtWidgets.QApplication([])
        super().__init__()
        self.grid = QtWidgets.QGridLayout()
        self.showMaximized()

    def run(self):
        self.application_manager.exec_()

    #def paintEvent(self, event):
    #    painter = QtGui.QPainter()
    #    painter.begin(self)
    #    painter.setBrush(QtGui.QColor(200,0,0))
    #    painter.drawRect(0, 0, 100, 100)
    #    painter.drawRect(100, 0, 100,100)
    #    painter.end()

class GameBoard(QtWidgets.QWidget):
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
    def __init__(self):
        super().__init__()
        self.make_grid()

    def make_grid(self):
        patterns = QtWidgets.QLabel('Make a list...') #patterns = QtWidgets.QListWidget()
        label = QtWidgets.QLabel('Location:')
        label.setAlignment(QtCore.Qt.AlignCenter)
        edit = QtWidgets.QLabel('Make an edit..') #edit = QtWidgets.QLineEdit()
        selected_pattern_image = QtWidgets.QLabel('Test, Replace with QWidget')
        start_button = QtWidgets.QPushButton('Start')
        pause_button = QtWidgets.QPushButton('Pause')
        reset_button = QtWidgets.QPushButton('Reset')

        self.addWidget(patterns, *(0, 0, 2, 1))
        self.addWidget(label, *(0, 1, 1, 1))
        self.addWidget(edit, *(1, 1, 1, 1))
        self.addWidget(selected_pattern_image, *(2, 0, 3, 1))
        self.addWidget(start_button, *(2, 1, 1, 1))
        self.addWidget(pause_button, *(3, 1, 1, 1))
        self.addWidget(reset_button, *(4, 1, 1, 1))
        

if __name__ == "__main__":
    #gui = App()

    app = QtWidgets.QApplication([])

    ## Nest grid inside HBox
    #widget = QtWidgets.QWidget()
    #v_layout = QtWidgets.QHBoxLayout()
    #grid = QtWidgets.QGridLayout()
    #button_0 = QtWidgets.QPushButton('0')
    #button_1 = QtWidgets.QPushButton('1')
    #grid.addWidget(button_0, *(0, 0))
    #grid.addWidget(button_1, *(1, 0))
    #v_layout.addLayout(grid)
    #button_2 = QtWidgets.QPushButton('2')
    #v_layout.addWidget(button_2)
    #widget.setLayout(v_layout)
    #widget.showMaximized()

    ## Using grid layouts
    widget = QtWidgets.QWidget()
    h_layout = QtWidgets.QHBoxLayout()
    #label = QtWidgets.QLabel('Game of Life')
    #label.setAlignment(QtCore.Qt.AlignCenter)
    #grid.addWidget(label, 0, 0, 1, 2)
    #grid.addLayout(dashboard_widget.grid, 1, 1, 10, 1)
    gameboard_widget = GameBoard()
    h_layout.addWidget(gameboard_widget, 3)
    dashboard_grid = Dashboard()
    h_layout.addLayout(dashboard_grid, 1)
    widget.setLayout(h_layout)
    widget.showMaximized()

    ## Using VBox, HBox layouts
    #nested_widget = QtWidgets.QWidget()
    #nested_layout = QtWidgets.QHBoxLayout()
    #button_label = QtWidgets.QLabel('Button: ')
    #button_label.setAlignment(QtCore.Qt.AlignCenter)
    #button = QtWidgets.QPushButton('Select')
    #button.clicked.connect(lambda : print('Button pressed.'))
    #nested_layout.addWidget(button_label, 10)
    #nested_layout.addWidget(button, 1)
    #nested_widget.setLayout(nested_layout)

    #widget = QtWidgets.QWidget()
    #title_label = QtWidgets.QLabel('Game of Life GUI')
    #title_label.setAlignment(QtCore.Qt.AlignCenter)
    #layout = QtWidgets.QVBoxLayout()
    #layout.addWidget(title_label, 1)
    #layout.addWidget(nested_widget, 20)
    #widget.setLayout(layout)
    #widget.showMaximized()
    
    app.exec_()
    
    ##gui.run()
