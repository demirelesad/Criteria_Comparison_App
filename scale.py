from PyQt5.QtWidgets import *
from scale_python import Ui_MainWindow
from PyQt5.QtGui import QIcon

class Scale_page(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icons/analytics.png"))


