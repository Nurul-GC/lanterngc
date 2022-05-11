from random import randint
from sys import argv
from time import sleep

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from lgcmain import LGC


class LGCINIT:
    def __init__(self):
        self.gc = QApplication(argv)

        # application font
        QFontDatabase.addApplicationFont("./lgc-fonts/Kranky.ttf")

        img = QPixmap("./lgc-icons/init.png")
        self.align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignAbsolute)
        self.color = Qt.GlobalColor.white
        self.janela = QSplashScreen(img)
        self.janela.setStyleSheet('font-family: "Kranky";'
                                  'font-size: 11pt;')
        self.janela.show()
        self.iniciar()

    def iniciar(self):
        load = 0
        while load < 100:
            self.janela.showMessage(f"Loading Package: {load}%", self.align, self.color)
            sleep(0.3)
            load += randint(5, 10)
        self.janela.close()
        app = LGC()
        app.ferramentas.show()


if __name__ == '__main__':
    lgcApp = LGCINIT()
    lgcApp.gc.exec()
