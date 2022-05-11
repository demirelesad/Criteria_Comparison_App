from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ask_python import Ui_MainWindow
from result import Result_page
import numpy as np
import pandas as pd
from PyQt5.QtGui import QDoubleValidator


class Ask_page(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/icons/analytics.png"))
        self.result = Result_page()
        self.number = 0
        self.matris = np.ones([self.number, self.number])
        self.list2 = []
        self.list3 = []
        self.old = 0
        self.column_sums = None
        self.row_sums = None
        self.p2 = None
        self.aij = None
        self.empty = None
        self.sumrowcopy = None
        self.s_over_c = []
        self.s_c_mean = None
        self.lambda_matris = None
        self.cons_index = None
        self.row_sums_org = None
        self.copy_matris = None
        self.x = 0
        self.y = 1
        self.z = 0
        self.x_x = 0
        self.y_y = 2
        self.ui.lineEdit.close()
        self.ui.pushButton_tick.close()
        self.ui.pushButton_back.close()
        self.ui.lineEdit.setValidator(QDoubleValidator(0,10,3))
        self.ui.pushButton_restart.clicked.connect(self.finish_button_pressed_slot)
        self.ui.pushButton_restart.clicked.connect(self.second_calculate)
        self.ui.pushButton_tick.clicked.connect(self.when_clicked)
        self.ui.pushButton_back.clicked.connect(self.back_command)

        self.ui.label.setText("Click enter to start")



    def finish_button_pressed_slot(self):

        while '' in self.list2:
            self.list2.remove('')
        print(self.list2)
        self.ui.lineEdit.show()
        self.ui.pushButton_tick.show()
        self.ui.pushButton_back.show()

    def when_clicked(self):
        self.aij = self.ui.lineEdit.text()
        if self.aij == "":
            QMessageBox.warning(self,"Error Message","You didn't enter a number!")
        elif self.aij == "0":
            QMessageBox.warning(self,"Error Message","Enter a valid number!")
        elif float(self.aij) > 9.00:
            QMessageBox.warning(self, "Error Message", "Enter a valid number!")
        else:
            self.ui.lineEdit.clear()
            if self.x < (self.number - 1):
                if self.x < self.y:
                    self.matris[self.x, self.y] = float(self.aij)
                    self.matris[self.y, self.x] = 1 / float(self.aij)
                    self.y += 1
                    print(self.matris)
                    if self.z < len(self.list3)-1:
                        self.z += 1
                        self.ui.label.setText(self.list3[self.z])
                        self.ui.statusbar.showMessage(
                            "Current Quesiton: {}  Total Questions: {}".format(self.y_y, self.x_x))
                        self.y_y += 1
                    if self.x == (self.number - 2):
                        self.x = self.x + 1
                        self.y = 0
                        self.ui.lineEdit.setText("1")
                        self.copy_matris = self.matris.copy()
                        self.column_sums = [sum([row[i] for row in self.matris]) for i in range(0, len(self.matris[0]))]
                        for i in range(0, self.number):
                            self.matris[:, i] = self.matris[:, i] / self.column_sums[i]

                        self.row_sums = [sum(row) for row in self.matris]
                        self.row_sums_org = self.row_sums
                        for i in range(0, len(self.row_sums)):
                            self.row_sums[i] = self.row_sums[i] / (self.number) * 100

                        self.p2 = self.row_sums


                        for i in range(0, self.number):
                            self.copy_matris[:, i] = self.copy_matris[:, i] * self.row_sums_org[i]
                        self.sumrowcopy = [sum(row) for row in self.copy_matris]
                        self.s_over_c = [0] * self.number
                        for i in range(0, len(self.s_over_c)):
                            self.s_over_c[i] = self.sumrowcopy[i] / self.row_sums_org[i]
                        self.s_c_mean = sum(self.s_over_c) / len(self.s_over_c)
                        self.lambda_matris = self.s_c_mean
                        self.cons_index = (self.lambda_matris - self.number) / (self.number-1)
                        self.result.consistency_index = self.cons_index

                        self.result.consistency_ratio = self.result.consistency_index / self.result.rci[self.number - 1]

                        self.result.our_data = pd.Series(data = self.list2, name="Criteria")
                        self.result.our_data_2 = pd.Series(data = self.p2, name="Weights")
                        self.result.data_Frame = pd.concat([self.result.our_data , self.result.our_data_2], axis= 1)
                        self.close()
                        self.result.show()

                        if self.number == 3:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))

                        if self.number == 4:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))

                        if self.number == 5:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))

                        if self.number == 6:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))

                        if self.number == 7:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))

                        if self.number == 8:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))

                        if self.number == 9:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))

                        if self.number == 10:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))

                        if self.number == 11:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])
                            self.result.ui.label_25.setText(self.list2[10])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))
                            self.result.ui.label_26.setText("% {}".format(round(self.p2[10], 2)))

                        if self.number == 12:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])
                            self.result.ui.label_25.setText(self.list2[10])
                            self.result.ui.label_27.setText(self.list2[11])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))
                            self.result.ui.label_26.setText("% {}".format(round(self.p2[10], 2)))
                            self.result.ui.label_28.setText("% {}".format(round(self.p2[11], 2)))

                        if self.number == 13:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])
                            self.result.ui.label_25.setText(self.list2[10])
                            self.result.ui.label_27.setText(self.list2[11])
                            self.result.ui.label_29.setText(self.list2[12])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))
                            self.result.ui.label_26.setText("% {}".format(round(self.p2[10], 2)))
                            self.result.ui.label_28.setText("% {}".format(round(self.p2[11], 2)))
                            self.result.ui.label_30.setText("% {}".format(round(self.p2[12], 2)))

                        if self.number == 14:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])
                            self.result.ui.label_25.setText(self.list2[10])
                            self.result.ui.label_27.setText(self.list2[11])
                            self.result.ui.label_29.setText(self.list2[12])
                            self.result.ui.label_31.setText(self.list2[13])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))
                            self.result.ui.label_26.setText("% {}".format(round(self.p2[10], 2)))
                            self.result.ui.label_28.setText("% {}".format(round(self.p2[11], 2)))
                            self.result.ui.label_30.setText("% {}".format(round(self.p2[12], 2)))
                            self.result.ui.label_32.setText("% {}".format(round(self.p2[13], 2)))

                        if self.number == 15:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])
                            self.result.ui.label_25.setText(self.list2[10])
                            self.result.ui.label_27.setText(self.list2[11])
                            self.result.ui.label_29.setText(self.list2[12])
                            self.result.ui.label_31.setText(self.list2[13])
                            self.result.ui.label_33.setText(self.list2[14])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))
                            self.result.ui.label_26.setText("% {}".format(round(self.p2[10], 2)))
                            self.result.ui.label_28.setText("% {}".format(round(self.p2[11], 2)))
                            self.result.ui.label_30.setText("% {}".format(round(self.p2[12], 2)))
                            self.result.ui.label_32.setText("% {}".format(round(self.p2[13], 2)))
                            self.result.ui.label_34.setText("% {}".format(round(self.p2[14], 2)))

                        if self.number == 16:
                            self.result.ui.label.setText(self.list2[0])
                            self.result.ui.label_3.setText(self.list2[1])
                            self.result.ui.label_9.setText(self.list2[2])
                            self.result.ui.label_11.setText(self.list2[3])
                            self.result.ui.label_13.setText(self.list2[4])
                            self.result.ui.label_15.setText(self.list2[5])
                            self.result.ui.label_17.setText(self.list2[6])
                            self.result.ui.label_19.setText(self.list2[7])
                            self.result.ui.label_21.setText(self.list2[8])
                            self.result.ui.label_23.setText(self.list2[9])
                            self.result.ui.label_25.setText(self.list2[10])
                            self.result.ui.label_27.setText(self.list2[11])
                            self.result.ui.label_29.setText(self.list2[12])
                            self.result.ui.label_31.setText(self.list2[13])
                            self.result.ui.label_33.setText(self.list2[14])
                            self.result.ui.label_35.setText(self.list2[15])

                            self.result.ui.label_2.setText("% {}".format(round(self.p2[0], 2)))
                            self.result.ui.label_4.setText("% {}".format(round(self.p2[1], 2)))
                            self.result.ui.label_10.setText("% {}".format(round(self.p2[2], 2)))
                            self.result.ui.label_12.setText("% {}".format(round(self.p2[3], 2)))
                            self.result.ui.label_14.setText("% {}".format(round(self.p2[4], 2)))
                            self.result.ui.label_16.setText("% {}".format(round(self.p2[5], 2)))
                            self.result.ui.label_18.setText("% {}".format(round(self.p2[6], 2)))
                            self.result.ui.label_20.setText("% {}".format(round(self.p2[7], 2)))
                            self.result.ui.label_22.setText("% {}".format(round(self.p2[8], 2)))
                            self.result.ui.label_24.setText("% {}".format(round(self.p2[9], 2)))
                            self.result.ui.label_26.setText("% {}".format(round(self.p2[10], 2)))
                            self.result.ui.label_28.setText("% {}".format(round(self.p2[11], 2)))
                            self.result.ui.label_30.setText("% {}".format(round(self.p2[12], 2)))
                            self.result.ui.label_32.setText("% {}".format(round(self.p2[13], 2)))
                            self.result.ui.label_34.setText("% {}".format(round(self.p2[14], 2)))
                            self.result.ui.label_36.setText("% {}".format(round(self.p2[15], 2)))

                    if self.y == self.number:
                        self.old = self.y
                        self.x += 1
                        self.y = self.x + 1


            else:
                QMessageBox.warning(self,"Error","something went wrong..")
                self.close()




    def second_calculate(self):
        for i in range(0, self.number):
            for j in range(0, self.number):
                if i < j:
                    self.list3.append('How important is option "{}" over option "{}" ?: '.format(self.list2[i], self.list2[j]))

        self.ui.label.setText(self.list3[self.z])
        self.ui.pushButton_restart.close()
        self.ui.statusbar.showMessage("Current Quesiton: 1  Total Questions: {}".format(self.x_x))
        self.ui.label_2.setText("Pls give your answers as floats and click tick button or 'Enter'")
        self.ui.label_3.setText("Please give answers in the range of 0-9 for the significance of the model.")

    def back_command(self):

        if self.y - self.x > 1:
            self.y = self.y - 1
            self.matris[self.x, self.y] = 1
            self.matris[self.y, self.x] = 1
            self.ui.lineEdit.clear()
            self.z -= 1
            self.ui.label.setText(self.list3[self.z])
            self.y_y -= 2
            self.ui.statusbar.showMessage(
                "Current Quesiton: {}  Total Questions: {}".format(self.y_y, self.x_x))
            self.y_y += 1
        else:
            self.x = self.x - 1
            self.y = self.old - 1
            self.matris[self.x, self.y] = 1
            self.matris[self.y, self.x] = 1
            self.ui.lineEdit.clear()
            self.z -= 1
            self.ui.label.setText(self.list3[self.z])
            self.y_y -= 2
            self.ui.statusbar.showMessage(
                "Current Quesiton: {}  Total Questions: {}".format(self.y_y, self.x_x))
            self.y_y += 1










