# Client per il tracciamento degli effetti
# indesiderati delle vaccinazioni anti Covid-19

# Alvise Bacco
# 19/04/22

# Made with <3
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel,
                             QProgressBar, QCheckBox)


class Login(QMainWindow):
    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()

        """"Nel costruttore della classe definisco come verra' creata la finestra"""

        self.title = 'Login'

        self.top = 1000
        self.left = 100
        self.width = 330
        self.height = 250
        self.login_window()
        self.main_window()
        sys.exit(app.exec())

    def login_window(self):
        # self.label.move(10, 10)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def main_window(self):
        self.setWindowTitle('Main Windows')


if __name__ == '__main__':
    Login()
