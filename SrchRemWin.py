# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\search_rem_win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
class Ui_MainWindow(object):
    def buttonClick_1(self):
        some_text=self.lineEdit.text()
        self.searchUser(some_text)
    def buttonClick_2(self):
        some_text=self.lineEdit_2.text()
        self.RemRoom(str(some_text))
    def searchUser(self,name_g):
        con = cx_Oracle.connect('hr/hr@localhost/orcl')
        cur = con.cursor()
        query="select count(*) from test where name="+"'"+name_g+"'"
        cur.execute(query)
        rows=0
        for x in cur:
            if x is not None:
                rows=x[0]
        self.tableWidget.setRowCount(rows)
        query="select * from test where name="+"'"+name_g+"'"
        rowdata=list()
        cur.execute(query)
        for x in cur:
            rowdata.append(x)
        print(rowdata)
        col=None
        query="select * from test where name="+"'"+name_g+"'"
        cur.execute(query)
        for x in cur:
            if x is not None:
                col=len(x)
                break
        query="select * from test where name="+"'"+name_g+"'"
        cur.execute(query)
        for x in range(rows):
            for y in range(col):
                self.tableWidget.setItem(x,y,QtWidgets.QTableWidgetItem(str(rowdata[x][y])))
        con.commit()
        con.close()
    def RemRoom(self,room):
        
        con = cx_Oracle.connect('hr/hr@localhost/orcl')
        cur = con.cursor()
        
        query="select phone from test where room_no="+str(int(room))
        print(query)
        cur=con.cursor()
        cur.execute(query)
        some_phone=0;
        for x in cur:
            for y in x:
                some_phone=y
        try:
            query2="update test set name=null,available='y', entry=null, phone=null where phone="+str(some_phone)
            cur=con.cursor()
            cur.execute(query2)
        except cx_Oracle.DatabaseError as e:
            pass
        query="update customer set exit=sysdate where phone="+str(int(some_phone))
        cur=con.cursor()
        cur.execute(query)
        query="update customer set cost=(exit-entry)*1000 where phone="+str(int(some_phone))
        cur=con.cursor()
        cur.execute(query)
        query3="insert into avail(available, room_no) select available, room_no from test where room_no="+str(int(room))
        cur=con.cursor()
        cur.execute(query3)
        con.commit()
        cur.close()
        con.close()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 791, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
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
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 280, 211, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 280, 191, 51))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.buttonClick_1)
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 340, 191, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.buttonClick_2)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 340, 211, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        item.setText(_translate("MainWindow", "Entry"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phone"))
        
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Room No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

