# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagestzsozv.ui'
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
        StackedWidget.resize(970, 666)
        StackedWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"KonsensRegular"])
        font.setPointSize(12)
        StackedWidget.setFont(font)
        StackedWidget.setStyleSheet(u"background-color: #F9F8F9;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout = QVBoxLayout(self.page_home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.page_home)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMaximumSize(QSize(16777215, 60))
        self.frame_25.setStyleSheet(u"background-color: #F4F4F4;;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_25)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(150, 44))
        self.label_39.setMaximumSize(QSize(150, 44))

        self.horizontalLayout_25.addWidget(self.label_39, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.page_home)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: #F4F4F4;;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_21 = QFrame(self.frame_26)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QSize(950, 600))
        self.frame_21.setMaximumSize(QSize(1000, 600))
        self.frame_21.setStyleSheet(u"background-color: #F4F4F4;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_21)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-110, -50, 1400, 400))
        self.label_3.setMinimumSize(QSize(1400, 400))
        self.label_3.setMaximumSize(QSize(16777215, 400))
        self.label_38 = QLabel(self.frame_21)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(100, 40, 281, 251))
        self.label_38.setStyleSheet(u"background-color: transparent;")
        self.widget = QWidget(self.frame_21)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 300, 950, 250))
        self.widget.setMinimumSize(QSize(950, 250))
        self.widget.setMaximumSize(QSize(1000, 250))
        self.widget.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_27 = QHBoxLayout(self.widget)
        self.horizontalLayout_27.setSpacing(30)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_aparencia = QFrame(self.widget)
        self.frame_aparencia.setObjectName(u"frame_aparencia")
        self.frame_aparencia.setMinimumSize(QSize(250, 250))
        self.frame_aparencia.setMaximumSize(QSize(250, 250))
        self.frame_aparencia.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_aparencia.setStyleSheet(u"QFrame {\n"
"	border-radius: 3px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frame_aparencia:hover {\n"
"	border: 1px solid #636569;\n"
"}")
        self.frame_aparencia.setFrameShape(QFrame.StyledPanel)
        self.frame_aparencia.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_aparencia)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 5, 0, 20)
        self.label_40 = QLabel(self.frame_aparencia)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(110, 100))
        self.label_40.setMaximumSize(QSize(110, 100))

        self.verticalLayout_32.addWidget(self.label_40, 0, Qt.AlignHCenter)

        self.label_41 = QLabel(self.frame_aparencia)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(200, 0))
        self.label_41.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"KonsensBold"])
        font1.setPointSize(16)
        self.label_41.setFont(font1)
        self.label_41.setStyleSheet(u"QLabel {\n"
"	color: #A7A8A9;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #853275;\n"
"}")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_41, 0, Qt.AlignHCenter)

        self.label_42 = QLabel(self.frame_aparencia)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(200, 0))
        self.label_42.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(9)
        self.label_42.setFont(font2)
        self.label_42.setStyleSheet(u"QLabel {\n"
"	color: #636569;\n"
"}")
        self.label_42.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_42.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.label_42, 0, Qt.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.frame_aparencia)

        self.frm_rapidez = QFrame(self.widget)
        self.frm_rapidez.setObjectName(u"frm_rapidez")
        self.frm_rapidez.setMinimumSize(QSize(250, 250))
        self.frm_rapidez.setMaximumSize(QSize(250, 250))
        self.frm_rapidez.setCursor(QCursor(Qt.PointingHandCursor))
        self.frm_rapidez.setStyleSheet(u"QFrame {\n"
"	border-radius: 3px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frm_rapidez:hover {\n"
"	border: 1px solid #636569;\n"
"}")
        self.frm_rapidez.setFrameShape(QFrame.StyledPanel)
        self.frm_rapidez.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frm_rapidez)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 5, 0, 20)
        self.label_43 = QLabel(self.frm_rapidez)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(110, 100))
        self.label_43.setMaximumSize(QSize(110, 100))

        self.verticalLayout_33.addWidget(self.label_43, 0, Qt.AlignHCenter)

        self.label_44 = QLabel(self.frm_rapidez)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(200, 0))
        self.label_44.setMaximumSize(QSize(200, 16777215))
        self.label_44.setFont(font1)
        self.label_44.setStyleSheet(u"QLabel {\n"
"	color: #A7A8A9;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #853275;\n"
"}")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_44, 0, Qt.AlignHCenter)

        self.label_45 = QLabel(self.frm_rapidez)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(200, 0))
        self.label_45.setMaximumSize(QSize(200, 16777215))
        self.label_45.setFont(font2)
        self.label_45.setStyleSheet(u"QLabel {\n"
"	color: #636569;\n"
"}")
        self.label_45.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_45.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.label_45, 0, Qt.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.frm_rapidez)

        self.frm_duvidas = QFrame(self.widget)
        self.frm_duvidas.setObjectName(u"frm_duvidas")
        self.frm_duvidas.setMinimumSize(QSize(250, 250))
        self.frm_duvidas.setMaximumSize(QSize(250, 250))
        self.frm_duvidas.setCursor(QCursor(Qt.PointingHandCursor))
        self.frm_duvidas.setStyleSheet(u"QFrame {\n"
"	border-radius: 3px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame#frm_duvidas:hover {\n"
"	border: 1px solid #636569;\n"
"}")
        self.frm_duvidas.setFrameShape(QFrame.StyledPanel)
        self.frm_duvidas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frm_duvidas)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 5, 0, 20)
        self.label_46 = QLabel(self.frm_duvidas)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(110, 100))
        self.label_46.setMaximumSize(QSize(110, 100))

        self.verticalLayout_34.addWidget(self.label_46, 0, Qt.AlignHCenter)

        self.label_47 = QLabel(self.frm_duvidas)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(200, 0))
        self.label_47.setMaximumSize(QSize(200, 16777215))
        self.label_47.setFont(font1)
        self.label_47.setStyleSheet(u"QLabel {\n"
"	color: #A7A8A9;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: #853275;\n"
"}")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_47, 0, Qt.AlignHCenter)

        self.label_48 = QLabel(self.frm_duvidas)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(200, 0))
        self.label_48.setMaximumSize(QSize(200, 16777215))
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"QLabel {\n"
"	color: #636569;\n"
"}")
        self.label_48.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_48.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.label_48, 0, Qt.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.frm_duvidas)


        self.horizontalLayout_26.addWidget(self.frame_21, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_26)

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
        font3 = QFont()
        font3.setFamilies([u"KonsensBook"])
        font3.setPointSize(8)
        self.groupBox_4.setFont(font3)
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
        self.cmb_catgPergunta = QComboBox(self.groupBox_4)
        self.cmb_catgPergunta.setObjectName(u"cmb_catgPergunta")
        self.cmb_catgPergunta.setMinimumSize(QSize(250, 30))
        self.cmb_catgPergunta.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Trebuchet MS"])
        font4.setPointSize(10)
        self.cmb_catgPergunta.setFont(font4)
        self.cmb_catgPergunta.setStyleSheet(u"QComboBox {\n"
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

        self.gridLayout_5.addWidget(self.cmb_catgPergunta, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.text_pergunta = QLineEdit(self.groupBox_4)
        self.text_pergunta.setObjectName(u"text_pergunta")
        self.text_pergunta.setMinimumSize(QSize(250, 30))
        self.text_pergunta.setMaximumSize(QSize(16777215, 30))
        self.text_pergunta.setFont(font4)
        self.text_pergunta.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_5.addWidget(self.text_pergunta, 1, 0, 1, 1)

        self.btn_buscarGeral = QPushButton(self.groupBox_4)
        self.btn_buscarGeral.setObjectName(u"btn_buscarGeral")
        font5 = QFont()
        font5.setFamilies([u"KonsensBook"])
        self.btn_buscarGeral.setFont(font5)
        self.btn_buscarGeral.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_5.addWidget(self.btn_buscarGeral, 1, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.groupBox_4)

        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.groupBox_5 = QGroupBox(self.frame_15)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 400))
        self.groupBox_5.setFont(font3)
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
        font6 = QFont()
        font6.setFamilies([u"Trebuchet MS"])
        font6.setPointSize(8)
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_28.addWidget(self.label_36)

        self.pesq_periodoInicial = QDateEdit(self.groupBox_5)
        self.pesq_periodoInicial.setObjectName(u"pesq_periodoInicial")
        self.pesq_periodoInicial.setMinimumSize(QSize(250, 30))
        self.pesq_periodoInicial.setMaximumSize(QSize(16777215, 30))
        self.pesq_periodoInicial.setFont(font4)
        self.pesq_periodoInicial.setStyleSheet(u"QDateEdit {\n"
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
        self.pesq_periodoInicial.setMinimumDate(QDate(2023, 1, 1))
        self.pesq_periodoInicial.setDate(QDate(2023, 1, 1))

        self.verticalLayout_28.addWidget(self.pesq_periodoInicial)


        self.gridLayout_6.addLayout(self.verticalLayout_28, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(91, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_37 = QLabel(self.groupBox_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font6)
        self.label_37.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_29.addWidget(self.label_37)

        self.pesq_periodoFinal = QDateEdit(self.groupBox_5)
        self.pesq_periodoFinal.setObjectName(u"pesq_periodoFinal")
        self.pesq_periodoFinal.setMinimumSize(QSize(250, 30))
        self.pesq_periodoFinal.setMaximumSize(QSize(16777215, 30))
        self.pesq_periodoFinal.setFont(font4)
        self.pesq_periodoFinal.setStyleSheet(u"QDateEdit {\n"
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
        self.pesq_periodoFinal.setMinimumDate(QDate(2023, 1, 1))
        self.pesq_periodoFinal.setDate(QDate(2023, 1, 1))

        self.verticalLayout_29.addWidget(self.pesq_periodoFinal)


        self.gridLayout_6.addLayout(self.verticalLayout_29, 1, 0, 2, 1)

        self.btn_buscarPeriodo = QPushButton(self.groupBox_5)
        self.btn_buscarPeriodo.setObjectName(u"btn_buscarPeriodo")
        self.btn_buscarPeriodo.setFont(font5)
        self.btn_buscarPeriodo.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_6.addWidget(self.btn_buscarPeriodo, 2, 1, 1, 1)


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
        if (self.tab_dados.rowCount() < 10):
            self.tab_dados.setRowCount(10)
        self.tab_dados.setObjectName(u"tab_dados")
        font7 = QFont()
        font7.setFamilies([u"KonsensBook"])
        font7.setPointSize(12)
        self.tab_dados.setFont(font7)
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
        self.tab_dados.setRowCount(10)
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
        self.lbl_totalRegistros = QLabel(self.frame_14)
        self.lbl_totalRegistros.setObjectName(u"lbl_totalRegistros")
        self.lbl_totalRegistros.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamilies([u"Trebuchet MS"])
        self.lbl_totalRegistros.setFont(font8)

        self.verticalLayout_27.addWidget(self.lbl_totalRegistros)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_7)

        self.btn_limparFiltros = QPushButton(self.frame_14)
        self.btn_limparFiltros.setObjectName(u"btn_limparFiltros")
        self.btn_limparFiltros.setEnabled(True)
        self.btn_limparFiltros.setMaximumSize(QSize(16777215, 30))
        self.btn_limparFiltros.setFont(font2)
        self.btn_limparFiltros.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_limparFiltros.setLayoutDirection(Qt.LeftToRight)
        self.btn_limparFiltros.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	color: #636569;\n"
"	padding: 5px;\n"
"	border: None;\n"
"	text-align: center;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	color: #853275;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: #A7A8A9;\n"
"}")
        self.btn_limparFiltros.setCheckable(False)

        self.verticalLayout_27.addWidget(self.btn_limparFiltros)

        self.btnAlterarRegistro = QPushButton(self.frame_14)
        self.btnAlterarRegistro.setObjectName(u"btnAlterarRegistro")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnAlterarRegistro.sizePolicy().hasHeightForWidth())
        self.btnAlterarRegistro.setSizePolicy(sizePolicy1)
        self.btnAlterarRegistro.setFont(font4)
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
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.page_del)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: #F9F8F9;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_18)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMinimumSize(QSize(0, 120))
        self.frame_19.setMaximumSize(QSize(16777215, 120))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(280, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_13)

        self.grpBusca_del = QGroupBox(self.frame_19)
        self.grpBusca_del.setObjectName(u"grpBusca_del")
        self.grpBusca_del.setMinimumSize(QSize(400, 100))
        self.grpBusca_del.setMaximumSize(QSize(400, 100))
        font9 = QFont()
        font9.setFamilies([u"KonsensBook"])
        font9.setPointSize(10)
        self.grpBusca_del.setFont(font9)
        self.grpBusca_del.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid rgb(99,101,105);\n"
"	border-radius: 3px;\n"
"	margin-top: 6px;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-position: top center;\n"
"	padding: 0 30px;\n"
"	background-color: rgb(99,101,105);\n"
"	color: white;\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.grpBusca_del)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 15, 0, 0)
        self.txtBuscar_del = QLineEdit(self.grpBusca_del)
        self.txtBuscar_del.setObjectName(u"txtBuscar_del")
        self.txtBuscar_del.setMinimumSize(QSize(230, 30))
        self.txtBuscar_del.setMaximumSize(QSize(230, 30))
        self.txtBuscar_del.setFont(font4)
        self.txtBuscar_del.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_22.addWidget(self.txtBuscar_del)

        self.btnBuscar_del = QPushButton(self.grpBusca_del)
        self.btnBuscar_del.setObjectName(u"btnBuscar_del")
        self.btnBuscar_del.setMinimumSize(QSize(90, 25))
        self.btnBuscar_del.setMaximumSize(QSize(90, 25))
        self.btnBuscar_del.setFont(font5)
        self.btnBuscar_del.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_22.addWidget(self.btnBuscar_del)


        self.horizontalLayout_23.addWidget(self.grpBusca_del)

        self.horizontalSpacer_14 = QSpacerItem(280, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_14)


        self.verticalLayout_30.addWidget(self.frame_19)

        self.tabDados_del = QTableWidget(self.frame_18)
        if (self.tabDados_del.columnCount() < 14):
            self.tabDados_del.setColumnCount(14)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(8, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(9, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(10, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(11, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(12, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabDados_del.setHorizontalHeaderItem(13, __qtablewidgetitem27)
        if (self.tabDados_del.rowCount() < 11):
            self.tabDados_del.setRowCount(11)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setCheckState(Qt.Unchecked);
        self.tabDados_del.setItem(0, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 10, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 11, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 12, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabDados_del.setItem(0, 13, __qtablewidgetitem41)
        self.tabDados_del.setObjectName(u"tabDados_del")
        self.tabDados_del.setFont(font7)
        self.tabDados_del.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tabDados_del.setStyleSheet(u"QTableWidget  {\n"
"	background-color: #f5f5f5;\n"
"	border: 1px solid rgb(99,101,105);\n"
"	gridline-color: #d1d1d1;\n"
"	selection-background-color: #a6a6a6;\n"
"	margin-bottom: 10px;\n"
"	margin-left: 5px;\n"
"	margin-right: 5px;\n"
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
        self.tabDados_del.setFrameShape(QFrame.NoFrame)
        self.tabDados_del.setFrameShadow(QFrame.Sunken)
        self.tabDados_del.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabDados_del.setTabKeyNavigation(True)
        self.tabDados_del.setDragEnabled(False)
        self.tabDados_del.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabDados_del.setGridStyle(Qt.SolidLine)
        self.tabDados_del.setRowCount(11)
        self.tabDados_del.horizontalHeader().setVisible(True)
        self.tabDados_del.horizontalHeader().setCascadingSectionResizes(False)
        self.tabDados_del.horizontalHeader().setMinimumSectionSize(100)
        self.tabDados_del.horizontalHeader().setDefaultSectionSize(130)
        self.tabDados_del.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabDados_del.verticalHeader().setVisible(False)
        self.tabDados_del.verticalHeader().setHighlightSections(False)

        self.verticalLayout_30.addWidget(self.tabDados_del)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 40))
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.lblTotalRegistros_Del = QLabel(self.frame_20)
        self.lblTotalRegistros_Del.setObjectName(u"lblTotalRegistros_Del")
        self.lblTotalRegistros_Del.setMinimumSize(QSize(130, 15))
        self.lblTotalRegistros_Del.setMaximumSize(QSize(200, 15))
        self.lblTotalRegistros_Del.setFont(font8)

        self.verticalLayout_31.addWidget(self.lblTotalRegistros_Del)

        self.verticalSpacer_8 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_8)


        self.horizontalLayout_24.addLayout(self.verticalLayout_31)

        self.horizontalSpacer_15 = QSpacerItem(631, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_15)

        self.btnDeleteRegister = QPushButton(self.frame_20)
        self.btnDeleteRegister.setObjectName(u"btnDeleteRegister")
        sizePolicy1.setHeightForWidth(self.btnDeleteRegister.sizePolicy().hasHeightForWidth())
        self.btnDeleteRegister.setSizePolicy(sizePolicy1)
        self.btnDeleteRegister.setMinimumSize(QSize(180, 35))
        self.btnDeleteRegister.setMaximumSize(QSize(180, 35))
        self.btnDeleteRegister.setFont(font4)
        self.btnDeleteRegister.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDeleteRegister.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border: 1px solid red;\n"
"	color: red;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: red;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #76777A;\n"
"	border: 1px solid #76777A;\n"
"}")

        self.horizontalLayout_24.addWidget(self.btnDeleteRegister)


        self.verticalLayout_30.addWidget(self.frame_20)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.page_del)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 48))
        self.frame_17.setStyleSheet(u"background-color: #F9F8F9;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(745, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_12)

        self.logoNeo_del = QLabel(self.frame_17)
        self.logoNeo_del.setObjectName(u"logoNeo_del")
        self.logoNeo_del.setMinimumSize(QSize(50, 44))
        self.logoNeo_del.setMaximumSize(QSize(200, 44))

        self.horizontalLayout_21.addWidget(self.logoNeo_del)


        self.verticalLayout_3.addWidget(self.frame_17)

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
        font10 = QFont()
        font10.setFamilies([u"KonsensRegular"])
        font10.setPointSize(11)
        self.label_8.setFont(font10)

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
        self.label_9.setFont(font10)
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
        self.label_10.setFont(font10)
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

        self.text_data = QLineEdit(self.frame_7)
        self.text_data.setObjectName(u"text_data")
        self.text_data.setMaximumSize(QSize(16777215, 50))
        self.text_data.setFont(font)
        self.text_data.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_14.addWidget(self.text_data)


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

        self.text_planta = QLineEdit(self.frame_7)
        self.text_planta.setObjectName(u"text_planta")
        self.text_planta.setMaximumSize(QSize(16777215, 50))
        self.text_planta.setFont(font)
        self.text_planta.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_15.addWidget(self.text_planta)


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

        self.text_ordem = QLineEdit(self.frame_7)
        self.text_ordem.setObjectName(u"text_ordem")
        self.text_ordem.setMinimumSize(QSize(368, 0))
        self.text_ordem.setMaximumSize(QSize(16777215, 50))
        self.text_ordem.setFont(font)
        self.text_ordem.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_16.addWidget(self.text_ordem)


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

        self.text_lote = QLineEdit(self.frame_7)
        self.text_lote.setObjectName(u"text_lote")
        self.text_lote.setMaximumSize(QSize(16777215, 50))
        self.text_lote.setFont(font)
        self.text_lote.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_17.addWidget(self.text_lote)


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

        self.text_item = QLineEdit(self.frame_7)
        self.text_item.setObjectName(u"text_item")
        self.text_item.setMaximumSize(QSize(16777215, 50))
        self.text_item.setFont(font)
        self.text_item.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_18.addWidget(self.text_item)


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

        self.cmb_areaResp = QComboBox(self.frame_7)
        self.cmb_areaResp.setObjectName(u"cmb_areaResp")
        self.cmb_areaResp.setMinimumSize(QSize(368, 0))
        self.cmb_areaResp.setMaximumSize(QSize(16777215, 50))
        self.cmb_areaResp.setFont(font)
        self.cmb_areaResp.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_19.addWidget(self.cmb_areaResp)


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

        self.text_respIden = QLineEdit(self.frame_7)
        self.text_respIden.setObjectName(u"text_respIden")
        self.text_respIden.setMinimumSize(QSize(368, 0))
        self.text_respIden.setMaximumSize(QSize(16777215, 50))
        self.text_respIden.setFont(font)
        self.text_respIden.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_20.addWidget(self.text_respIden)


        self.gridLayout.addLayout(self.verticalLayout_20, 4, 0, 1, 2)

        self.btn_DadoGerais = QPushButton(self.frame_7)
        self.btn_DadoGerais.setObjectName(u"btn_DadoGerais")
        self.btn_DadoGerais.setMaximumSize(QSize(16777215, 35))
        font11 = QFont()
        font11.setFamilies([u"KonsensBold"])
        font11.setPointSize(12)
        self.btn_DadoGerais.setFont(font11)
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

        self.text_qtde = QLineEdit(self.frame_10)
        self.text_qtde.setObjectName(u"text_qtde")
        self.text_qtde.setMaximumSize(QSize(16777215, 50))
        self.text_qtde.setFont(font)
        self.text_qtde.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_21.addWidget(self.text_qtde)


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

        self.text_qtdeRep = QLineEdit(self.frame_10)
        self.text_qtdeRep.setObjectName(u"text_qtdeRep")
        self.text_qtdeRep.setMaximumSize(QSize(16777215, 50))
        self.text_qtdeRep.setFont(font)
        self.text_qtdeRep.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_22.addWidget(self.text_qtdeRep)


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

        self.cmb_areaNC = QComboBox(self.frame_10)
        self.cmb_areaNC.setObjectName(u"cmb_areaNC")
        self.cmb_areaNC.setMinimumSize(QSize(368, 0))
        self.cmb_areaNC.setFont(font)
        self.cmb_areaNC.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_23.addWidget(self.cmb_areaNC)


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

        self.cmb_Motivos = QComboBox(self.frame_10)
        self.cmb_Motivos.setObjectName(u"cmb_Motivos")
        self.cmb_Motivos.setMinimumSize(QSize(368, 0))
        self.cmb_Motivos.setMaximumSize(QSize(16777215, 50))
        self.cmb_Motivos.setFont(font)
        self.cmb_Motivos.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_24.addWidget(self.cmb_Motivos)


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

        self.text_acao = QLineEdit(self.frame_10)
        self.text_acao.setObjectName(u"text_acao")
        self.text_acao.setMinimumSize(QSize(368, 0))
        self.text_acao.setMaximumSize(QSize(16777215, 50))
        self.text_acao.setFont(font)
        self.text_acao.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_25.addWidget(self.text_acao)


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

        self.text_Obs = QTextEdit(self.frame_10)
        self.text_Obs.setObjectName(u"text_Obs")
        self.text_Obs.setMinimumSize(QSize(368, 100))
        self.text_Obs.setMaximumSize(QSize(16777215, 100))
        self.text_Obs.setFont(font)
        self.text_Obs.setStyleSheet(u"QTextEdit {\n"
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

        self.verticalLayout_26.addWidget(self.text_Obs)


        self.gridLayout_2.addLayout(self.verticalLayout_26, 4, 0, 1, 2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnVoltar1 = QPushButton(self.frame_10)
        self.btnVoltar1.setObjectName(u"btnVoltar1")
        font12 = QFont()
        font12.setFamilies([u"KonsensLight"])
        self.btnVoltar1.setFont(font12)
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
        self.btn_DadosNcs.setFont(font11)
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
        self.group_SRo = QGroupBox(self.frame_13)
        self.group_SRo.setObjectName(u"group_SRo")
        self.group_SRo.setMinimumSize(QSize(0, 100))
        self.group_SRo.setMaximumSize(QSize(16777215, 100))
        font13 = QFont()
        font13.setFamilies([u"KonsensBook"])
        font13.setPointSize(10)
        font13.setItalic(False)
        self.group_SRo.setFont(font13)
        self.group_SRo.setStyleSheet(u"QGroupBox {\n"
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
        self.group_SRo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.group_SRo.setFlat(False)
        self.group_SRo.setCheckable(False)
        self.horizontalLayout_15 = QHBoxLayout(self.group_SRo)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_2 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)

        self.btnSimRo = QRadioButton(self.group_SRo)
        self.btnSimRo.setObjectName(u"btnSimRo")
        self.btnSimRo.setMinimumSize(QSize(85, 0))
        self.btnSimRo.setMaximumSize(QSize(85, 16777215))
        self.btnSimRo.setFont(font)
        self.btnSimRo.setStyleSheet(u"QRadioButton {\n"
"	padding-left: 15%;\n"
"}")
        self.btnSimRo.setCheckable(True)
        self.btnSimRo.setChecked(False)

        self.horizontalLayout_15.addWidget(self.btnSimRo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btnNaoRo = QRadioButton(self.group_SRo)
        self.btnNaoRo.setObjectName(u"btnNaoRo")
        self.btnNaoRo.setMinimumSize(QSize(85, 0))
        self.btnNaoRo.setMaximumSize(QSize(85, 16777215))
        self.btnNaoRo.setFont(font)
        self.btnNaoRo.setStyleSheet(u"QRadioButton {\n"
"	padding-left: 15%;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btnNaoRo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addWidget(self.group_SRo, 0, 0, 1, 2)

        self.group_Email = QGroupBox(self.frame_13)
        self.group_Email.setObjectName(u"group_Email")
        self.group_Email.setMinimumSize(QSize(0, 100))
        self.group_Email.setMaximumSize(QSize(16777215, 100))
        self.group_Email.setFont(font9)
        self.group_Email.setStyleSheet(u"QGroupBox {\n"
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
        self.horizontalLayout_16 = QHBoxLayout(self.group_Email)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_4 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.btn_SimEmail = QRadioButton(self.group_Email)
        self.btn_SimEmail.setObjectName(u"btn_SimEmail")
        self.btn_SimEmail.setMinimumSize(QSize(85, 0))
        self.btn_SimEmail.setMaximumSize(QSize(85, 16777215))
        self.btn_SimEmail.setFont(font)
        self.btn_SimEmail.setStyleSheet(u"padding-left: 15%;")

        self.horizontalLayout_16.addWidget(self.btn_SimEmail)

        self.btn_NaoEmail = QRadioButton(self.group_Email)
        self.btn_NaoEmail.setObjectName(u"btn_NaoEmail")
        self.btn_NaoEmail.setMinimumSize(QSize(85, 0))
        self.btn_NaoEmail.setMaximumSize(QSize(85, 16777215))
        self.btn_NaoEmail.setFont(font)
        self.btn_NaoEmail.setStyleSheet(u"padding-left: 15%;")

        self.horizontalLayout_16.addWidget(self.btn_NaoEmail)

        self.horizontalSpacer_5 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)


        self.gridLayout_4.addWidget(self.group_Email, 1, 0, 1, 2)

        self.group_addressEmail = QGroupBox(self.frame_13)
        self.group_addressEmail.setObjectName(u"group_addressEmail")
        self.group_addressEmail.setEnabled(True)
        self.group_addressEmail.setMinimumSize(QSize(0, 200))
        self.group_addressEmail.setMaximumSize(QSize(16777215, 200))
        self.group_addressEmail.setFont(font9)
        self.group_addressEmail.setStyleSheet(u"QGroupBox {\n"
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
        self.gridLayout_3 = QGridLayout(self.group_addressEmail)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 20, 10, 0)
        self.check_acabamento = QCheckBox(self.group_addressEmail)
        self.check_acabamento.setObjectName(u"check_acabamento")
        self.check_acabamento.setEnabled(True)
        font14 = QFont()
        font14.setFamilies([u"KonsensBook"])
        font14.setPointSize(12)
        font14.setUnderline(False)
        self.check_acabamento.setFont(font14)
        self.check_acabamento.setStyleSheet(u"QCheckBox {\n"
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
        self.check_acabamento.setChecked(False)
        self.check_acabamento.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_acabamento, 0, 0, 1, 1)

        self.check_tnc = QCheckBox(self.group_addressEmail)
        self.check_tnc.setObjectName(u"check_tnc")
        self.check_tnc.setFont(font14)
        self.check_tnc.setStyleSheet(u"QCheckBox {\n"
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
        self.check_tnc.setChecked(False)
        self.check_tnc.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_tnc, 0, 1, 1, 1)

        self.check_cnc = QCheckBox(self.group_addressEmail)
        self.check_cnc.setObjectName(u"check_cnc")
        self.check_cnc.setFont(font14)
        self.check_cnc.setStyleSheet(u"QCheckBox {\n"
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
        self.check_cnc.setChecked(False)
        self.check_cnc.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_cnc, 0, 2, 1, 1)

        self.check_higienizacao = QCheckBox(self.group_addressEmail)
        self.check_higienizacao.setObjectName(u"check_higienizacao")
        self.check_higienizacao.setFont(font14)
        self.check_higienizacao.setStyleSheet(u"QCheckBox {\n"
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
        self.check_higienizacao.setChecked(False)
        self.check_higienizacao.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_higienizacao, 1, 0, 1, 1)

        self.check_recebimento = QCheckBox(self.group_addressEmail)
        self.check_recebimento.setObjectName(u"check_recebimento")
        self.check_recebimento.setFont(font14)
        self.check_recebimento.setStyleSheet(u"QCheckBox {\n"
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
        self.check_recebimento.setChecked(False)
        self.check_recebimento.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_recebimento, 1, 1, 1, 1)

        self.check_usinagem = QCheckBox(self.group_addressEmail)
        self.check_usinagem.setObjectName(u"check_usinagem")
        self.check_usinagem.setFont(font14)
        self.check_usinagem.setStyleSheet(u"QCheckBox {\n"
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
        self.check_usinagem.setChecked(False)
        self.check_usinagem.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_usinagem, 1, 2, 1, 1)

        self.check_trs = QCheckBox(self.group_addressEmail)
        self.check_trs.setObjectName(u"check_trs")
        self.check_trs.setFont(font14)
        self.check_trs.setStyleSheet(u"QCheckBox {\n"
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
        self.check_trs.setChecked(False)
        self.check_trs.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_trs, 2, 0, 1, 1)

        self.check_usiAnaLid = QCheckBox(self.group_addressEmail)
        self.check_usiAnaLid.setObjectName(u"check_usiAnaLid")
        self.check_usiAnaLid.setFont(font14)
        self.check_usiAnaLid.setStyleSheet(u"QCheckBox {\n"
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
        self.check_usiAnaLid.setChecked(False)
        self.check_usiAnaLid.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_usiAnaLid, 2, 1, 1, 2)

        self.check_pcp = QCheckBox(self.group_addressEmail)
        self.check_pcp.setObjectName(u"check_pcp")
        self.check_pcp.setFont(font14)
        self.check_pcp.setStyleSheet(u"QCheckBox {\n"
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
        self.check_pcp.setChecked(False)
        self.check_pcp.setAutoRepeat(False)

        self.gridLayout_3.addWidget(self.check_pcp, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.group_addressEmail, 2, 0, 1, 2)

        self.btnVoltar2 = QPushButton(self.frame_13)
        self.btnVoltar2.setObjectName(u"btnVoltar2")
        self.btnVoltar2.setFont(font12)
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
        self.btn_Disposicao.setFont(font11)
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

        StackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_39.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"right\"><img src=\"images/neo_Logo1.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><img src=\"images/background_image.png\"/></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><img src=\"images/30anos_menor.png\"/></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><img src=\"images/new_design.png\"/></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("StackedWidget", u"NOVA APAR\u00caNCIA", None))
        self.label_42.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:8pt;\">Bem-vindos ao novo sistema de N\u00e3o Conformidades. Uma maneira mais \u00e1gil e r\u00e1pida de preenchimento da n\u00e3o conformidade.</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><img src=\"images/rapidez.png\"/></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("StackedWidget", u"MAIS RAPIDEZ", None))
        self.label_45.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:8pt;\">Agilidade e rapidez no processo de inser\u00e7\u00e3o, edi\u00e7\u00e3o e abertura de S.RO diretamente pelo sistema.</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><img src=\"images/duvidas.png\"/></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("StackedWidget", u"D\u00daVIDAS?", None))
        self.label_48.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p><span style=\" font-size:8pt;\">Caso possua alguma d\u00favida e/ou sugest\u00e3o de melhoria, em qualquer processo, favor contatar o seu L\u00edder direto ou o respons\u00e1vel pelo sistema.</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("StackedWidget", u"PESQUISAR", None))
        self.cmb_catgPergunta.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma categoria..", None))
        self.text_pergunta.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Digite sua busca..", None))
        self.btn_buscarGeral.setText(QCoreApplication.translate("StackedWidget", u"BUSCAR", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("StackedWidget", u"FILTROS DE DATAS", None))
        self.label_36.setText(QCoreApplication.translate("StackedWidget", u"Per\u00edodo Inicial:", None))
        self.label_37.setText(QCoreApplication.translate("StackedWidget", u"Per\u00edodo Final:", None))
        self.btn_buscarPeriodo.setText(QCoreApplication.translate("StackedWidget", u"BUSCAR", None))
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
        self.lbl_totalRegistros.setText(QCoreApplication.translate("StackedWidget", u"Total de registro(s): 0", None))
        self.btn_limparFiltros.setText(QCoreApplication.translate("StackedWidget", u"Limpar filtros", None))
        self.btnAlterarRegistro.setText(QCoreApplication.translate("StackedWidget", u"ALTERAR", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"right\"><img src=\"images/neo_Logo1.png\"/></p></body></html>", None))
        self.grpBusca_del.setTitle(QCoreApplication.translate("StackedWidget", u"PESQUISAR", None))
        self.txtBuscar_del.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Buscar", None))
        self.btnBuscar_del.setText(QCoreApplication.translate("StackedWidget", u"BUSCAR", None))
        ___qtablewidgetitem14 = self.tabDados_del.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem15 = self.tabDados_del.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("StackedWidget", u"ITEM", None));
        ___qtablewidgetitem16 = self.tabDados_del.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("StackedWidget", u"ORDEM", None));
        ___qtablewidgetitem17 = self.tabDados_del.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("StackedWidget", u"LOTE", None));
        ___qtablewidgetitem18 = self.tabDados_del.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("StackedWidget", u"\u00c1REA RESPONS\u00c1VEL", None));
        ___qtablewidgetitem19 = self.tabDados_del.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("StackedWidget", u"OPERA\u00c7\u00c3O", None));
        ___qtablewidgetitem20 = self.tabDados_del.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("StackedWidget", u"MOTIVO", None));
        ___qtablewidgetitem21 = self.tabDados_del.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("StackedWidget", u"QTDE.", None));
        ___qtablewidgetitem22 = self.tabDados_del.horizontalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("StackedWidget", u"QTDE. REPROVADA", None));
        ___qtablewidgetitem23 = self.tabDados_del.horizontalHeaderItem(9)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("StackedWidget", u"ACAO", None));
        ___qtablewidgetitem24 = self.tabDados_del.horizontalHeaderItem(10)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("StackedWidget", u"DATA", None));
        ___qtablewidgetitem25 = self.tabDados_del.horizontalHeaderItem(11)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("StackedWidget", u"RESPONS\u00c1VEL", None));
        ___qtablewidgetitem26 = self.tabDados_del.horizontalHeaderItem(12)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("StackedWidget", u"S.RO", None));
        ___qtablewidgetitem27 = self.tabDados_del.horizontalHeaderItem(13)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("StackedWidget", u"OBSERVA\u00c7\u00c3O", None));

        __sortingEnabled = self.tabDados_del.isSortingEnabled()
        self.tabDados_del.setSortingEnabled(False)
        self.tabDados_del.setSortingEnabled(__sortingEnabled)

        self.lblTotalRegistros_Del.setText(QCoreApplication.translate("StackedWidget", u"Total de registro(s): 0", None))
        self.btnDeleteRegister.setText(QCoreApplication.translate("StackedWidget", u"DELETAR", None))
        self.logoNeo_del.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"right\"><img src=\"images/neo_Logo1.png\"/></p></body></html>", None))
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
        self.text_data.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"01/01/2024", None))
        self.label_24.setText(QCoreApplication.translate("StackedWidget", u"Planta:*", None))
        self.text_planta.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"4400 / 4401", None))
        self.label_25.setText(QCoreApplication.translate("StackedWidget", u"Ordem:*", None))
        self.text_ordem.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"501020304", None))
        self.label_26.setText(QCoreApplication.translate("StackedWidget", u"Lote:*", None))
        self.text_lote.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"ABC12", None))
        self.label_27.setText(QCoreApplication.translate("StackedWidget", u"Item:*", None))
        self.text_item.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"109.XXX-X", None))
        self.label_28.setText(QCoreApplication.translate("StackedWidget", u"\u00c1rea Respons\u00e1vel pela identifica\u00e7\u00e3o:*", None))
        self.cmb_areaResp.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_29.setText(QCoreApplication.translate("StackedWidget", u"Respons\u00e1vel pela identifica\u00e7\u00e3o:*", None))
        self.text_respIden.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"u123XXX", None))
        self.btn_DadoGerais.setText(QCoreApplication.translate("StackedWidget", u"AVAN\u00c7AR", None))
        self.label_15.setText(QCoreApplication.translate("StackedWidget", u"Preencha os", None))
        self.label_16.setText(QCoreApplication.translate("StackedWidget", u"DADOS DA NCs", None))
        self.label_17.setText(QCoreApplication.translate("StackedWidget", u"da N\u00e3o Conformidade", None))
        self.label_18.setText(QCoreApplication.translate("StackedWidget", u"Informe corretamente todos os dados  da N\u00e3o Conformidade para evitar informa\u00e7\u00f5es divergentes nos indicadores, qualquer d\u00favida falar com seu L\u00edder direto.", None))
        self.label_30.setText(QCoreApplication.translate("StackedWidget", u"Qtde. Total:*", None))
        self.text_qtde.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"100", None))
        self.label_31.setText(QCoreApplication.translate("StackedWidget", u"Qtde. Reprovada:*", None))
        self.text_qtdeRep.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"50", None))
        self.label_32.setText(QCoreApplication.translate("StackedWidget", u"\u00c1res respons\u00e1vel da NC:*", None))
        self.cmb_areaNC.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_33.setText(QCoreApplication.translate("StackedWidget", u"Motivo da NC:*", None))
        self.cmb_Motivos.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_34.setText(QCoreApplication.translate("StackedWidget", u"A\u00e7\u00e3o a ser tomada:*", None))
        self.text_acao.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Retornou ao setor respons\u00e1vel", None))
        self.label_35.setText(QCoreApplication.translate("StackedWidget", u"Observa\u00e7\u00f5es:", None))
        self.text_Obs.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Escreva algo aqui..", None))
        self.btnVoltar1.setText(QCoreApplication.translate("StackedWidget", u"VOLTAR", None))
        self.btn_DadosNcs.setText(QCoreApplication.translate("StackedWidget", u"AVAN\u00c7AR", None))
        self.label_19.setText(QCoreApplication.translate("StackedWidget", u"Preencha a", None))
        self.label_20.setText(QCoreApplication.translate("StackedWidget", u"DISPOSI\u00c7\u00c3O", None))
        self.label_21.setText(QCoreApplication.translate("StackedWidget", u"da N\u00e3o Conformidade", None))
        self.label_22.setText(QCoreApplication.translate("StackedWidget", u"Informe corretamente a disposi\u00e7\u00e3o final da ordem para evitar processos faltantes durante a tratativa da n\u00e3o conformidade, qualquer d\u00favida falar com seu L\u00edder direto.", None))
        self.group_SRo.setTitle(QCoreApplication.translate("StackedWidget", u"Deseja abrir S.RO?*", None))
        self.btnSimRo.setText(QCoreApplication.translate("StackedWidget", u"SIM", None))
        self.btnNaoRo.setText(QCoreApplication.translate("StackedWidget", u"N\u00c3O", None))
        self.group_Email.setTitle(QCoreApplication.translate("StackedWidget", u"Deseja enviar por e-mail?*", None))
        self.btn_SimEmail.setText(QCoreApplication.translate("StackedWidget", u"SIM", None))
        self.btn_NaoEmail.setText(QCoreApplication.translate("StackedWidget", u"N\u00c3O", None))
        self.group_addressEmail.setTitle(QCoreApplication.translate("StackedWidget", u"Selecione os e-mails que deseja enviar:", None))
        self.check_acabamento.setText(QCoreApplication.translate("StackedWidget", u"Acabamento", None))
        self.check_tnc.setText(QCoreApplication.translate("StackedWidget", u"TNC", None))
        self.check_cnc.setText(QCoreApplication.translate("StackedWidget", u"CNC", None))
        self.check_higienizacao.setText(QCoreApplication.translate("StackedWidget", u"Higieniza\u00e7\u00e3o", None))
        self.check_recebimento.setText(QCoreApplication.translate("StackedWidget", u"Recebimento", None))
        self.check_usinagem.setText(QCoreApplication.translate("StackedWidget", u"Usinagem", None))
        self.check_trs.setText(QCoreApplication.translate("StackedWidget", u"TRS", None))
        self.check_usiAnaLid.setText(QCoreApplication.translate("StackedWidget", u"USI - Analista e L\u00edderes", None))
        self.check_pcp.setText(QCoreApplication.translate("StackedWidget", u"PCP", None))
        self.btnVoltar2.setText(QCoreApplication.translate("StackedWidget", u"VOLTAR", None))
        self.btn_Disposicao.setText(QCoreApplication.translate("StackedWidget", u"SALVAR", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p align=\"right\"><img src=\"images/neo_Logo1.png\"/></p></body></html>", None))
    # retranslateUi

