import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QThread, SIGNAL
import mysql.connector
import pyodbc
import json

tables = []
numbers = []


class replicador(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        i = 0
        while True:
            print("hello" + str(i))
            i += 1
            for i in range(len(tables)):
                print(i)
            self.sleep(2)


class Main2Window(QtGui.QMainWindow):
    def run_repli(self):
        if not self.rep.isRunning():
            self.rep.start()

    def __init__(self, sqldict, mysqldict):
        super(Main2Window, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main2.ui", self)
        self.rep = replicador()
        try:
            self.sqlcon = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                + sqldict["server"]
                + ";DATABASE="
                + sqldict["nombredb"]
                + ";UID="
                + sqldict["user"]
                + ";PWD="
                + sqldict["password"]
            )
            self.sqlcursor = self.sqlcon.cursor()
            self.mysqlcon = mysql.connector.connect(
                host=mysqldict["server"],
                port=mysqldict["puerto"],
                user=mysqldict["user"],
                passwd=mysqldict["password"],
                database=mysqldict["nombredb"],
            )
            self.sqlcursor.execute(
                "SELECT TABLE_NAME FROM "
                + sqldict["nombredb"]
                + " .INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
            )
            myresult = self.sqlcursor.fetchall()
            for i in range(len(myresult)):
                myresult[i] = str(myresult[i][0])
            self.replica_list.addItems(myresult)

        except:
            pass

        self.guardar_botton.clicked.connect(self.run_repli)
