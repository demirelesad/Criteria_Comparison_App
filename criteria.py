from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from criteria_python import Ui_MainWindow
from ask import Ask_page
import numpy as np
import time

class Criteria_name(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ask = Ask_page()
        self.setWindowIcon(QIcon(":/icons/icons/analytics.png"))
        self.num = 0
        self.list1 = []
        self.ui.pushButton_go.setStyleSheet("border-image: url(:/icons/icons/Tick.png);\n""")
        self.ui.pushButton_go.pressed.connect(self.go_button_pressed_slot)
        self.ui.pushButton_go.clicked.connect(self.go_button_clicked_slot)

    def go_button_pressed_slot(self):
        self.ui.pushButton_go.setStyleSheet("border-image: url(:/icons/icons/Tick2.png);\n""")
        self.ui.label_20.setText("               Your process is in progress, please wait.              ")


    def go_button_clicked_slot(self):
        time.sleep(1)
        self.ask.show()
        self.ask.number = self.num
        self.ask.x_x = int(self.num * (self.num - 1) / 2)
        self.ask.matris = np.ones([self.ask.number, self.ask.number])
        self.close()

        self.list1.append(self.ui.lineEdit_1.text())
        self.list1.append(self.ui.lineEdit_9.text())
        self.list1.append(self.ui.lineEdit_2.text())
        self.list1.append(self.ui.lineEdit_10.text())
        self.list1.append(self.ui.lineEdit_3.text())
        self.list1.append(self.ui.lineEdit_11.text())
        self.list1.append(self.ui.lineEdit_4.text())
        self.list1.append(self.ui.lineEdit_12.text())
        self.list1.append(self.ui.lineEdit_5.text())
        self.list1.append(self.ui.lineEdit_13.text())
        self.list1.append(self.ui.lineEdit_6.text())
        self.list1.append(self.ui.lineEdit_14.text())
        self.list1.append(self.ui.lineEdit_7.text())
        self.list1.append(self.ui.lineEdit_15.text())
        self.list1.append(self.ui.lineEdit_8.text())
        self.list1.append(self.ui.lineEdit_16.text())



        self.ask.list2.append(self.ui.lineEdit_1.text())
        self.ask.list2.append(self.ui.lineEdit_9.text())
        self.ask.list2.append(self.ui.lineEdit_2.text())
        self.ask.list2.append(self.ui.lineEdit_10.text())
        self.ask.list2.append(self.ui.lineEdit_3.text())
        self.ask.list2.append(self.ui.lineEdit_11.text())
        self.ask.list2.append(self.ui.lineEdit_4.text())
        self.ask.list2.append(self.ui.lineEdit_12.text())
        self.ask.list2.append(self.ui.lineEdit_5.text())
        self.ask.list2.append(self.ui.lineEdit_13.text())
        self.ask.list2.append(self.ui.lineEdit_6.text())
        self.ask.list2.append(self.ui.lineEdit_14.text())
        self.ask.list2.append(self.ui.lineEdit_7.text())
        self.ask.list2.append(self.ui.lineEdit_15.text())
        self.ask.list2.append(self.ui.lineEdit_8.text())
        self.ask.list2.append(self.ui.lineEdit_16.text())



