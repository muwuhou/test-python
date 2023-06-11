
import sys
import random
from functools import cache
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor, QPaintEvent, QPainter, QPen
from PyQt6.QtCore import QSize


@cache
def get_palette(color):
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(color))
    return palette

def get_pen(color, width):
    pen = QPen(QColor(color))
    pen.setWidth(width)
    return pen

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

class MyDrawing(QWidget):
    def paintEvent(self, event: QPaintEvent):
        qp = QPainter(self)
        size = self.size()
        hi = size.height()
        wi = size.width()

        # Draw a box
        qp.setPen(get_pen("red", 1))
        qp.drawRect(2, 2, wi - 4, hi - 4)

        # Draw some random points
        qp.setPen(get_pen("blue", 10))
        for i in range(0, 10):
            qp.drawPoint(random.randint(2, wi-4), random.randint(2, hi-4))

    def sizeHint(self) -> QSize:
        return QSize(100, 100)


def test1():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("My shining app")
    layout = QVBoxLayout()

    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.TabPosition.West)
    tabs.setMovable(True)
    colors = ["red", "green", "blue", "yellow"]
    for color in colors:
        tabs.addTab(Grid(colors), color)

    layout.addWidget(tabs)
    layout.addWidget(QPushButton("One"))
    repaint_button = QPushButton("Repaint")
    layout.addWidget(repaint_button)
    mydrawing = MyDrawing()
    layout.addWidget(mydrawing)

    window.setLayout(layout)

    repaint_button.clicked.connect(mydrawing.update)

    window.show()
    # Start the event loop.
    app.exec()

test1()
