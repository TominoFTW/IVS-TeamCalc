from PyQt5 import QtWidgets
from gui.ivs import IvsWidget
import pathlib



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        with open(f"{pathlib.Path(__file__).parent.resolve()}/app.qss", "r") as style:
            self.setStyleSheet(style.read())

        self.__help = self.menuBar().addMenu(self.tr("&Help"))
        self.__about = self.__help.addAction(self.tr("about"))
        self.setWindowTitle("IVS Calc")
        l = IvsWidget()
        self.setFixedSize(l.size())
        self.setCentralWidget(l)
        self.show()
