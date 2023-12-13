# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageszdKiqH.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
# import resources_rc

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(954, 660)
        StackedWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"KonsensRegular"])
        font.setPointSize(12)
        StackedWidget.setFont(font)
        StackedWidget.setStyleSheet(u"background-color: #ffffff;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout = QVBoxLayout(self.page_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        StackedWidget.addWidget(self.page_home)
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.page_edit.setStyleSheet(u"background-color: #F9F8F9;")
        self.verticalLayout_4 = QVBoxLayout(self.page_edit)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_edit)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 150))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.groupBox_4 = QGroupBox(self.frame_15)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font1 = QFont()
        font1.setFamilies([u"KonsensBook"])
        font1.setPointSize(8)
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-radius: 3px;\n"
"	margin-top: 6px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-position: bottom left;\n"
"	padding: 0 30px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(20)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(20, 0, 20, 20)
        self.comboBox_4 = QComboBox(self.groupBox_4)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(250, 30))
        self.comboBox_4.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(10)
        self.comboBox_4.setFont(font2)
        self.comboBox_4.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 5px;\n"
"	padding-left: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.gridLayout_5.addWidget(self.comboBox_4, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(250, 30))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_7.setFont(font2)
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding:5px;\n"
"	padding-left: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.gridLayout_5.addWidget(self.lineEdit_7, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font3 = QFont()
        font3.setFamilies([u"KonsensBook"])
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #d0d0d0;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
" 	font-size: 16px;\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #c0c0c0;\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.groupBox_4)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.groupBox_5 = QGroupBox(self.frame_15)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 400))
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-radius: 3px;\n"
"	margin-top: 6px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-position: bottom left;\n"
"	padding: 0 30px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(20, 10, 20, 20)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_36 = QLabel(self.groupBox_5)
        self.label_36.setObjectName(u"label_36")
        font4 = QFont()
        font4.setFamilies([u"Trebuchet MS"])
        font4.setPointSize(8)
        self.label_36.setFont(font4)
        self.label_36.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_28.addWidget(self.label_36)

        self.dateEdit = QDateEdit(self.groupBox_5)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(250, 30))
        self.dateEdit.setMaximumSize(QSize(16777215, 30))
        self.dateEdit.setFont(font2)
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"	background-color: rgb(242,242,242);\n"
"	border-radius: 5px;\n"
"	padding-left: 15px;\n"
"	border: 2px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_28.addWidget(self.dateEdit)


        self.gridLayout_6.addLayout(self.verticalLayout_28, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_37 = QLabel(self.groupBox_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)
        self.label_37.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_29.addWidget(self.label_37)

        self.dateEdit_2 = QDateEdit(self.groupBox_5)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(250, 30))
        self.dateEdit_2.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_2.setFont(font2)
        self.dateEdit_2.setStyleSheet(u"QDateEdit {\n"
"	background-color: rgb(242,242,242);\n"
"	border-radius: 5px;\n"
"	padding-left: 15px;\n"
"	border: 2px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_29.addWidget(self.dateEdit_2)


        self.gridLayout_6.addLayout(self.verticalLayout_29, 1, 0, 2, 1)

        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #d0d0d0;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
" 	font-size: 16px;\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #c0c0c0;\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_3, 2, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.groupBox_5)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_11)


        self.verticalLayout_4.addWidget(self.frame_15, 0, Qt.AlignHCenter)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, -1, -1, -1)
        self.tab_dados = QTableWidget(self.page_edit)
        if (self.tab_dados.columnCount() < 14):
            self.tab_dados.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tab_dados.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.tab_dados.setObjectName(u"tab_dados")
        font5 = QFont()
        font5.setFamilies([u"KonsensBook"])
        font5.setPointSize(12)
        self.tab_dados.setFont(font5)
        self.tab_dados.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tab_dados.setStyleSheet(u"QTableWidget  {\n"
"	background-color: #f5f5f5;\n"
"	border: 1px solid rgb(99,101,105);\n"
"	gridline-color: #d1d1d1;\n"
"	selection-background-color: #a6a6a6;\n"
"	margin-bottom: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	padding: 5px;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView {\n"
"	background-color: rgb(133,50,117);\n"
"	font: 9pt \"Trebuchet MS\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: rgb(133,50,117);\n"
"	color: white;\n"
"	padding: 5px;\n"
"	border: 0.5px solid transparent;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"	background-color: #ab4c7d;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: #636569;\n"
"	color: white;\n"
"}")
        self.tab_dados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_dados.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_dados.horizontalHeader().setVisible(True)
        self.tab_dados.horizontalHeader().setCascadingSectionResizes(False)
        self.tab_dados.horizontalHeader().setMinimumSectionSize(100)
        self.tab_dados.horizontalHeader().setDefaultSectionSize(130)
        self.tab_dados.horizontalHeader().setProperty("showSortIndicator", False)
        self.tab_dados.verticalHeader().setVisible(False)
        self.tab_dados.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_18.addWidget(self.tab_dados)

        self.frame_14 = QFrame(self.page_edit)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(170, 0))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setLineWidth(1)
        self.verticalLayout_27 = QVBoxLayout(self.frame_14)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_7)

        self.btnAlterarRegistro = QPushButton(self.frame_14)
        self.btnAlterarRegistro.setObjectName(u"btnAlterarRegistro")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAlterarRegistro.sizePolicy().hasHeightForWidth())
        self.btnAlterarRegistro.setSizePolicy(sizePolicy)
        self.btnAlterarRegistro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAlterarRegistro.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(133,50,117);\n"
"	color: white;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ab4c7d;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #550044;\n"
"}")

        self.verticalLayout_27.addWidget(self.btnAlterarRegistro)


        self.horizontalLayout_18.addWidget(self.frame_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.frame_16 = QFrame(self.page_edit)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 48))
        self.frame_16.setStyleSheet(u"background-color: #F9F8F9;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(745, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 44))
        self.label_4.setMaximumSize(QSize(200, 44))

        self.horizontalLayout_19.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_16)

        StackedWidget.addWidget(self.page_edit)
        self.page_del = QWidget()
        self.page_del.setObjectName(u"page_del")
        self.page_del.setStyleSheet(u"background-color: #F9F8F9;")
        self.verticalLayout_3 = QVBoxLayout(self.page_del)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_del)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        StackedWidget.addWidget(self.page_del)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_5 = QVBoxLayout(self.page_settings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.page_settings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        StackedWidget.addWidget(self.page_settings)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.verticalLayout_2 = QVBoxLayout(self.page_add)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_add)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 432))
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"background-color: #F9F8F9;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background-color: #853275;\n"
"	color: #fff;\n"
"	border-radius: 10%;\n"
"	font: 10pt \"KonsensLight\" bold;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setFamilies([u"KonsensRegular"])
        font6.setPointSize(11)
        self.label_8.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_8)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setStyleSheet(u"background-color: #A7A8A9;\n"
"color: #fff;\n"
"border-radius: 10%;\n"
"font: 10pt \"KonsensLight\" bold;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(100, 16777215))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"color: #e6e6e6;")

        self.horizontalLayout_3.addWidget(self.label_9)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setStyleSheet(u"background-color: #A7A8A9;\n"
"color: #fff;\n"
"border-radius: 10%;\n"
"font: 10pt \"KonsensLight\" bold;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"color: #e6e6e6;")

        self.horizontalLayout_4.addWidget(self.label_10)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background-color: #F9F8F9;")
        self.page_geral = QWidget()
        self.page_geral.setObjectName(u"page_geral")
        self.horizontalLayout_7 = QHBoxLayout(self.page_geral)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.page_geral)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(760, 342))
        self.frame_5.setMaximumSize(QSize(900, 600))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(340, 0))
        self.frame_6.setMaximumSize(QSize(340, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(279, 32))
        self.label_11.setMaximumSize(QSize(279, 32))
        self.label_11.setStyleSheet(u"font: 20pt \"KonsensLight\";\n"
"color: #853275;")

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(279, 32))
        self.label_12.setMaximumSize(QSize(279, 32))
        self.label_12.setStyleSheet(u"font: 22pt \"KonsensBold\";\n"
"color: #853275;")

        self.verticalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(279, 32))
        self.label_13.setMaximumSize(QSize(279, 32))
        self.label_13.setStyleSheet(u"font: 20pt \"KonsensLight\";\n"
"color: #853275;")

        self.verticalLayout_8.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(279, 121))
        self.label_14.setMaximumSize(QSize(279, 121))
        self.label_14.setStyleSheet(u"font: 10pt \"KonsensLight\";")
        self.label_14.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_14)

        self.verticalSpacer_2 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 15))
        self.label_23.setMaximumSize(QSize(16777215, 15))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_14.addWidget(self.label_23)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_14.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 15))
        self.label_24.setMaximumSize(QSize(16777215, 15))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_15.addWidget(self.label_24)

        self.lineEdit_2 = QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_15.addWidget(self.lineEdit_2)


        self.gridLayout.addLayout(self.verticalLayout_15, 0, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 15))
        self.label_25.setMaximumSize(QSize(16777215, 15))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_16.addWidget(self.label_25)

        self.lineEdit_3 = QLineEdit(self.frame_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(368, 0))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_16.addWidget(self.lineEdit_3)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 0, 1, 2)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 15))
        self.label_26.setMaximumSize(QSize(16777215, 15))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_17.addWidget(self.label_26)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_17.addWidget(self.lineEdit_4)


        self.gridLayout.addLayout(self.verticalLayout_17, 2, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 15))
        self.label_27.setMaximumSize(QSize(16777215, 15))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_18.addWidget(self.label_27)

        self.lineEdit_5 = QLineEdit(self.frame_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_18.addWidget(self.lineEdit_5)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 1, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 15))
        self.label_28.setMaximumSize(QSize(16777215, 15))
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_19.addWidget(self.label_28)

        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(368, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 50))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_19.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.verticalLayout_19, 3, 0, 1, 2)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 15))
        self.label_29.setMaximumSize(QSize(16777215, 15))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_20.addWidget(self.label_29)

        self.lineEdit_6 = QLineEdit(self.frame_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(368, 0))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_20.addWidget(self.lineEdit_6)


        self.gridLayout.addLayout(self.verticalLayout_20, 4, 0, 1, 2)

        self.btn_DadoGerais = QPushButton(self.frame_7)
        self.btn_DadoGerais.setObjectName(u"btn_DadoGerais")
        self.btn_DadoGerais.setMaximumSize(QSize(16777215, 35))
        font7 = QFont()
        font7.setFamilies([u"KonsensBold"])
        font7.setPointSize(12)
        self.btn_DadoGerais.setFont(font7)
        self.btn_DadoGerais.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(133,50,117);\n"
"	color: white;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ab4c7d;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #550044;\n"
"}")

        self.gridLayout.addWidget(self.btn_DadoGerais, 5, 1, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_geral)
        self.page_NC = QWidget()
        self.page_NC.setObjectName(u"page_NC")
        self.horizontalLayout_6 = QHBoxLayout(self.page_NC)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_8 = QFrame(self.page_NC)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(760, 342))
        self.frame_8.setMaximumSize(QSize(900, 600))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(340, 0))
        self.frame_9.setMaximumSize(QSize(340, 16777215))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_3 = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(279, 32))
        self.label_15.setMaximumSize(QSize(279, 32))
        self.label_15.setStyleSheet(u"font: 20pt \"KonsensLight\";\n"
"color: #853275;")

        self.verticalLayout_11.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(279, 32))
        self.label_16.setMaximumSize(QSize(279, 32))
        self.label_16.setStyleSheet(u"font: 22pt \"KonsensBold\";\n"
"color: #853275;")

        self.verticalLayout_11.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(279, 32))
        self.label_17.setMaximumSize(QSize(279, 32))
        self.label_17.setStyleSheet(u"font: 20pt \"KonsensLight\";\n"
"color: #853275;")

        self.verticalLayout_11.addWidget(self.label_17)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(279, 121))
        self.label_18.setMaximumSize(QSize(279, 121))
        self.label_18.setStyleSheet(u"font: 10pt \"KonsensLight\";")
        self.label_18.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_18)

        self.verticalSpacer_4 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(10, -1, 10, 10)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_30 = QLabel(self.frame_10)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 15))
        self.label_30.setMaximumSize(QSize(16777215, 15))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_21.addWidget(self.label_30)

        self.lineEdit_12 = QLineEdit(self.frame_10)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_21.addWidget(self.lineEdit_12)


        self.gridLayout_2.addLayout(self.verticalLayout_21, 0, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_31 = QLabel(self.frame_10)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 15))
        self.label_31.setMaximumSize(QSize(16777215, 15))
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_22.addWidget(self.label_31)

        self.lineEdit_9 = QLineEdit(self.frame_10)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_22.addWidget(self.lineEdit_9)


        self.gridLayout_2.addLayout(self.verticalLayout_22, 0, 1, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_32 = QLabel(self.frame_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 15))
        self.label_32.setMaximumSize(QSize(16777215, 15))
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_23.addWidget(self.label_32)

        self.comboBox_3 = QComboBox(self.frame_10)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(368, 0))
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_23.addWidget(self.comboBox_3)


        self.gridLayout_2.addLayout(self.verticalLayout_23, 1, 0, 1, 2)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 15))
        self.label_33.setMaximumSize(QSize(16777215, 15))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_24.addWidget(self.label_33)

        self.comboBox_2 = QComboBox(self.frame_10)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(368, 0))
        self.comboBox_2.setMaximumSize(QSize(16777215, 50))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_24.addWidget(self.comboBox_2)


        self.gridLayout_2.addLayout(self.verticalLayout_24, 2, 0, 1, 2)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_34 = QLabel(self.frame_10)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 15))
        self.label_34.setMaximumSize(QSize(16777215, 15))
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_25.addWidget(self.label_34)

        self.lineEdit_8 = QLineEdit(self.frame_10)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(368, 0))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_25.addWidget(self.lineEdit_8)


        self.gridLayout_2.addLayout(self.verticalLayout_25, 3, 0, 1, 2)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_35 = QLabel(self.frame_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 15))
        self.label_35.setMaximumSize(QSize(16777215, 15))
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_26.addWidget(self.label_35)

        self.textEdit = QTextEdit(self.frame_10)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(368, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 100))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding: 15px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(242,242,242);\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(167,168,169);\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(99,101,105);\n"
"}")

        self.verticalLayout_26.addWidget(self.textEdit)


        self.gridLayout_2.addLayout(self.verticalLayout_26, 4, 0, 1, 2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnVoltar1 = QPushButton(self.frame_10)
        self.btnVoltar1.setObjectName(u"btnVoltar1")
        font8 = QFont()
        font8.setFamilies([u"KonsensLight"])
        self.btnVoltar1.setFont(font8)
        self.btnVoltar1.setStyleSheet(u"QPushButton {\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #d0d0d0;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
" 	font-size: 16px;\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #c0c0c0;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btnVoltar1)

        self.btn_DadosNcs = QPushButton(self.frame_10)
        self.btn_DadosNcs.setObjectName(u"btn_DadosNcs")
        self.btn_DadosNcs.setMaximumSize(QSize(16777215, 35))
        self.btn_DadosNcs.setFont(font7)
        self.btn_DadosNcs.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(133,50,117);\n"
"	color: white;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ab4c7d;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #550044;\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_DadosNcs)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 5, 0, 1, 2)


        self.horizontalLayout_17.addLayout(self.gridLayout_2)


        self.horizontalLayout_10.addWidget(self.frame_10)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_NC)
        self.page_Disp = QWidget()
        self.page_Disp.setObjectName(u"page_Disp")
        self.horizontalLayout_14 = QHBoxLayout(self.page_Disp)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_11 = QFrame(self.page_Disp)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(760, 342))
        self.frame_11.setMaximumSize(QSize(900, 600))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(340, 0))
        self.frame_12.setMaximumSize(QSize(340, 16777215))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_5 = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_19 = QLabel(self.frame_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(279, 32))
        self.label_19.setMaximumSize(QSize(279, 32))
        self.label_19.setStyleSheet(u"font: 20pt \"KonsensLight\";\n"
"color: #853275;")

        self.verticalLayout_13.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(279, 32))
        self.label_20.setMaximumSize(QSize(279, 32))
        self.label_20.setStyleSheet(u"font: 22pt \"KonsensBold\";\n"
"color: #853275;")

        self.verticalLayout_13.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(279, 32))
        self.label_21.setMaximumSize(QSize(279, 32))
        self.label_21.setStyleSheet(u"font: 20pt \"KonsensLight\";\n"
"color: #853275;")

        self.verticalLayout_13.addWidget(self.label_21)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(279, 121))
        self.label_22.setMaximumSize(QSize(279, 121))
        self.label_22.setStyleSheet(u"font: 10pt \"KonsensLight\";")
        self.label_22.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_22)

        self.verticalSpacer_6 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)


        self.horizontalLayout_12.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.frame_13)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 100))
        font9 = QFont()
        font9.setFamilies([u"KonsensBook"])
        font9.setPointSize(10)
        font9.setItalic(False)
        self.groupBox.setFont(font9)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-radius: 6px;\n"
"	margin-top: 6px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top center;\n"
"	padding: 0 3px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"}")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_2 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(85, 0))
        self.radioButton.setMaximumSize(QSize(85, 16777215))
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	padding-left: 15%;\n"
"}")
        self.radioButton.setCheckable(False)
        self.radioButton.setChecked(False)

        self.horizontalLayout_15.addWidget(self.radioButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(85, 0))
        self.radioButton_2.setMaximumSize(QSize(85, 16777215))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"	padding-left: 15%;\n"
"}")

        self.horizontalLayout_15.addWidget(self.radioButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.frame_13)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 100))
        self.groupBox_2.setMaximumSize(QSize(16777215, 100))
        font10 = QFont()
        font10.setFamilies([u"KonsensBook"])
        font10.setPointSize(10)
        self.groupBox_2.setFont(font10)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-radius: 6px;\n"
"	margin-top: 6px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top center;\n"
"	padding: 0 3px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_4 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(85, 0))
        self.radioButton_3.setMaximumSize(QSize(85, 16777215))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(u"padding-left: 15%;")

        self.horizontalLayout_16.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMinimumSize(QSize(85, 0))
        self.radioButton_4.setMaximumSize(QSize(85, 16777215))
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet(u"padding-left: 15%;")

        self.horizontalLayout_16.addWidget(self.radioButton_4)

        self.horizontalSpacer_5 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.frame_13)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setMinimumSize(QSize(0, 200))
        self.groupBox_3.setMaximumSize(QSize(16777215, 200))
        self.groupBox_3.setFont(font10)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-left: 1px solid transparent;\n"
"	border-right: 2px solid transparent;\n"
"	border-bottom: 1px solid transparent;\n"
"	margin-top: 6px;\n"
"	padding: 5px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	padding: 0 3px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 20, 10, 0)
        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        font11 = QFont()
        font11.setFamilies([u"KonsensBook"])
        font11.setPointSize(12)
        font11.setUnderline(False)
        self.checkBox.setFont(font11)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"")
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font11)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_5, 0, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_3)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setFont(font11)
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_9.setChecked(False)
        self.checkBox_9.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_9, 0, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font11)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font11)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_6.setChecked(False)
        self.checkBox_6.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_6, 1, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font11)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_7.setChecked(False)
        self.checkBox_7.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_7, 1, 2, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font11)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox_3)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font11)
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_8.setChecked(False)
        self.checkBox_8.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_8, 2, 1, 1, 2)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font11)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 1px solid #853275;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	background-color: #636569;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border: 1px solid #853275;\n"
"}")
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.checkBox_4, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 2)

        self.btnVoltar2 = QPushButton(self.frame_13)
        self.btnVoltar2.setObjectName(u"btnVoltar2")
        self.btnVoltar2.setFont(font8)
        self.btnVoltar2.setStyleSheet(u"QPushButton {\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #d0d0d0;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
" 	font-size: 16px;\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #c0c0c0;\n"
"}")

        self.gridLayout_4.addWidget(self.btnVoltar2, 3, 0, 1, 1)

        self.btn_Disposicao = QPushButton(self.frame_13)
        self.btn_Disposicao.setObjectName(u"btn_Disposicao")
        self.btn_Disposicao.setMaximumSize(QSize(16777215, 35))
        self.btn_Disposicao.setFont(font7)
        self.btn_Disposicao.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(133,50,117);\n"
"	color: white;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ab4c7d;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #550044;\n"
"}")

        self.gridLayout_4.addWidget(self.btn_Disposicao, 3, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_4)


        self.horizontalLayout_12.addWidget(self.frame_13)


        self.horizontalLayout_14.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_Disp)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 48))
        self.frame_3.setStyleSheet(u"background-color: #F9F8F9;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(745, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 44))
        self.label.setMaximumSize(QSize(200, 44))

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        StackedWidget.addWidget(self.page_add)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("StackedWidget", u"PESQUISAR", None))
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma categoria..", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Digite sua busca..", None))
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"BUSCAR", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("StackedWidget", u"FILTROS DE DATAS", None))
        self.label_36.setText(QCoreApplication.translate("StackedWidget", u"Per\u00edodo Inicial:", None))
        self.label_37.setText(QCoreApplication.translate("StackedWidget", u"Per\u00edodo Final:", None))
        self.pushButton_3.setText(QCoreApplication.translate("StackedWidget", u"BUSCAR", None))
        ___qtablewidgetitem = self.tab_dados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem1 = self.tab_dados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StackedWidget", u"ITEM", None));
        ___qtablewidgetitem2 = self.tab_dados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StackedWidget", u"ORDEM", None));
        ___qtablewidgetitem3 = self.tab_dados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StackedWidget", u"LOTE", None));
        ___qtablewidgetitem4 = self.tab_dados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StackedWidget", u"\u00c1REA RESPONS\u00c1VEL", None));
        ___qtablewidgetitem5 = self.tab_dados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StackedWidget", u"OPERA\u00c7\u00c3O", None));
        ___qtablewidgetitem6 = self.tab_dados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StackedWidget", u"MOTIVO", None));
        ___qtablewidgetitem7 = self.tab_dados.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("StackedWidget", u"QTDE.", None));
        ___qtablewidgetitem8 = self.tab_dados.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("StackedWidget", u"QTDE. REPROVADA", None));
        ___qtablewidgetitem9 = self.tab_dados.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("StackedWidget", u"ACAO", None));
        ___qtablewidgetitem10 = self.tab_dados.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("StackedWidget", u"DATA", None));
        ___qtablewidgetitem11 = self.tab_dados.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("StackedWidget", u"RESPONS\u00c1VEL", None));
        ___qtablewidgetitem12 = self.tab_dados.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("StackedWidget", u"S.RO", None));
        ___qtablewidgetitem13 = self.tab_dados.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("StackedWidget", u"OBSERVA\u00c7\u00c3O", None));
        self.btnAlterarRegistro.setText(QCoreApplication.translate("StackedWidget", u"ALTERAR", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"right\"><img src=\"images/neo_Logo1.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Deletar um registro", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Configura\u00e7\u00f5es", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"1", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"Dados Gerais", None))
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"2", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"Dados da Ncs", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"3", None))
        self.label_10.setText(QCoreApplication.translate("StackedWidget", u"Disposi\u00e7\u00e3o", None))
        self.label_11.setText(QCoreApplication.translate("StackedWidget", u"Preencha os", None))
        self.label_12.setText(QCoreApplication.translate("StackedWidget", u"DADOS GERAIS", None))
        self.label_13.setText(QCoreApplication.translate("StackedWidget", u"da N\u00e3o Conformidade", None))
        self.label_14.setText(QCoreApplication.translate("StackedWidget", u"Informe corretamente todos os dados  da ordem para evitar informa\u00e7\u00f5es divergentes nos indicadores, qualquer d\u00favida falar com seu L\u00edder direto.", None))
        self.label_23.setText(QCoreApplication.translate("StackedWidget", u"Data:*", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"01/01/2024", None))
        self.label_24.setText(QCoreApplication.translate("StackedWidget", u"Planta:*", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"4400 / 4401", None))
        self.label_25.setText(QCoreApplication.translate("StackedWidget", u"Ordem:*", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"501020304", None))
        self.label_26.setText(QCoreApplication.translate("StackedWidget", u"Lote:*", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"ABC12", None))
        self.label_27.setText(QCoreApplication.translate("StackedWidget", u"Item:*", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"109.XXX-X", None))
        self.label_28.setText(QCoreApplication.translate("StackedWidget", u"\u00c1rea Respons\u00e1vel pela identifica\u00e7\u00e3o:*", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("StackedWidget", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("StackedWidget", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("StackedWidget", u"3", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_29.setText(QCoreApplication.translate("StackedWidget", u"Respons\u00e1vel pela identifica\u00e7\u00e3o:*", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"u123XXX", None))
        self.btn_DadoGerais.setText(QCoreApplication.translate("StackedWidget", u"AVAN\u00c7AR", None))
        self.label_15.setText(QCoreApplication.translate("StackedWidget", u"Preencha os", None))
        self.label_16.setText(QCoreApplication.translate("StackedWidget", u"DADOS DA NCs", None))
        self.label_17.setText(QCoreApplication.translate("StackedWidget", u"da N\u00e3o Conformidade", None))
        self.label_18.setText(QCoreApplication.translate("StackedWidget", u"Informe corretamente todos os dados  da N\u00e3o Conformidade para evitar informa\u00e7\u00f5es divergentes nos indicadores, qualquer d\u00favida falar com seu L\u00edder direto.", None))
        self.label_30.setText(QCoreApplication.translate("StackedWidget", u"Qtde. Total:*", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"100", None))
        self.label_31.setText(QCoreApplication.translate("StackedWidget", u"Qtde. Reprovada:*", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"50", None))
        self.label_32.setText(QCoreApplication.translate("StackedWidget", u"\u00c1res respons\u00e1vel da NC:*", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_33.setText(QCoreApplication.translate("StackedWidget", u"Motivo da NC:*", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_34.setText(QCoreApplication.translate("StackedWidget", u"A\u00e7\u00e3o a ser tomada:*", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Retornou ao setor respons\u00e1vel", None))
        self.label_35.setText(QCoreApplication.translate("StackedWidget", u"Observa\u00e7\u00f5es:", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Escreva algo aqui..", None))
        self.btnVoltar1.setText(QCoreApplication.translate("StackedWidget", u"VOLTAR", None))
        self.btn_DadosNcs.setText(QCoreApplication.translate("StackedWidget", u"AVAN\u00c7AR", None))
        self.label_19.setText(QCoreApplication.translate("StackedWidget", u"Preencha a", None))
        self.label_20.setText(QCoreApplication.translate("StackedWidget", u"DISPOSI\u00c7\u00c3O", None))
        self.label_21.setText(QCoreApplication.translate("StackedWidget", u"da N\u00e3o Conformidade", None))
        self.label_22.setText(QCoreApplication.translate("StackedWidget", u"Informe corretamente a disposi\u00e7\u00e3o final da ordem para evitar processos faltantes durante a tratativa da n\u00e3o conformidade, qualquer d\u00favida falar com seu L\u00edder direto.", None))
        self.groupBox.setTitle(QCoreApplication.translate("StackedWidget", u"Deseja abrir S.RO?", None))
        self.radioButton.setText(QCoreApplication.translate("StackedWidget", u"SIM", None))
        self.radioButton_2.setText(QCoreApplication.translate("StackedWidget", u"N\u00c3O", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("StackedWidget", u"Deseja enviar por e-mail?", None))
        self.radioButton_3.setText(QCoreApplication.translate("StackedWidget", u"SIM", None))
        self.radioButton_4.setText(QCoreApplication.translate("StackedWidget", u"N\u00c3O", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("StackedWidget", u"Selecione os e-mails que deseja enviar:", None))
        self.checkBox.setText(QCoreApplication.translate("StackedWidget", u"Acabamento", None))
        self.checkBox_5.setText(QCoreApplication.translate("StackedWidget", u"TNC", None))
        self.checkBox_9.setText(QCoreApplication.translate("StackedWidget", u"CNC", None))
        self.checkBox_2.setText(QCoreApplication.translate("StackedWidget", u"Higieniza\u00e7\u00e3o", None))
        self.checkBox_6.setText(QCoreApplication.translate("StackedWidget", u"Recebimento", None))
        self.checkBox_7.setText(QCoreApplication.translate("StackedWidget", u"Usinagem", None))
        self.checkBox_3.setText(QCoreApplication.translate("StackedWidget", u"TRS", None))
        self.checkBox_8.setText(QCoreApplication.translate("StackedWidget", u"USI - Analista e L\u00edderes", None))
        self.checkBox_4.setText(QCoreApplication.translate("StackedWidget", u"PCP", None))
        self.btnVoltar2.setText(QCoreApplication.translate("StackedWidget", u"VOLTAR", None))
        self.btn_Disposicao.setText(QCoreApplication.translate("StackedWidget", u"SALVAR", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"right\"><img src=\"images/neo_Logo1.png\"/></p></body></html>", None))
    # retranslateUi

