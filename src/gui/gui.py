#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @package gui
# Definition of base window

import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from gui.ivs import IvsWidget, click_process
import pathlib

##
# @brief MainWindow class defining keyboard events
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        with open(f"{pathlib.Path(__file__).parent.resolve()}/app.qss", "r") as style:
            self.setStyleSheet(style.read())
        self.__help = self.menuBar().addMenu(self.tr("&Help"))
        self.__about = self.__help.addAction(self.tr("about"))
        self.__about.triggered.connect(self.helpme)
        self.setWindowTitle("IVS Calc")
        l = IvsWidget()
        self.setFixedSize(l.size())
        self.setCentralWidget(l)
        self.show()
        
    @pyqtSlot()
    def helpme(self):
        subprocess.Popen(["xdg-open", f"{pathlib.Path(__file__).parent.resolve()}/napoveda.pdf"])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            click_process(0, "0")
        elif event.key() == Qt.Key_1:
            click_process(1, "1")
        elif event.key() == Qt.Key_2:
            click_process(2, "2")
        elif event.key() == Qt.Key_3:
            click_process(3, "3")
        elif event.key() == Qt.Key_4:
            click_process(4, "4")
        elif event.key() == Qt.Key_5:
            click_process(5, "5")
        elif event.key() == Qt.Key_6:
            click_process(6, "6")
        elif event.key() == Qt.Key_7:
            click_process(7, "7")
        elif event.key() == Qt.Key_8:
            click_process(8, "8")
        elif event.key() == Qt.Key_9:
            click_process(9, "9")
        elif event.key() == Qt.Key_Plus:
            click_process(13, "+")
        elif event.key() == Qt.Key_Minus:
            click_process(14, "-")
        elif event.key() == Qt.Key_Asterisk:
            click_process(15, "×")
        elif event.key() == Qt.Key_Slash:
            click_process(16, "÷")
        elif event.key() == Qt.Key_R:
            click_process(17, "√")
        elif event.key() == Qt.Key_AsciiCircum:
            click_process(18, "^")
        elif event.key() == Qt.Key_Period:
            click_process(10, ".")
        elif event.key() == Qt.Key_Exclam:
            click_process(20, "!")
        elif event.key() == Qt.Key_Escape:
            click_process(11, "AC")
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            click_process(21, "=")
        elif event.key() == Qt.Key_ParenLeft:
            click_process(22, "(")
        elif event.key() == Qt.Key_ParenRight:
            click_process(23, ")")
        elif event.key() == Qt.Key_Backspace:
            click_process(12, "C")
