from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
from PyQt5.QtCore import QRect
from Pyqt5 import Qtcore


#___________________________________________________________________________________________________________________________
#This function is used to create a window
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
        self.createbtn()
        self.trybtn()
        self.show()
 #_______________________________________________________________________________________________________________________________
        
        
        #This function is used to create the button
        def UIcomp(self):
            button =QPushButton("CLICK ME",self) #The text inside is displayed in the button
            button.move(100,100)
            #button.setGeometry(QRect(100,100,111,30)) #This is used to set the size of the  button
            button.setIcon(QtGui.QIcon("icon.png")) #The file needs to be in the same folder
            button.setIcon(QtCore.Qsize(40,40))
            button.setToolTip("<h2>This is a click me button<h2>")  #You can also use header sizes for the tooltip

        
        
        def CreateBtn(self):
            button=QPushButton("Click To Quit",self)
            button.move(200,200)
            button.setToolTip("<h1>Gud Bye User</h1>")
            button.clicked.connect(self.exitme)
        
        
        
        def exitme(self):
            sys.exit()
        
        
        
        def trybtn(self):
            a = 2
            b = 3
            c = str(a + b)
            button = QPushButton(c,self)
            button.move(300,300)


        
        
if __name__ == "__main__":             
    App = QApplication(sys.argv)
    window =Window()
    sys.exit(App.exec())
