import sys
from PyQt4 import QtCore, QtGui, uic
import mysql.connector
import pyodbc


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
        if filename != "":
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

    def __init__(self):
        super(MainWindow, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main.ui", self)
        self.actionAbrir.triggered.connect(self.open_file)
        self.actionGuardar.triggered.connect(self.save_file)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
sys.exit(app.exec_())
