from PyQt5.QtWidgets import *
from result_python import Ui_MainWindow
from pathlib import Path
import openpyxl
import subprocess
import pandas as pd
import os
import sys


class Result_page(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.expand = 1
        self.consistency_index = None
        self.new_file_name = None
        self.our_data = None
        self.our_data_2 = None
        self.data_Frame = None
        self.consistency_ratio = None
        self.button_reply = None
        self.button_reply_number = 0
        self.rci = [0,0,0.58,0.892,1.116,1.236,1.332,1.395,1.454,1.488,1.512,1.536,1.557,1.571,1.587,1.596]
        self.file_name = "\CriteriaWeights.xlsx"
        self.downloads_path = str(Path.home() / "Downloads")
        self.combined_path = self.downloads_path + self.file_name
        self.ui.action_Consistency.triggered.connect(self.consist_index_slot)
        self.ui.action_Save_as_Excel.triggered.connect(self.save_excel_slot)
        self.ui.action_Restart.triggered.connect(self.restart_button_slot2)

    def restart_button_slot2(self):
        print("x")
        self.button_reply = QMessageBox.question(self,"Question","Are you sure you want to restart the programme?", QMessageBox.Yes, QMessageBox.No,)
        if self.button_reply == QMessageBox.Yes:
            self.button_reply_number = 1
            self.close()
            pathname = self.get_executable_name()
            QApplication.exit()
            subprocess.call([pathname])



    def consist_index_slot(self):
        print(self.consistency_index)
        print(self.consistency_ratio)
        if self.consistency_ratio > 0.09999:
            QMessageBox.information(self, "Model Consistency",
                                    "<font size = 5>Model Consistency Ratio"
                                    "<br><br>"
                                    "Consistency Ratio: {}"
                                    "<br><br>"
                                    "{} > 0.10"
                                    "<br><br>"
                                    "These criteria weights are <b>not consistent<b> for model estimation."
                                    .format(round(self.consistency_ratio,5),round(self.consistency_ratio,5)))
        else:
            print(self.consistency_index)
            print(self.consistency_ratio)
            QMessageBox.information(self, "Model Consistency",
                                    "<font size = 5>Model Consistency Ratio"
                                    "<br><br>"
                                    "Consistency Ratio: {}"
                                    "<br><br>"
                                    "0.10 > {}"
                                    "<br><br>"
                                    "These criteria weights <b>can be used<b> in model estimation."
                                    .format(round(self.consistency_ratio,5),round(self.consistency_ratio,5)))

    def save_excel_slot(self):
        """
        print(self.downloads_path)
        print(self.combined_path)
        if os.path.isfile(self.combined_path):
            self.expand = 1
            while True:
                self.expand += 1
                self.new_file_name = self.file_name.split(".xlsx")[0] + str(self.expand) + ".xlsx"
                self.combined_path = self.downloads_path + self.new_file_name
                if os.path.isfile(self.combined_path):
                    print(self.combined_path)
                    continue
                else:
                    self.file_name = self.new_file_name
                    self.combined_path = self.downloads_path + self.file_name
                    print(self.combined_path)
                    break
        """
        name = QFileDialog.getSaveFileName(self, 'Save File', filter='*.xlsx')
        self.data_Frame.to_excel(name[0])
        #file = open(name, 'w')
        #file.write(self.data_Frame)
        #file.close()
        #self.data_Frame.to_excel(self.combined_path)
        QMessageBox.information(self, "File Saved", "Excel file saved.")

    def get_executable_name(self):
        if getattr(sys, 'frozen', False):
            name, _ = os.path.splitext(os.path.basename((sys.executable)))
        else:
            name, _ = os.path.splitext(os.path.basename((sys.argv[0])))

        return name
