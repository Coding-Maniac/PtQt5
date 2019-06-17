from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
from PyQt5.QtCore import QRect
from Pyqt5 import Qtcore



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
        
        
        #This function is used to create the button
        def UIcomp(self):
        button =QPushButton("CLICK ME",self) #The text inside is displayed in the button
        button.move(100,100)
        #button.setGeometry(QRect(100,100,111,30)) #This is used to set the size of the  button
        button.setIcon(QtGui.QIcon("icon.png")) #The file needs to be in the same folder
        
        
        
if __name__ == "__main__":             
    App = QApplication(sys.argv)
    window =Window()
    sys.exit(App.exec())
