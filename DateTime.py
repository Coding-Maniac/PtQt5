#This doesnot include any GUI programming
from PyQt5.QtCore import QDateTime,QTime,Qt,QDate

datetime = QDateTime.currentDateTime()

print("_______________________________")
print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print("_______________________________")

