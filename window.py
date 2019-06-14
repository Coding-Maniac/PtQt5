#This code helps in creating a dialog box with an icon
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "My Window"
        self.top =100                     
        self.left = 100
        self.width =680
        self.height = 500
        self.InitWindow()
        self.setWindowIcon(QtGui.QIcon("mass.png"))           #This is used for setting an icon.You should have the file stored in your project folder

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height) 
        self.show()
App = QApplication(sys.argv)
window =Window()
sys.exit(App.exec())
