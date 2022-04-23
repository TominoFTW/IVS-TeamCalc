#!/usr/bin/env python
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSpacerItem, QLineEdit
from PyQt5.QtCore import Qt


class IvsPushButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class IvsLongButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class IvsTextBox(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignRight)


class IvsWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__layout = QGridLayout()
        self.__layout.addWidget(IvsTextBox('Test'), 0, 0, 1, 3)
        self.__layout.addWidget(IvsLongButton('0'), 4, 0, 1, 2)
        self.__layout.addWidget(IvsPushButton(','), 4, 2)
        self.__layout.addWidget(IvsPushButton('1'), 3, 0)
        self.__layout.addWidget(IvsPushButton('2'), 3, 1)
        self.__layout.addWidget(IvsPushButton('3'), 3, 2)
        self.__layout.addWidget(IvsPushButton('4'), 2, 0)
        self.__layout.addWidget(IvsPushButton('5'), 2, 1)
        self.__layout.addWidget(IvsPushButton('6'), 2, 2)
        self.__layout.addWidget(IvsPushButton('7'), 1, 0)
        self.__layout.addWidget(IvsPushButton('8'), 1, 1)
        self.__layout.addWidget(IvsPushButton('9'), 1, 2)
        self.__layout.addItem(QSpacerItem(50 ,100), 0, 3)
        self.__layout.addWidget(IvsPushButton('AC'), 0, 4)
        self.__layout.addWidget(IvsPushButton('C'), 0, 5)
        self.__layout.addWidget(IvsPushButton('*'), 2, 4)
        self.__layout.addWidget(IvsPushButton('/'), 2, 5)
        self.__layout.setHorizontalSpacing(0)
        self.__layout.setVerticalSpacing(0)
        self.setLayout(self.__layout)