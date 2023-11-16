from PyQt5.QtWidgets import QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setGeometry(300, 300, 800, 700)
        self.pushButton = QPushButton("Создать", self)
        self.pushButton.resize(100, 50)
        self.pushButton.move(350, 350)
