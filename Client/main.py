# Client per il tracciamento degli effetti
# indesiderati delle vaccinazioni anti Covid-19

# Alvise Bacco
# 19/04/22

# Made with <3
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel,
                             QProgressBar, QCheckBox, QWidget)
from QLed import QLed
import requests


class DrawObj(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        # Applicazione grafica
        self.app = QApplication(sys.argv)

        # Led circolare rosso
        self.led_red = QLed(self, onColour=QLed.Red, shape=QLed.Circle)
        self.led_green = QLed(self, onColour=QLed.Green, shape=QLed.Circle)

    def __del__(self):
        sys.exit(self.app.exec())

    def get_connection_status(self, top: int, left: int, width: int, height: int, title: str) -> bool:
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.led_red.move(10, 50)
        self.led_red.value = True

        self.label = QLabel("<h5>Uploader utility<h5>", self)
        self.show()
        return True


if __name__ == '__main__':
    DrawObj().get_connection_status(1000, 100, 330, 250, 'Check database')
