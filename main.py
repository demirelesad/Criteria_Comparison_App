import PyQt5.QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from design_python import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from criteria import Criteria_name
from scale import Scale_page
from result import Result_page
import time
import sys


class Ahpmain(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.criteria = Criteria_name()
        self.scale = Scale_page()
        self.resultt = Result_page()
        self.setWindowIcon(QIcon(":/icons/icons/analytics.png"))
        self.sonuc = 0
        self.ui.pushButton_enter.pressed.connect(self.enter_button_pressed_slot)
        self.ui.pushButton_enter.pressed.connect(self.number_criteria)
        self.ui.pushButton_enter.clicked.connect(self.enter_button_clicked_slot)
        self.ui.action_About_the_App.triggered.connect(self.about_app_slot)
        self.ui.action_About_the_AHP.triggered.connect(self.about_ahp_slot)
        self.ui.action_About_the_Developer.triggered.connect(self.about_developer_slot)
        self.ui.action_Pairwise_Comparison_Table.triggered.connect(self.comparison_table_slot)


    def about_app_slot(self):
        QMessageBox.about(self, "About the Application",
                            "<font size = 5>This application ranks the criteria according to their importance by calculating the superiority of the criteria against each other in multi-criteria decision making problems using the analytical hierarchy process method."
                            "<br><br>"
                            "<font size = 5> This software was developed by"
                            "<br>"
                            "<b>Ahmet Esad Demirel</b>")

    def about_ahp_slot(self):
        QMessageBox.about(self, "About the Analytic Hierarchy Process",
                          "The Analytic Hierarchy Process is one of the multi-criteria decision-making methods and it is one of the most frequently used methods in solving decision-making problems. The Analytic Hierarchy Process is a method that ranks the criteria intended to be used in solving the problem by weighting them according to the degree of importance among each other, thus enabling criteria and result evaluation. The method can be used as a solver in decision-making problems, as well as in criterion weighting by using it in an integrated manner with different decision-making methods."
                          "<br><br>"
                          "First of all, the proposed Binary Comparison Matrix is used to calculate the comparative advantage of each of the determined criteria (Saaty). As shown in the table, a matrix is formed by scoring the criteria according to the degree of importance compared to other criteria. The diagonals of the matrix will be one (1) because the same criterion has the same degree of self-importance. For the same reason, one side of the diagonal will be the inverse of the other side according to the multiplication operation. In the first step, the columns of the last created matrix should be summed."
                          "<br><br>"
                          "The matrix created in the second step is updated by dividing the matrix elements by the column sums of the matrix. The criteria weights are determined by dividing the row sums of the updated matrix by the number of criteria."
                          "<br><br>"
                          "In the third step, a new matrix is created by multiplying the elements of the matrix created in the first step with the calculated weight of the column's criterion. The row sums of this matrix are recorded as they will be used to calculate the consistency of the model."
                          "<br><br>"
                          "Finally, consistency calculation is done to test the validity of the comparative advantage scores given.")
    def about_developer_slot(self):
        QMessageBox.about(self, "About the Developer",
                          "<font size = 5>This software was developed by"
                          "<br>"
                          "<b>Ahmet Esad Demirel<b>"
                          "<br><br>"
                          "<b>CONTACT ME</b>"
                          "<br><br>"
                          "<a href=\'https://www.linkedin.com/in/ahmet-esad-demirel-403704174/'>Linkedin Profile</a>"
                          "<br><br>"
                          "<a href=\'https://github.com/demirelesad'>Github Profile</a>"
                          "<br><br>"
                          "<a href=\'mailto:demirellesad@gmail.com'>demirellesad@gmail.com</a>")

    def comparison_table_slot(self):
        self.scale.show()
        self.scale.setWindowTitle("Saaty's Scale Of Relative Importance")
        self.scale.ui.statusbar.showMessage("Saaty's Scale Of Relative Importance, 1980")

    def number_criteria(self):
        self.sonuc = self.ui.lcdNumber.intValue()

        return self.sonuc


    def enter_button_pressed_slot(self):
        self.ui.pushButton_enter.setStyleSheet("border-image: url(:/icons/icons/Tick2.png);\n"
"")
        self.ui.label.setText("You Confirmed Your Criteria Number")
        self.ui.label_2.setText("please wait..")



    def enter_button_clicked_slot(self):
        time.sleep(2)
        self.criteria.show()
        self.close()
        if self.sonuc == 3:
            self.criteria.num = 3
            self.criteria.ui.lineEdit_3.close()
            self.criteria.ui.lineEdit_4.close()
            self.criteria.ui.lineEdit_5.close()
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_10.close()
            self.criteria.ui.lineEdit_11.close()
            self.criteria.ui.lineEdit_12.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_3.close()
            self.criteria.ui.label_4.close()
            self.criteria.ui.label_5.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_10.close()
            self.criteria.ui.label_11.close()
            self.criteria.ui.label_12.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 4:
            self.criteria.num = 4
            self.criteria.ui.lineEdit_3.close()
            self.criteria.ui.lineEdit_4.close()
            self.criteria.ui.lineEdit_5.close()
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_11.close()
            self.criteria.ui.lineEdit_12.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_3.close()
            self.criteria.ui.label_4.close()
            self.criteria.ui.label_5.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_11.close()
            self.criteria.ui.label_12.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 5:
            self.criteria.num = 5
            self.criteria.ui.lineEdit_4.close()
            self.criteria.ui.lineEdit_5.close()
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_11.close()
            self.criteria.ui.lineEdit_12.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_4.close()
            self.criteria.ui.label_5.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_11.close()
            self.criteria.ui.label_12.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 6:
            self.criteria.num = 6
            self.criteria.ui.lineEdit_4.close()
            self.criteria.ui.lineEdit_5.close()
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_12.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_4.close()
            self.criteria.ui.label_5.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_12.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 7:
            self.criteria.num = 7
            self.criteria.ui.lineEdit_5.close()
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_12.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_5.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_12.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 8:
            self.criteria.num = 8
            self.criteria.ui.lineEdit_5.close()
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_5.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 9:
            self.criteria.num = 9
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_13.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_13.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 10:
            self.criteria.num = 10
            self.criteria.ui.lineEdit_6.close()
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_6.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 11:
            self.criteria.num = 11
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_14.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_14.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 12:
            self.criteria.num = 12
            self.criteria.ui.lineEdit_7.close()
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_7.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 13:
            self.criteria.num = 13
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_15.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_15.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 14:
            self.criteria.num = 14
            self.criteria.ui.lineEdit_8.close()
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_8.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 15:
            self.criteria.num = 15
            self.criteria.ui.lineEdit_16.close()
            self.criteria.ui.label_16.close()
        if self.sonuc == 16:
            self.criteria.num = 16



uygulama = QApplication([])
pencere = Ahpmain()
pencere.show()
uygulama.exec_()




