from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication
import sys
# import os
from PyQt5 import QtWidgets, QtGui,QtCore,uic
sys.path.append("ui")
import mysql.connector
# from wid_login import Ui_MainWindow
from auth import Ui_mainWindow
from PyQt5.QtCore import pyqtSignal, QObject
 
 

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
    #    
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())

# app = QtWidgets.QApplication([])
# win = uic.loadUi("my_design.ui") # расположение вашего файла .ui
 
# win.show()
# sys.exit(app.exec())

# def dbcon():
#     db = QSqlDatabase.addDatabase('QMYSQL')
#     db.setHostName('localhost')
#     db.setDatabaseName('vista')
#     db.setUserName('root')
#     db.setPassword('root')
#     ok = db.open()
#     if not ok: print(db.lastError().text())
#     else: print("connected")
#     query = QSqlQuery(db)
#     query.exec_('SELECT * FROM tbl_Customers')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dbcon()
