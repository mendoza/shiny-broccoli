import sys
from PyQt4 import QtCore, QtGui, uic
import mysql.connector
import pyodbc


class prototipoWindow(QtGui.QMainWindow):
    def __init__(self):
        super(prototipoWindow, self).__init__()
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("./ui/Main.ui", self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = prototipoWindow()
    window.show()
sys.exit(app.exec_())
