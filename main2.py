import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QThread
import mysql.connector
import pyodbc
import json

tables = []
numbers = []
mytables = []
sqltables = []


class replicador(QThread):
    def __init__(self, sqldict, mysqldict):
        QThread.__init__(self)
        self.sqldict = sqldict
        self.mysqldict = mysqldict

    def __del__(self):
        pass

    def run(self):
        global mytables
        global sqltables
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
            print("iteracion :v")
            global mytables
            global sqltables
            sqlcursor.execute("SELECT * FROM MASTER_LOG where bandera <> 1")
            results = sqlcursor.fetchall()
            # el cero id del cambio
            # el uno nuestro tipo
            # el dos es nuestra tabla
            # el  tres es nuestra bandera
            # el cuatro es nuestro id modificado
            for tabla in results:
                if tabla[2].lower() in map(lambda a: a.lower(), mytables):
                    if tabla[1].lower() == "delete".lower() and tabla[3] == False:
                        sqlcursor.execute(
                            "SELECT COLUMN_NAME FROM "+str(self.sqldict['nombredb'])+".INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME LIKE '"+str(tabla[2])+"' AND CONSTRAINT_NAME LIKE 'PK%'")
                        resultado = sqlcursor.fetchall()[0]
                        pk = resultado[0]
                        try:
                            mycursor.execute(
                                "delete from "+tabla[2]+" where "+pk+" = "+str(tabla[4]))
                            mysqlcon.commit()
                            sqlcursor.execute(
                                "UPDATE MASTER_LOG SET bandera=1 where id="+str(tabla[0]))
                            sqlcon.commit()
                        except Exception as e:
                            print(e)
                    elif tabla[1].lower() == "update".lower() and tabla[3] == False:

                        sqlcursor.execute(
                            "SELECT COLUMN_NAME FROM "+str(self.sqldict['nombredb'])+".INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME LIKE '"+str(tabla[2])+"' AND CONSTRAINT_NAME LIKE 'PK%'")
                        resultado = sqlcursor.fetchall()[0]
                        pk = resultado[0]
                        sqlcursor.execute(
                            "SELECT * FROM ["+str(tabla[2]+"] where "+pk+" = '"+tabla[4])+"'")
                        valores = sqlcursor.fetchone()
                        sqlcursor.execute("SELECT COLUMN_NAME FROM " +
                                          self.sqldict["nombredb"]+".INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+str(tabla[2])+"'")
                        columnas = sqlcursor.fetchall()
                        columnas = map(lambda a: a[0], columnas)

                    elif tabla[1].lower() == "insert".lower() and tabla[3] == False:
                        sqlcursor.execute(
                            "SELECT COLUMN_NAME FROM "+str(self.sqldict['nombredb'])+".INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME LIKE '"+str(tabla[2])+"' AND CONSTRAINT_NAME LIKE 'PK%'")
                        resultado = sqlcursor.fetchall()[0]
                        pk = resultado[0]
                        print(
                            "SELECT * FROM ["+str(tabla[2]+"] where "+pk+" = '"+tabla[4])+"'")
                        sqlcursor.execute(
                            "SELECT * FROM ["+str(tabla[2]+"] where "+pk+" = '"+tabla[4])+"'")
                        valores = sqlcursor.fetchone()
                        sqlcursor.execute("SELECT COLUMN_NAME FROM " +
                                          self.sqldict["nombredb"]+".INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='"+str(tabla[2])+"'")
                        columnas = sqlcursor.fetchall()
                        columnas = map(lambda a: a[0], columnas)
                        values = "("
                        for i in range(len(valores)):
                            if i != len(valores)-1:
                                values += "%s,"
                            else:
                                values += "%s)"
                        columns = "("
                        for i in range(len(columnas)):
                            if i != len(valores)-1:
                                columns += columnas[i]+","
                            else:
                                columns += columnas[i]+")"
                        try:
                            mycursor.execute(
                                "INSERT INTO `"+str(tabla[2])+"` "+columns+" VALUES "+values, list(valores))
                            mysqlcon.commit()
                            sqlcursor.execute(
                                "UPDATE MASTER_LOG SET bandera=1 where id="+str(tabla[0]))
                            sqlcon.commit()
                        except Exception as e:
                            print(e)

                else:
                    continue
            self.sleep(2)


class Main2Window(QtGui.QMainWindow):
    def run_repli(self):
        if not self.rep.isRunning():
            self.rep.start()

    def replicar(self):
        global mytables
        global sqltables
        tabla = str(self.replica_list.selectedItems()[0].text())
        self.replicando_list.clear()
        if tabla not in mytables:
            mytables.append(tabla)
        self.replica_list.clear()
        sqltables.remove(tabla)
        sqltables = sorted(sqltables)
        mytables = sorted(mytables)
        self.replica_list.addItems(sqltables)
        self.replicando_list.addItems(mytables)

    def desreplicar(self):
        global mytables
        global sqltables
        tabla = str(self.replicando_list.selectedItems()[0].text())
        self.replica_list.clear()
        if tabla not in sqltables:
            sqltables.append(tabla)
        self.replicando_list.clear()
        mytables.remove(tabla)
        mytables = sorted(mytables)
        sqltables = sorted(sqltables)
        self.replicando_list.addItems(mytables)
        self.replica_list.addItems(sqltables)

    def __init__(self, sqldict, mysqldict):
        super(Main2Window, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main2.ui", self)
        global mytables
        global sqltables
        self.rep = replicador(sqldict, mysqldict)
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
            sqltables = self.sqlcursor.fetchall()
            for i in range(len(sqltables)):
                sqltables[i] = str(sqltables[i][0])
            sqltables.remove('MASTER_LOG')
            sqltables = sorted(sqltables)
            self.replica_list.addItems(sqltables)
            self.derecha_botton.clicked.connect(self.replicar)
            self.izquierda_botton.clicked.connect(self.desreplicar)
        except Exception as e:
            print "exception"
            print(e)

        self.guardar_botton.clicked.connect(self.run_repli)
