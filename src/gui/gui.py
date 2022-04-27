from PyQt5 import QtWidgets, QtGui
import sys
from ivs import IvsWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        with open("app.qss", "r") as style:
            self.setStyleSheet(style.read())

        self.__help = self.menuBar().addMenu(self.tr("&Help"))
        self.__about = self.__help.addAction(self.tr("about"))
        self.setWindowTitle("IVS Calc")
        l = IvsWidget()
        self.setFixedSize(l.size())
        self.setCentralWidget(l)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("hand.ico"))
    w = MainWindow()
    app.exec()
