# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import SrchRemWin as srw
import subprocess
class Ui_MainWindow(object):
    def openSrchRemWin(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=srw.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def searchRoom(self,room):
        con = cx_Oracle.connect('hr/hr@localhost/orcl')
        cur = con.cursor()
        query="select * from test where room_no="+int(room)
        self.tableWidget.setRowCount(1)
        rowdata=list()
        cur.execute(query)
        for x in cur:
            rowdata.append(x)
        col=None
        for x in cur:
            if x is not None:
                col=len(x)
                break
        cur=con.cursor()
        cur.execute(query)
        for y in range(col):
            self.tableWidget.setItem(1,y,QtWidgets.QTableWidgetItem(str(rowdata[1][y])))
        con.commit()
        con.close()

    def loadAvail(self):
        con = cx_Oracle.connect('hr/hr@localhost/orcl')
        cur = con.cursor()
        try:
            query="select count(*) from avail"
            cur.execute(query)
        except TypeError as e:
            pass
        else:
            print("Success!!!")
        rows=0
        for x in cur:
            if x is not None:
                rows=x[0]
        self.tableWidget.setRowCount(rows)
        try:
            query="insert into avail select available,room_no from test where available='y'"
            cur=con.cursor()
            cur.execute(query)
        except cx_Oracle.IntegrityError as e:
            pass
        else:
            pass
        query="select * from avail"
        cur = con.cursor()
        cur.execute(query)
        col=0
        for x in cur:
            if x is not None:
                col=len(x)
                break
        
        self.tableWidget.setColumnCount(col)
        print('rows=',rows)
        rowdata=list()
        query="select * from avail"
        cur = con.cursor()
        cur.execute(query)
        for x in cur:
            rowdata.append(x)
        for y in rowdata:
            print(y)
        
        for x in range(0,rows):
            for y in range(0,col):
                if y>=2:
                    rowdata[x][y]=None
                self.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(rowdata[x][y])))
        con.commit()
        con.close()
    def loadData(self):
        con = cx_Oracle.connect('hr/hr@localhost/orcl')
        cur = con.cursor()
        query="select count(*) from test"
        cur.execute(query)
        rows=0
        for x in cur:
            if x is not None:
                rows=x[0]
        try:
            self.tableWidget.setRowCount(rows)
        except TypeError as e:
            pass
        else:
            pass
        query="select * from test"
        cur = con.cursor()
        cur.execute(query)
        col=None
        for x in cur:
            if x is not None:
                col=len(x)
                break
        try:
            self.tableWidget.setColumnCount(col)
        except TypeError as e:
            pass
        else:
            pass         
        print('rows=',rows)
        rowdata=list()
        query="select * from test"
        cur = con.cursor()
        cur.execute(query)
        for x in cur:
            rowdata.append(x)
        for y in rowdata:
            print(y)
        
        for x in range(0,rows):
            for y in range(0,col):

                self.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(rowdata[x][y])))
                
        con.close()
    def run(self):
        subprocess.Popen('Matrix.bat', cwd=r'C:\Users\nimis\Desktop\dbms')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 581)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 821, 351))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 390, 761, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.loadData)
        
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_6.clicked.connect(self.run)
        
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openSrchRemWin)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 450, 761, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_4.clicked.connect(self.loadAvail)
        
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_New_Entry = QtWidgets.QAction(MainWindow)
        self.action_New_Entry.setObjectName("action_New_Entry")
        self.actionRemove_Entry = QtWidgets.QAction(MainWindow)
        self.actionRemove_Entry.setObjectName("actionRemove_Entry")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Room No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Floor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Available"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Entry Date/Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        self.pushButton_2.setText(_translate("MainWindow", "Reload"))
        self.pushButton_6.setText(_translate("MainWindow", "Add Customer"))
        self.pushButton.setText(_translate("MainWindow", "Remove/Search a Customer"))
        self.pushButton_4.setText(_translate("MainWindow", "Load avail_Rooms"))
        self.actionRemove_Entry.setToolTip(_translate("MainWindow", "Remove or Search a customer"))
        self.actionRemove_Entry.setShortcut(_translate("MainWindow", "Ctrl+R"))



import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())


