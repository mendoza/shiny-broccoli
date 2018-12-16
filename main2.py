import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QThread
import mysql.connector
import pyodbc
import json

tables = []
numbers = []


class replicador(QThread):
    def __init__(self, sqldict, mysqldict):
        QThread.__init__(self)
        self.sqldict = sqldict
        self.mysqldict = mysqldict

    def __del__(self):
        pass

    def run(self):
        sqlcon = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + self.sqldict["server"]
            + ";DATABASE="
            + self.sqldict["nombredb"]
            + ";UID="
            + self.sqldict["user"]
            + ";PWD="
            + self.sqldict["password"]
        )
        mysqlcon = mysql.connector.connect(
            host=self.mysqldict["server"],
            port=self.mysqldict["puerto"],
            user=self.mysqldict["user"],
            passwd=self.mysqldict["password"],
            database=self.mysqldict["nombredb"],
        )
        sqlcursor = sqlcon.cursor()
        mycursor = mysqlcon.cursor()
        while True:
            sqlcursor.execute("SELECT * FROM MASTER_LOG")
            results = sqlcursor.fetchall()
            print(len(results))
            self.sleep(2)


class Main2Window(QtGui.QMainWindow):
    def run_repli(self):
        if not self.rep.isRunning():
            self.rep.start()

    def replicar(self):
        tabla = str(self.replica_list.selectedItems()[0].text())
        self.replicando_list.clear()
        if tabla not in self.mytables:
            self.mytables.append(tabla)
        self.replica_list.clear()
        self.sqltables.remove(tabla)
        self.sqltables = sorted(self.sqltables)
        self.mytables = sorted(self.mytables)
        self.replica_list.addItems(self.sqltables)
        self.replicando_list.addItems(self.mytables)

    def desreplicar(self):
        tabla = str(self.replicando_list.selectedItems()[0].text())
        self.replica_list.clear()
        if tabla not in self.sqltables:
            self.sqltables.append(tabla)
        self.replicando_list.clear()
        self.mytables.remove(tabla)
        self.mytables = sorted(self.mytables)
        self.sqltables = sorted(self.sqltables)
        self.replicando_list.addItems(self.mytables)
        self.replica_list.addItems(self.sqltables)

    def __init__(self, sqldict, mysqldict):
        super(Main2Window, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main2.ui", self)
        self.rep = replicador(sqldict, mysqldict)
        self.mytables = []
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
                + ".INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
            )
            self.sqltables = self.sqlcursor.fetchall()
            for i in range(len(self.sqltables)):
                self.sqltables[i] = str(self.sqltables[i][0])
            self.sqltables.remove('MASTER_LOG')
            self.sqltables = sorted(self.sqltables)
            self.replica_list.addItems(self.sqltables)
            self.derecha_botton.clicked.connect(self.replicar)
            self.izquierda_botton.clicked.connect(self.desreplicar)
        except Exception as e:
            print "exception"
            print(e)

        self.guardar_botton.clicked.connect(self.run_repli)
