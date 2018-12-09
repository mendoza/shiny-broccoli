import sys
from PyQt4 import QtCore, QtGui, uic
import mysql.connector
import pyodbc
import json


class Main2Window(QtGui.QMainWindow):
    def __init__(self, sqldict, mysqldict):
        super(Main2Window, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main2.ui", self)
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
            self.mycursor = self.mysqlcon.cursor()
            self.mycursor.execute("show tables;")
            myresult = self.mycursor.fetchall()
            for i in range(len(myresult)):
                myresult[i] = str(myresult[i][0])
            self.replicando_list.addItems(myresult)
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
