import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from mainUi import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.CanDraw = False

    def paintEvent(self, event):
        if self.CanDraw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for i in range(10):
                m = random.randint(20, 200)
                qp.drawEllipse(random.randint(0, 600), random.randint(0, 500), m, m)
            qp.end()

    def run(self):
        self.CanDraw = True
        self.repaint()
        self.CanDraw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
