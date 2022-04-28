#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @package ivscalc
# Main ivscalc module.

##
# @brief Main ivscalc module.

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
