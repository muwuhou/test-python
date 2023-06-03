
import sys
import random
from functools import cache
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor


@cache
def get_palette(color):
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(color))
    return palette

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setPalette(get_palette(color))
        self.setAutoFillBackground(True)

class Grid(QWidget):
    def __init__(self, colors):
        super(Grid, self).__init__()
        colors_copy = list(colors)
        random.shuffle(colors_copy)
        layout = QGridLayout()
        for i in range(0, len(colors_copy)):
            layout.addWidget(Color(colors_copy[i]), i // 2, i % 2)
        self.setLayout(layout)


def test1():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("My shining app")
    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.TabPosition.West)
    tabs.setMovable(True)
    colors = ["red", "green", "blue", "yellow"]
    for color in colors:
        tabs.addTab(Grid(colors), color)

    window.setCentralWidget(tabs)

    window.show()
    # Start the event loop.
    app.exec()

test1()
