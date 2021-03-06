from sys import argv, exit
import webbrowser

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

temaescuro = open('lgc-theme/dark.qss').read().strip()
temaclaro = open('lgc-theme/light.qss').read().strip()


class LGC:
    def __init__(self):
        # main-window-widget
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle('LanternGC')
        self.ferramentas.setWindowState(Qt.WindowState.WindowMaximized)
        self.ferramentas.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint)
        self.ferramentas.setStyleSheet(temaescuro)

        # main-layout
        self.layout = QFormLayout()
        self.layout.setSpacing(10)

        # menu-bar
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

        # main-button-function
        def ligar():
            if self.lantern_btn.isChecked():
                self.ferramentas.setStyleSheet(temaclaro)
            else:
                self.ferramentas.setStyleSheet(temaescuro)

        self.lantern_btn = QPushButton()
        self.lantern_btn.setFixedHeight(550)
        self.lantern_btn.setCheckable(True)
        self.lantern_btn.setStyleSheet('''
        background-image: url("./lgc-icons/lantern.png");
        background-repeat: no-repeat;
        background-size: auto;
        background-attachment: fixed;
        background-position: center;
        ''')
        self.lantern_btn.clicked.connect(ligar)
        self.layout.addRow(self.lantern_btn)

        # copyright-label
        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none; background-color: none;" href="#">&trade;ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")

        barramenu = QToolBar("Copyright")
        barramenu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        barramenu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        barramenu.addWidget(copyrightlabel)
        self.layout.addRow(barramenu)

    # menu-bar-functions
    def _sobre(self):
        QMessageBox.information(self.ferramentas, 'About', '''<h2>Information about the Program</h2><hr>
        Name: <b>GC-lantern (LGC)</b><br>
        Version: <b>0.2-062022</b><br>
        Programmer & Designer: <b>Nurul-GC</b><br>
        Company: <b>ArtesGC, Inc.</b>''')

    def _instr(self):
        QMessageBox.information(self.ferramentas, 'Instructions', '''<h2>Quick Presentation</h2><hr>
        <p>Hello Dear User!<br>
        I present to you a very practical and useful tool,
        a program that works as a lantern on your desktop/tablet PC..</p>
        <p>It's easy to be used, you just need to push the button and it will change his lgc-theme,
        helping you to see what's around you!</p>
        <p>Thanks for your support!<br>
        <b>&trade;ArtesGC, Inc.</b></p>''')

    def _sair(self):
        if self.lantern_btn.isChecked():
            pergunta = QMessageBox.question(self.ferramentas, 'Confirm Exit', '<b>Do you really want to close the program?</b>')
            if pergunta == pergunta.Yes:
                return exit(0)
        else:
            return exit(0)
