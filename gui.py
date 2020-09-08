#!/usr/bin/env python3

from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        self.application_manager = QtWidgets.QApplication([])
        super().__init__()
        self.build()
        self.showMaximized()

    def build(self):
        toplevel_layout = QtWidgets.QHBoxLayout()
        self.setLayout(toplevel_layout)

        gameboard = GameBoard()
        dashboard_grid = Dashboard(toplevel_layout)

        GAMEBOARD_STRETCH = 3
        toplevel_layout.addWidget(gameboard, GAMEBOARD_STRETCH)

    def run(self):
        self.application_manager.exec_()
 

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
    def __init__(self, parent):
        super().__init__()
        DASHBOARD_STRETCH = 1
        parent.addLayout(self, DASHBOARD_STRETCH)
        self.make_grid()

    def make_grid(self):
        patterns = QtWidgets.QListWidget()
        label = QtWidgets.QLabel('Location:')
        label.setAlignment(QtCore.Qt.AlignCenter)
        edit = QtWidgets.QLineEdit()
        selected_pattern_image = QtWidgets.QWidget()
        start_button = QtWidgets.QPushButton('Start')
        pause_button = QtWidgets.QPushButton('Pause')
        reset_button = QtWidgets.QPushButton('Reset')

        self.addWidget(patterns, *(0, 0, 2, 1))
        self.addWidget(selected_pattern_image, *(0, 1, 1, 2))
        self.addWidget(label, *(1, 1, 1, 1))
        self.addWidget(edit, *(1, 2, 1, 1))
        self.addWidget(start_button, *(2, 0, 2, 1))
        self.addWidget(pause_button, *(2, 1, 1, 2))
        self.addWidget(reset_button, *(3, 1, 1, 2))
        

if __name__ == "__main__":
    gui = App()
    gui.run()
