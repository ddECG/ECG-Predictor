# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_top = QFrame(self.centralwidget)
        self.sidebar_top.setObjectName(u"sidebar_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_top.sizePolicy().hasHeightForWidth())
        self.sidebar_top.setSizePolicy(sizePolicy)
        self.sidebar_top.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar_top.setAutoFillBackground(False)
        self.sidebar_top.setFrameShape(QFrame.NoFrame)
        self.sidebar_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.sidebar_top)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.img_logo = QLabel(self.sidebar_top)
        self.img_logo.setObjectName(u"img_logo")
        self.img_logo.setMinimumSize(QSize(80, 80))
        self.img_logo.setMaximumSize(QSize(100, 80))
        self.img_logo.setPixmap(QPixmap(u":/Logo/Asset 1.svg"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setWordWrap(False)

        self.horizontalLayout.addWidget(self.img_logo)

        self.label_title = QLabel(self.sidebar_top)
        self.label_title.setObjectName(u"label_title")
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QSize(200, 0))
        self.label_title.setMaximumSize(QSize(16777215, 16777215))
        self.label_title.setTextFormat(Qt.RichText)
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_title.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_title)

        self.frame_model = QFrame(self.sidebar_top)
        self.frame_model.setObjectName(u"frame_model")
        self.frame_model.setMinimumSize(QSize(0, 0))
        self.frame_model.setMaximumSize(QSize(600, 16777215))
        self.frame_model.setFrameShape(QFrame.NoFrame)
        self.frame_model.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_model)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_model)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.btn_model_pretrained = QRadioButton(self.widget)
        self.btn_model_pretrained.setObjectName(u"btn_model_pretrained")
        self.btn_model_pretrained.setMinimumSize(QSize(150, 0))
        self.btn_model_pretrained.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btn_model_pretrained.setFont(font)
        self.btn_model_pretrained.setChecked(True)

        self.horizontalLayout_9.addWidget(self.btn_model_pretrained)

        self.btn_model_finetune = QRadioButton(self.widget)
        self.btn_model_finetune.setObjectName(u"btn_model_finetune")
        self.btn_model_finetune.setMinimumSize(QSize(150, 0))
        self.btn_model_finetune.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(18)
        self.btn_model_finetune.setFont(font1)

        self.horizontalLayout_9.addWidget(self.btn_model_finetune)

        self.btn_model_new = QRadioButton(self.widget)
        self.btn_model_new.setObjectName(u"btn_model_new")
        self.btn_model_new.setMinimumSize(QSize(150, 0))
        self.btn_model_new.setMaximumSize(QSize(150, 16777215))
        self.btn_model_new.setFont(font)

        self.horizontalLayout_9.addWidget(self.btn_model_new)


        self.verticalLayout_8.addWidget(self.widget)

        self.frame_6 = QFrame(self.frame_model)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        self.label.setTextFormat(Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setIndent(10)

        self.horizontalLayout_10.addWidget(self.label)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(10)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setMaximumSize(QSize(150, 16777215))
        self.label_4.setWordWrap(True)
        self.label_4.setIndent(10)

        self.horizontalLayout_10.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_model)


        self.verticalLayout_2.addWidget(self.sidebar_top)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.frame_concent = QFrame(self.content)
        self.frame_concent.setObjectName(u"frame_concent")
        self.frame_concent.setFrameShape(QFrame.NoFrame)
        self.frame_concent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_concent)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 12, -1, 0)
        self.description_1 = QLabel(self.frame_concent)
        self.description_1.setObjectName(u"description_1")

        self.verticalLayout_3.addWidget(self.description_1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_selection = QFrame(self.frame_concent)
        self.frame_selection.setObjectName(u"frame_selection")
        self.frame_selection.setMinimumSize(QSize(0, 0))
        self.frame_selection.setFrameShape(QFrame.NoFrame)
        self.frame_selection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_selection)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_id = QFrame(self.frame_selection)
        self.frame_id.setObjectName(u"frame_id")
        sizePolicy.setHeightForWidth(self.frame_id.sizePolicy().hasHeightForWidth())
        self.frame_id.setSizePolicy(sizePolicy)
        self.frame_id.setFrameShape(QFrame.NoFrame)
        self.frame_id.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_id)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.description_ID = QLabel(self.frame_id)
        self.description_ID.setObjectName(u"description_ID")
        self.description_ID.setMaximumSize(QSize(16777215, 30))
        self.description_ID.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.description_ID)

        self.lineEdit_id = QSpinBox(self.frame_id)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_id.setSizePolicy(sizePolicy1)
        self.lineEdit_id.setMinimumSize(QSize(0, 0))
        self.lineEdit_id.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_id.setFrame(True)
        self.lineEdit_id.setMinimum(1)
        self.lineEdit_id.setMaximum(100000)

        self.verticalLayout.addWidget(self.lineEdit_id)


        self.horizontalLayout_6.addWidget(self.frame_id)

        self.frame_file = QFrame(self.frame_selection)
        self.frame_file.setObjectName(u"frame_file")
        self.frame_file.setFrameShape(QFrame.NoFrame)
        self.frame_file.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_file)
#ifndef Q_OS_MAC
        self.horizontalLayout_7.setSpacing(-1)
#endif
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.frame = QFrame(self.frame_file)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
#ifndef Q_OS_MAC
        self.horizontalLayout_8.setSpacing(-1)
#endif
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_selection = QLineEdit(self.frame_3)
        self.lineEdit_selection.setObjectName(u"lineEdit_selection")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_selection.sizePolicy().hasHeightForWidth())
        self.lineEdit_selection.setSizePolicy(sizePolicy2)
        self.lineEdit_selection.setMinimumSize(QSize(0, 0))
        self.lineEdit_selection.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_selection.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_selection)

        self.btn_select_ecg = QPushButton(self.frame_3)
        self.btn_select_ecg.setObjectName(u"btn_select_ecg")
        sizePolicy.setHeightForWidth(self.btn_select_ecg.sizePolicy().hasHeightForWidth())
        self.btn_select_ecg.setSizePolicy(sizePolicy)
        self.btn_select_ecg.setMinimumSize(QSize(30, 30))
        self.btn_select_ecg.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_8.addWidget(self.btn_select_ecg)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout_7.addWidget(self.frame)


        self.horizontalLayout_6.addWidget(self.frame_file)


        self.verticalLayout_3.addWidget(self.frame_selection)

        self.frame_folder_selection = QFrame(self.frame_concent)
        self.frame_folder_selection.setObjectName(u"frame_folder_selection")
        self.frame_folder_selection.setMinimumSize(QSize(0, 0))
        self.frame_folder_selection.setFrameShape(QFrame.NoFrame)
        self.frame_folder_selection.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_folder_selection)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_folder_selection)


        self.horizontalLayout_3.addWidget(self.frame_concent)


        self.verticalLayout_2.addWidget(self.content)

        self.sidebar_bottom = QFrame(self.centralwidget)
        self.sidebar_bottom.setObjectName(u"sidebar_bottom")
        self.sidebar_bottom.setMinimumSize(QSize(0, 0))
        self.sidebar_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar_bottom.setFrameShape(QFrame.NoFrame)
        self.sidebar_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_bottom)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 12)
        self.horizontalSpacer = QSpacerItem(530, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_convert = QDialogButtonBox(self.sidebar_bottom)
        self.btn_convert.setObjectName(u"btn_convert")
        sizePolicy.setHeightForWidth(self.btn_convert.sizePolicy().hasHeightForWidth())
        self.btn_convert.setSizePolicy(sizePolicy)
        self.btn_convert.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.btn_convert)


        self.verticalLayout_2.addWidget(self.sidebar_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1090, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">Heart age</span></p><p align=\"justify\"><span style=\" font-size:18pt;\">Predict age from ECG - How old are you?</span></p></body></html>", None))
        self.btn_model_pretrained.setText(QCoreApplication.translate("MainWindow", u" Pretrained", None))
        self.btn_model_finetune.setText(QCoreApplication.translate("MainWindow", u" Fine tuned", None))
        self.btn_model_new.setText(QCoreApplication.translate("MainWindow", u" New", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pretrained model from <span style=\" font-style:italic;\">Lima.  et.  al.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Model fine tuned on PTB-xl", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model trained from PTB-xl", None))
        self.description_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Select ECG-file</span></p><p>Select a single ECG file (.hdf5) and ID of ECG you want to predict age on.</p></body></html>", None))
        self.description_ID.setText(QCoreApplication.translate("MainWindow", u"Sample ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ECG file", None))
        self.btn_select_ecg.setText(QCoreApplication.translate("MainWindow", u"Select ECG", None))
    # retranslateUi

