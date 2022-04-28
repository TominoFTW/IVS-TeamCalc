#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtGui
from gui.gui import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("hand.ico"))
    w = MainWindow()
    app.exec()

if __name__ == "__main__":
    main()
