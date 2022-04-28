from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSpacerItem, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot
from ivsmath.parser import infixToPrefix


def click_process(id, text):
    if id in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        IvsWidget.textBox.value += text
        if IvsWidget.buffer[-1] not in (
            "-",
            "+",
            "*",
            "/",
            "%",
            "^",
            "!0",
            "_",
            "(",
            ")",
        ):
            IvsWidget.buffer[-1] += text
        else:
            IvsWidget.buffer.append(text)
    elif id in (13, 14, 22, 23):
        IvsWidget.textBox.value += text
        IvsWidget.buffer.append(text)
    elif id == 15:
        IvsWidget.textBox.value += text
        IvsWidget.buffer.append("*")
    elif id == 16:
        IvsWidget.textBox.value += text
        IvsWidget.buffer.append("/")
    elif id == 17:
        IvsWidget.textBox.value += text
        IvsWidget.buffer.append("_")
    elif id == 18:
        IvsWidget.textBox.value += "^"
        IvsWidget.buffer.append("^")
    elif id == 19:
        IvsWidget.textBox.value += text
        IvsWidget.buffer.append("%")
    elif id == 20:
        IvsWidget.textBox.value += text
        IvsWidget.buffer.append("!")
        IvsWidget.buffer.append("0")
    elif id == 10:
        IvsWidget.textBox.value += text
        IvsWidget.buffer[-1] += "."
    elif id == 11:
        IvsWidget.textBox.value = "0"
        IvsWidget.buffer = ["0"]
    elif id == 12:
        IvsWidget.textBox.backspace()
        if len(IvsWidget.buffer):
            if IvsWidget.buffer[-1] not in ("-", "+", "*", "/", "%", "^", "!0", "_"):
                IvsWidget.buffer[-1] = IvsWidget.buffer[-1][:-1]
                if not len(IvsWidget.buffer[-1]):
                    IvsWidget.buffer.pop()
            else:
                IvsWidget.buffer.pop()
    elif id == 21:
        try:
            print(infixToPrefix(IvsWidget.buffer))
        except Exception as e:
            IvsWidget.buffer = ["0"]
            IvsWidget.textBox.value = "Syntax Error"


class IvsButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(args[0], **kwargs)
        self.__text = args[0]
        self.__id = args[1]
        self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self, *args, **kwargs):
        click_process(self.__id, self.__text)


class IvsPushButton(IvsButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class IvsLongButton(IvsButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class IvsTextBox(QLineEdit):
    @property
    def value(self):
        return self.text()

    @value.setter
    def value(self, value):
        self.setText(value)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignRight)


class IvsWidget(QWidget):

    textBox = None
    buffer = ["0"]

    def __init__(self) -> None:
        super().__init__()
        self.__textBox = IvsTextBox("0")
        IvsWidget.textBox = self.__textBox
        self.setFocusPolicy(Qt.StrongFocus)
        self.__layout = QGridLayout()
        self.__layout.addWidget(self.__textBox, 0, 0, 1, 3)
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
        self.__layout.addWidget(IvsPushButton("(", 22), 5, 1)
        self.__layout.addWidget(IvsPushButton(")", 23), 5, 2)
        self.__layout.addWidget(IvsPushButton("×", 15), 2, 5)
        self.__layout.addWidget(IvsPushButton("÷", 16), 3, 5)
        self.__layout.addWidget(IvsPushButton("√", 17), 2, 4)
        self.__layout.addWidget(IvsPushButton("xⁿ", 18), 3, 4)
        self.__layout.addWidget(IvsPushButton("mod", 19), 4, 4)
        self.__layout.addWidget(IvsPushButton("!", 20), 5, 4)
        self.__layout.addWidget(IvsLongButton("=", 21), 4, 5, 2, 1)
        self.__layout.setHorizontalSpacing(0)
        self.__layout.setVerticalSpacing(0)
        self.setLayout(self.__layout)
