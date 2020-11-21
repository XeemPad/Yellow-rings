import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 600, 520)
        self.setWindowTitle('Жёлтые круги')

        self.do_paint = False
        self.startButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_rings(qp)
            qp.end()

    def draw_rings(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for _ in range(10):
            x, y = randint(0, 580), randint(0, 500)
            d = randint(5, 100)
            while x + d > 600 or y + d > 520:
                x, y = randint(0, 580), randint(0, 500)
                d = randint(5, 100)
            qp.drawEllipse(x, y, d, d)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Widget()
    window.show()

    sys.exit(app.exec())