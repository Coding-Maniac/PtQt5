from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
from PyQt5.QtCore import QRect



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "My Window"
        top =100
        left = 100
        width =680
        height = 500
        self.setWindowIcon(QtGui.QIcon("mass.png"))
        self.setWindowTitle(title)
        self.setGeometry(top,left,width,height)
        self.UIcomp()
        self.show()
