import webbrowser
from sys import argv, exit

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class GCL:
    def __init__(self):
        self.gc = QApplication(argv)
        QFontDatabase.addApplicationFont('fonts/Kranky.ttf')

        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle('GC-lantern')
        self.ferramentas.setWindowState(Qt.WindowState.WindowMaximized)
        self.ferramentas.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint)
        self.ferramentas.setStyleSheet(temaescuro)

        self.layout = QVBoxLayout()

        menu = QMenuBar()
        detalhes = menu.addMenu('Details')
        instr = detalhes.addAction('Instructions')
        instr.triggered.connect(self._instr)
        detalhes.addSeparator()
        sair = detalhes.addAction('Exit')
        sair.triggered.connect(self._sair)
        sobre = menu.addAction('About')
        sobre.triggered.connect(self._sobre)
        self.layout.setMenuBar(menu)
        self.ferramentas.setLayout(self.layout)

        self.principal()

        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none;" href="#">&trade; ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")
        barramenu = QToolBar("Copyright")
        barramenu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        barramenu.addWidget(copyrightlabel)
        self.layout.addWidget(barramenu)

    def principal(self):
        def ligar():
            if lantern_btn.isChecked():
                lantern_btn.setText('OFF')
                self.ferramentas.setStyleSheet(temaclaro)
            else:
                lantern_btn.setText('ON')
                self.ferramentas.setStyleSheet(temaescuro)

        frame = QFrame()
        layout = QVBoxLayout()

        lantern_btn = QPushButton('ON')
        lantern_btn.setFixedHeight(550)
        lantern_btn.setAutoExclusive(True)
        lantern_btn.setCheckable(True)
        lantern_btn.clicked.connect(ligar)
        layout.addWidget(lantern_btn)

        frame.setLayout(layout)
        self.layout.addWidget(frame)

    def _sobre(self):
        QMessageBox.information(self.ferramentas, 'About', '''<h2>Information about the Program</h2><hr>
        Name: <b>GC-lantern (GCL)</b><br>
        Version: <b>0.1-042022</b><br>
        Programmer & Designer: <b>Nurul-GC</b><br>
        Company: <b>ArtesGC, Inc.</b>''')

    def _instr(self):
        QMessageBox.information(self.ferramentas, 'Instructions', '''<h2>Quick Presentation</h2><hr>
        <p>Hello Dear User!<br>
        I present to you a very practical and useful tool,
        a program that works as a lantern on your desktop/tablet PC..</p>
        <p>It's easy to be used, you just need to push the button and it will change his theme,
        helping you to see what's around you!</p>
        <p>Thanks for your support!<br>
        <b>&trade;ArtesGC, Inc.</b></p>''')

    def _sair(self):
        pergunta = QMessageBox.question(self.ferramentas, 'Confirm Exit', 'Do you really want to close the program?')
        if pergunta == pergunta.Yes:
            exit(0)


if __name__ == '__main__':
    temaescuro = open('theme/dark.qss').read().strip()
    temaclaro = open('theme/light.qss').read().strip()
    app = GCL()
    app.ferramentas.show()
    app.gc.exec()
