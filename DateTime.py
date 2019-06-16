#This doesnot include any GUI programming
from PyQt5.QtCore import QDateTime,QTime,Qt,QDate

datetime = QDateTime.currentDateTime()
print("_______________________________")
print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print("_______________________________")



date = QDate.currentDate()
print("_______________________________")
print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))
print("_______________________________")


time = QTime.currentTime()
print("_______________________________")
print(time.toString())

print(time.toString(Qt.DefaultLocaleLongDate))
print("_______________________________")


#The UTC time:


datetime = QDateTime.currentDateTime()
print("Local Date and Time is " + datetime.toString(Qt.DefaultLocaleLongDate))
print("The UTC time is" + datetime.toUTC().toString())
print("The offset from UTC is {0} seconds".format(datetime.offsetFromUtc()))

