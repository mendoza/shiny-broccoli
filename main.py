import sys
from PyQt4 import QtCore, QtGui, uic
import mysql.connector
import pyodbc
from main2 import Main2Window


class MainWindow(QtGui.QMainWindow):
    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(
            self, "Open file", "", "*.rpc")
        if filename != "":
            with open(str(filename), "r") as file:
                lineO = file.readline()
                lineD = file.readline()
                lineO = lineO.replace("\n", "")
                lineD = lineD.replace("\n", "")
                lineO = lineO.split("|")
                lineD = lineD.split("|")
                self.instanciaO_edit.setText(lineO[0])
                self.nombreO_edit.setText(lineO[1])
                self.puertoO_edit.setText(lineO[2])
                self.usuarioO_edit.setText(lineO[3])
                self.passwordO_edit.setText(lineO[4])
                self.instanciaD_edit.setText(lineD[0])
                self.nombreD_edit.setText(lineD[1])
                self.puertoD_edit.setText(lineD[2])
                self.usuarioD_edit.setText(lineD[3])
                self.passwordD_edit.setText(lineD[4])
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("El archivo debe existir")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            if msg.exec_():
                pass

    def save_file(self):
        filename = QtGui.QFileDialog.getSaveFileName(
            self, "Save file", "", "*.rpc")
        if str(filename) != "":
            if not str(filename).endswith(".rpc"):
                filename = str(filename) + ".rpc"
            with open(str(filename), "w") as file:
                file.write(
                    str(self.instanciaO_edit.text())
                    + "|"
                    + str(self.nombreO_edit.text())
                    + "|"
                    + str(self.puertoO_edit.text())
                    + "|"
                    + str(self.usuarioO_edit.text())
                    + "|"
                    + str(self.passwordO_edit.text())
                    + "\n"
                )
                file.write(
                    str(self.instanciaD_edit.text())
                    + "|"
                    + str(self.nombreD_edit.text())
                    + "|"
                    + str(self.puertoD_edit.text())
                    + "|"
                    + str(self.usuarioD_edit.text())
                    + "|"
                    + str(self.passwordD_edit.text())
                    + "\n"
                )
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("El archivo debe tener nombre")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            if msg.exec_():
                pass

    def try_mysql(self):
        try:
            server = "localhost"
            puerto = str(self.puertoD_edit.text())
            databases = str(self.nombreD_edit.text())
            username = str(self.usuarioD_edit.text())
            password = str(self.passwordD_edit.text())
            mydb = mysql.connector.connect(
                host=server,
                port=puerto,
                user=username,
                passwd=password,
                database=databases,
            )
            mycursor = mydb.cursor()
        except Exception as p:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText(str(p))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            if msg.exec_():
                pass
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Coneccion Exitosa")
            msg.setWindowTitle("Exito")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            if msg.exec_():
                pass

    def try_sql(self):
        try:
            server = "localhost" + "," + str(self.puertoO_edit.text())
            database = str(self.nombreO_edit.text())
            username = str(self.usuarioO_edit.text())
            password = str(self.passwordO_edit.text())
            cnxn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
                + server
                + ";DATABASE="
                + database
                + ";UID="
                + username
                + ";PWD="
                + password
            )
            cursor = cnxn.cursor()
        except Exception as p:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText(str(p))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            if msg.exec_():
                pass
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Coneccion Exitosa")
            msg.setWindowTitle("Exito")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            if msg.exec_():
                pass

    def open_window(self):
        sqldict = {
            "instancia": str(self.instanciaO_edit.text()),
            "nombredb": str(self.nombreO_edit.text()),
            "server": str("localhost") + "," + str(self.puertoO_edit.text()),
            "user": str(self.usuarioO_edit.text()),
            "password": str(self.passwordO_edit.text()),
        }
        mysqldict = {
            "instancia": str(self.instanciaD_edit.text()),
            "server": "localhost",
            "nombredb": str(self.nombreD_edit.text()),
            "puerto": str(self.puertoD_edit.text()),
            "user": str(self.usuarioD_edit.text()),
            "password": str(self.passwordD_edit.text()),
        }
        window = QtGui.QMainWindow()
        ui = Main2Window(sqldict, mysqldict)
        ui.show()
        self.close()
        sys.exit(ui.exec_())

    def __init__(self):
        super(MainWindow, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main.ui", self)
        self.actionAbrir.triggered.connect(self.open_file)
        self.actionGuardar.triggered.connect(self.save_file)
        self.probarD_botton.clicked.connect(self.try_mysql)
        self.probarO_botton.clicked.connect(self.try_sql)
        self.execute_botton.clicked.connect(self.open_window)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
sys.exit(app.exec_())
