# -----------------------------------------------------------------------------
# Module: User interface
#
# What: User interface logic and definitions.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
from curses.ascii import NAK
import glob
import re
import os
from pathlib import Path # Window specific paths
from PySide2.QtWidgets import QDialogButtonBox, QMainWindow, QFileDialog, QMessageBox, QWizard, QWizardPage
from PySide2.QtCore import QSize

# Local resources 
from resources.user_interface.mainwindow import Ui_MainWindow
from modules.predict import predict

# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    '''Main user interface window.
    
    Class that contains all functions and interactions related to
    the main user interace, including initialization of ui, loading
    custom widgets and settings and establishing ui connections.
    Inherits UI file from resources/user_interface/mainwindow.ui.
    Args:
        None
    
    Attributes:
        None
    '''

    # ---- Constructor ---- #
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        # General variables
        self.file_path = None
        self.predicted_age = None
        self.true_age = None
        self.model = "resources/model_pretrained"

        # Define user interface
        self.setupUi(self)
        self.setWindowTitle("ECG age predictor")
        self.btn_convert.button(QDialogButtonBox.Ok).setText("Predict")
        self.btn_convert.button(QDialogButtonBox.Ok).setEnabled(False)

        window_size = QSize(1200, 500)
        self.resize(window_size)
        self.setFixedSize(window_size)

        # Signals
        self.btn_select_ecg.clicked.connect(self.select_file)
        self.btn_convert.rejected.connect(self.exit_program)
        self.btn_convert.accepted.connect(self.predict_age)
        self.btn_model_pretrained.clicked.connect(self.model_pretrained)
        self.btn_model_finetune.clicked.connect(self.model_finetune)
        self.btn_model_new.clicked.connect(self.model_new) 

    # ---- Slots ---- #
    def select_file(self,) -> None:
        ''' Select single hdf5 file. '''
        self.dialog_file_dialog()

    def predict_age(self) -> None:
        ''' Predicts age '''
        self.calculate_age()

    def model_pretrained(self) -> None:
        ''' Selects pretrained model'''
        self.model = "resources/model_pretrained"
        print(self.model)


    def model_finetune(self) -> None:
        ''' Selects fine tuned model'''
        self.model = "resources/model_finetune"
        print(self.model)


    def model_new(self) -> None:
        ''' Selects pretrained model'''
        self.model = "resources/model_new"
        print(self.model)

    def exit_program(self) -> None:
        ''' Exits probram. '''
        self.close()

    # ---- Functions ---- #
    def select_model(self):
        print("Test")

    def calculate_age(self):
        ''' Predicts age based on selected ID and file_path. '''

        # Get ID
        id = self.lineEdit_id.value()

        # Predict
        self.predicted_age, self.true_age = predict(self.model, self.file_path, exam_id=id)
        
        # Print
        message = f"Age prediction for ID: {id}.\n\nTrue age: {self.true_age}\nPredicted age: {self.predicted_age}"
        self.message_box(type=QMessageBox.Information, message=message)

    # ---- Dialogs ---- #
    def dialog_file_dialog(self) -> None:
        ''' Dialog to select file using native wizard. '''

        # Define dialog
        dlg = QFileDialog()
        
        # Check if folder or file.
        dlg.setLabelText(QFileDialog.Accept, "Select HDF5 file")
        dlg.setFileMode(QFileDialog.ExistingFile)
        dlg.setNameFilter("HDF5 files (*.hdf5)")

        # Retrieve selection
        if dlg.exec_():
            self.file_path = dlg.selectedFiles()[0]
            self.lineEdit_selection.setText(str(self.file_path))
            self.btn_convert.button(QDialogButtonBox.Ok).setEnabled(True)

    def message_box(self, type: QMessageBox, message: str) -> None:
        ''' Dialog that display warnings '''
        dlg = QMessageBox(self)
        
        dlg.setWindowTitle(message)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(type)
        
        dlg.exec_()