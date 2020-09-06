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
        for index in range(10):
            painter.drawRect(0 + index*100, 0, 100, 100)
        painter.end()

class Dashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.grid = self.make_grid()

    def make_grid(self):
        grid = QtWidgets.QGridLayout()
        #self.setLayout(grid)

        patterns = QtWidgets.QListWidget()
        label = QtWidgets.QLabel('Location:')
        label.setAlignment(QtCore.Qt.AlignCenter)
        edit = QtWidgets.QLineEdit()
        selected_pattern_image = QtWidgets.QLabel('Test, Replace with QWidget')
        start_button = QtWidgets.QPushButton('Start')
        pause_button = QtWidgets.QPushButton('Pause')
        reset_button = QtWidgets.QPushButton('Reset')

        grid.addWidget(patterns, *(0, 0, 2, 1))
        grid.addWidget(label, *(0, 1, 1, 1))
        grid.addWidget(edit, *(1, 1, 1, 1))
        grid.addWidget(selected_pattern_image, *(2, 0, 3, 1))
        grid.addWidget(start_button, *(2, 1, 1, 1))
        grid.addWidget(pause_button, *(3, 1, 1, 1))
        grid.addWidget(reset_button, *(4, 1, 1, 1))
        return grid
        

if __name__ == "__main__":
    #gui = App()

    app = QtWidgets.QApplication([])

    ## Using grid layouts
    widget = QtWidgets.QWidget()
    grid = QtWidgets.QGridLayout()
    widget.setLayout(grid)
    label = QtWidgets.QLabel('Game of Life')
    label.setAlignment(QtCore.Qt.AlignCenter)
    grid.addWidget(label, 0, 0, 1, 2)
    dashboard_widget = Dashboard()
    print("Dashboard geom: %s" % dashboard_widget.frameGeometry())
    grid.addWidget(dashboard_widget, 1, 1, 10, 1)
    #grid.addLayout(dashboard_widget.grid, 1, 1, 10, 1)
    gameboard_widget = GameBoard()
    grid.addWidget(gameboard_widget, 1, 0, 10, 1)
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
