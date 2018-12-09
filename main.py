import sys
from PyQt4 import QtCore, QtGui, uic
import mysql.connector
import pyodbc


class MainWindow(QtGui.QMainWindow):
    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open file", "", "*.rpc")

    def save_file(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", "*.rpc")
        with open(filename, "w") as file:
            file.write(str(self.instanciaO_edit.Text))

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
