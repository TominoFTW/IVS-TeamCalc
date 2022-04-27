#!/usr/bin/env python
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSpacerItem, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot


class IvsPushButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(args[0], **kwargs)
        print(args, kwargs, "\n")
        self.__id = args[1]
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self, *args, **kwargs):
        print(f"PyQt5 button click {self.__id} {kwargs}")


class IvsLongButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(args[0], **kwargs)
        self.__id = args[1]
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self, *args, **kwargs):
        print(f"PyQt5 button click {self.__id} {kwargs}")


class IvsTextBox(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignRight)


class IvsWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__layout = QGridLayout()
        self.__layout.addWidget(IvsTextBox("Test"), 0, 0, 1, 3)
        self.__layout.addWidget(IvsLongButton("0", 0), 4, 0, 1, 2)
        self.__layout.addWidget(IvsPushButton("1", 1), 3, 0)
        self.__layout.addWidget(IvsPushButton("2", 2), 3, 1)
        self.__layout.addWidget(IvsPushButton("3", 3), 3, 2)
        self.__layout.addWidget(IvsPushButton("4", 4), 2, 0)
        self.__layout.addWidget(IvsPushButton("5", 5), 2, 1)
        self.__layout.addWidget(IvsPushButton("6", 6), 2, 2)
        self.__layout.addWidget(IvsPushButton("7", 7), 1, 0)
        self.__layout.addWidget(IvsPushButton("8", 8), 1, 1)
        self.__layout.addWidget(IvsPushButton("9", 9), 1, 2)
        self.__layout.addWidget(IvsPushButton(",", 10), 4, 2)
        self.__layout.addItem(QSpacerItem(50, 100), 0, 3)
        self.__layout.addWidget(IvsPushButton("AC", 11), 0, 4)
        self.__layout.addWidget(IvsPushButton("C", 12), 0, 5)
        self.__layout.addWidget(IvsPushButton("+", 13), 1, 4)
        self.__layout.addWidget(IvsPushButton("-", 14), 1, 5)
        self.__layout.addWidget(IvsPushButton("×", 15), 2, 5)
        self.__layout.addWidget(IvsPushButton("÷", 16), 3, 5)
        self.__layout.addWidget(IvsPushButton("√", 17), 2, 4)
        self.__layout.addWidget(IvsPushButton("xⁿ", 18), 3, 4)
        self.__layout.addWidget(IvsPushButton("%", 19), 4, 4)
        self.__layout.addWidget(IvsPushButton("!", 20), 4, 5)
        self.__layout.setHorizontalSpacing(0)
        self.__layout.setVerticalSpacing(0)
        self.setLayout(self.__layout)
