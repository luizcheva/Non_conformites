# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogFYBmgR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QToolBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(776, 569)
        Dialog.setStyleSheet(u"background-color: #F9F8F9;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(Dialog)
        self.toolBox.setObjectName(u"toolBox")
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(u"QToolBox {\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	background-color: #A7A8A9;\n"
"	color: #e6e6e6;;\n"
"	border: 1px solid transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"	border: 1px solid #636569;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"	background-color: #853275;\n"
"	color: white;\n"
"}")
        self.group_geral = QWidget()
        self.group_geral.setObjectName(u"group_geral")
        self.group_geral.setGeometry(QRect(0, 0, 766, 422))
        self.horizontalLayout_3 = QHBoxLayout(self.group_geral)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.group_geral)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(700, 400))
        self.frame_2.setMaximumSize(QSize(700, 400))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 15))
        self.label_23.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setFamilies([u"KonsensRegular"])
        font1.setPointSize(12)
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_2.addWidget(self.label_23)

        self.text_data = QLineEdit(self.frame_2)
        self.text_data.setObjectName(u"text_data")
        self.text_data.setMinimumSize(QSize(200, 35))
        self.text_data.setMaximumSize(QSize(200, 35))
        self.text_data.setFont(font1)
        self.text_data.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_2.addWidget(self.text_data)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 15))
        self.label_24.setMaximumSize(QSize(16777215, 15))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_3.addWidget(self.label_24)

        self.text_planta = QLineEdit(self.frame_2)
        self.text_planta.setObjectName(u"text_planta")
        self.text_planta.setMinimumSize(QSize(200, 0))
        self.text_planta.setMaximumSize(QSize(200, 35))
        self.text_planta.setFont(font1)
        self.text_planta.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_3.addWidget(self.text_planta)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 15))
        self.label_25.setMaximumSize(QSize(16777215, 15))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_4.addWidget(self.label_25)

        self.text_ordem = QLineEdit(self.frame_2)
        self.text_ordem.setObjectName(u"text_ordem")
        self.text_ordem.setMinimumSize(QSize(368, 0))
        self.text_ordem.setMaximumSize(QSize(16777215, 35))
        self.text_ordem.setFont(font1)
        self.text_ordem.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_4.addWidget(self.text_ordem)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 15))
        self.label_26.setMaximumSize(QSize(16777215, 15))
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_5.addWidget(self.label_26)

        self.text_lote = QLineEdit(self.frame_2)
        self.text_lote.setObjectName(u"text_lote")
        self.text_lote.setMinimumSize(QSize(200, 0))
        self.text_lote.setMaximumSize(QSize(200, 35))
        self.text_lote.setFont(font1)
        self.text_lote.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_5.addWidget(self.text_lote)


        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 15))
        self.label_27.setMaximumSize(QSize(16777215, 15))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_6.addWidget(self.label_27)

        self.text_item = QLineEdit(self.frame_2)
        self.text_item.setObjectName(u"text_item")
        self.text_item.setMinimumSize(QSize(200, 0))
        self.text_item.setMaximumSize(QSize(200, 35))
        self.text_item.setFont(font1)
        self.text_item.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_6.addWidget(self.text_item)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 15))
        self.label_28.setMaximumSize(QSize(16777215, 15))
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_8.addWidget(self.label_28)

        self.cmb_areaResp = QComboBox(self.frame_2)
        self.cmb_areaResp.setObjectName(u"cmb_areaResp")
        self.cmb_areaResp.setMinimumSize(QSize(368, 0))
        self.cmb_areaResp.setMaximumSize(QSize(16777215, 35))
        self.cmb_areaResp.setFont(font1)
        self.cmb_areaResp.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_8.addWidget(self.cmb_areaResp)


        self.gridLayout.addLayout(self.verticalLayout_8, 3, 0, 1, 2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 15))
        self.label_29.setMaximumSize(QSize(16777215, 15))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_7.addWidget(self.label_29)

        self.text_respIden = QLineEdit(self.frame_2)
        self.text_respIden.setObjectName(u"text_respIden")
        self.text_respIden.setMinimumSize(QSize(368, 0))
        self.text_respIden.setMaximumSize(QSize(16777215, 35))
        self.text_respIden.setFont(font1)
        self.text_respIden.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_7.addWidget(self.text_respIden)


        self.gridLayout.addLayout(self.verticalLayout_7, 4, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.toolBox.addItem(self.group_geral, u"Dados Gerais")
        self.group_Nc = QWidget()
        self.group_Nc.setObjectName(u"group_Nc")
        self.horizontalLayout_4 = QHBoxLayout(self.group_Nc)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.group_Nc)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(700, 400))
        self.frame_3.setMaximumSize(QSize(700, 400))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(5)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 15))
        self.label_30.setMaximumSize(QSize(16777215, 15))
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_9.addWidget(self.label_30)

        self.text_qtde = QLineEdit(self.frame_3)
        self.text_qtde.setObjectName(u"text_qtde")
        self.text_qtde.setMinimumSize(QSize(200, 35))
        self.text_qtde.setMaximumSize(QSize(200, 35))
        self.text_qtde.setFont(font1)
        self.text_qtde.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_9.addWidget(self.text_qtde)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 15))
        self.label_31.setMaximumSize(QSize(16777215, 15))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_10.addWidget(self.label_31)

        self.text_qtdeRep = QLineEdit(self.frame_3)
        self.text_qtdeRep.setObjectName(u"text_qtdeRep")
        self.text_qtdeRep.setMinimumSize(QSize(200, 35))
        self.text_qtdeRep.setMaximumSize(QSize(200, 35))
        self.text_qtdeRep.setFont(font1)
        self.text_qtdeRep.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_10.addWidget(self.text_qtdeRep)


        self.gridLayout_2.addLayout(self.verticalLayout_10, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 15))
        self.label_32.setMaximumSize(QSize(16777215, 15))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_11.addWidget(self.label_32)

        self.cmb_areaNC = QComboBox(self.frame_3)
        self.cmb_areaNC.setObjectName(u"cmb_areaNC")
        self.cmb_areaNC.setMinimumSize(QSize(368, 35))
        self.cmb_areaNC.setMaximumSize(QSize(16777215, 35))
        self.cmb_areaNC.setFont(font1)
        self.cmb_areaNC.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_11.addWidget(self.cmb_areaNC)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 1, 0, 1, 2)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 15))
        self.label_33.setMaximumSize(QSize(16777215, 15))
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_12.addWidget(self.label_33)

        self.cmb_Motivos = QComboBox(self.frame_3)
        self.cmb_Motivos.setObjectName(u"cmb_Motivos")
        self.cmb_Motivos.setMinimumSize(QSize(368, 35))
        self.cmb_Motivos.setMaximumSize(QSize(16777215, 35))
        self.cmb_Motivos.setFont(font1)
        self.cmb_Motivos.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_12.addWidget(self.cmb_Motivos)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 0, 1, 2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 15))
        self.label_34.setMaximumSize(QSize(16777215, 15))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_13.addWidget(self.label_34)

        self.text_acao = QLineEdit(self.frame_3)
        self.text_acao.setObjectName(u"text_acao")
        self.text_acao.setMinimumSize(QSize(368, 35))
        self.text_acao.setMaximumSize(QSize(16777215, 35))
        self.text_acao.setFont(font1)
        self.text_acao.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
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

        self.verticalLayout_13.addWidget(self.text_acao)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 3, 0, 1, 2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 15))
        self.label_35.setMaximumSize(QSize(16777215, 15))
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_14.addWidget(self.label_35)

        self.text_Obs = QTextEdit(self.frame_3)
        self.text_Obs.setObjectName(u"text_Obs")
        self.text_Obs.setMinimumSize(QSize(368, 35))
        self.text_Obs.setMaximumSize(QSize(16777215, 90))
        self.text_Obs.setFont(font1)
        self.text_Obs.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(255,255,255);\n"
"	padding-left: 15px;\n"
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

        self.verticalLayout_14.addWidget(self.text_Obs)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 4, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.toolBox.addItem(self.group_Nc, u"Dados da NCs")
        self.group_disp = QWidget()
        self.group_disp.setObjectName(u"group_disp")
        self.group_disp.setGeometry(QRect(0, 0, 766, 422))
        self.horizontalLayout_5 = QHBoxLayout(self.group_disp)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.group_disp)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(700, 400))
        self.frame_4.setMaximumSize(QSize(700, 400))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.group_SRo = QGroupBox(self.frame_4)
        self.group_SRo.setObjectName(u"group_SRo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_SRo.sizePolicy().hasHeightForWidth())
        self.group_SRo.setSizePolicy(sizePolicy)
        self.group_SRo.setMinimumSize(QSize(0, 60))
        self.group_SRo.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setFamilies([u"KonsensBook"])
        font2.setPointSize(10)
        font2.setItalic(False)
        self.group_SRo.setFont(font2)
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
        self.btnSimRo.setFont(font1)
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
        self.btnNaoRo.setFont(font1)
        self.btnNaoRo.setStyleSheet(u"QRadioButton {\n"
"	padding-left: 15%;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btnNaoRo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addWidget(self.group_SRo)

        self.group_Email = QGroupBox(self.frame_4)
        self.group_Email.setObjectName(u"group_Email")
        self.group_Email.setMinimumSize(QSize(0, 60))
        self.group_Email.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setFamilies([u"KonsensBook"])
        font3.setPointSize(10)
        self.group_Email.setFont(font3)
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
        self.btn_SimEmail.setFont(font1)
        self.btn_SimEmail.setStyleSheet(u"padding-left: 15%;")

        self.horizontalLayout_16.addWidget(self.btn_SimEmail)

        self.btn_NaoEmail = QRadioButton(self.group_Email)
        self.btn_NaoEmail.setObjectName(u"btn_NaoEmail")
        self.btn_NaoEmail.setMinimumSize(QSize(85, 0))
        self.btn_NaoEmail.setMaximumSize(QSize(85, 16777215))
        self.btn_NaoEmail.setFont(font1)
        self.btn_NaoEmail.setStyleSheet(u"padding-left: 15%;")

        self.horizontalLayout_16.addWidget(self.btn_NaoEmail)

        self.horizontalSpacer_5 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)


        self.verticalLayout_15.addWidget(self.group_Email)

        self.group_addressEmail = QGroupBox(self.frame_4)
        self.group_addressEmail.setObjectName(u"group_addressEmail")
        self.group_addressEmail.setEnabled(True)
        self.group_addressEmail.setMinimumSize(QSize(0, 200))
        self.group_addressEmail.setMaximumSize(QSize(16777215, 200))
        self.group_addressEmail.setFont(font3)
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
        font4 = QFont()
        font4.setFamilies([u"KonsensBook"])
        font4.setPointSize(12)
        font4.setUnderline(False)
        self.check_acabamento.setFont(font4)
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
        self.check_tnc.setFont(font4)
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
        self.check_cnc.setFont(font4)
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
        self.check_higienizacao.setFont(font4)
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
        self.check_recebimento.setFont(font4)
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
        self.check_usinagem.setFont(font4)
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
        self.check_trs.setFont(font4)
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
        self.check_usiAnaLid.setFont(font4)
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
        self.check_pcp.setFont(font4)
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


        self.verticalLayout_15.addWidget(self.group_addressEmail)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.toolBox.addItem(self.group_disp, u"Disposi\u00e7\u00e3o")

        self.verticalLayout.addWidget(self.toolBox)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(490, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 10, -1)
        self.btnVoltar1 = QPushButton(self.frame)
        self.btnVoltar1.setObjectName(u"btnVoltar1")
        self.btnVoltar1.setMinimumSize(QSize(130, 35))
        self.btnVoltar1.setMaximumSize(QSize(130, 35))
        font5 = QFont()
        font5.setFamilies([u"KonsensLight"])
        self.btnVoltar1.setFont(font5)
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

        self.horizontalLayout.addWidget(self.btnVoltar1)

        self.btn_DadosNcs = QPushButton(self.frame)
        self.btn_DadosNcs.setObjectName(u"btn_DadosNcs")
        self.btn_DadosNcs.setMinimumSize(QSize(130, 35))
        self.btn_DadosNcs.setMaximumSize(QSize(130, 35))
        font6 = QFont()
        font6.setFamilies([u"KonsensBold"])
        font6.setPointSize(12)
        self.btn_DadosNcs.setFont(font6)
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

        self.horizontalLayout.addWidget(self.btn_DadosNcs)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Data:*", None))
        self.text_data.setPlaceholderText(QCoreApplication.translate("Dialog", u"01/01/2024", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Planta:*", None))
        self.text_planta.setPlaceholderText(QCoreApplication.translate("Dialog", u"4400 / 4401", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Ordem:*", None))
        self.text_ordem.setPlaceholderText(QCoreApplication.translate("Dialog", u"501020304", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Lote:*", None))
        self.text_lote.setPlaceholderText(QCoreApplication.translate("Dialog", u"ABC12", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Item:*", None))
        self.text_item.setPlaceholderText(QCoreApplication.translate("Dialog", u"109.XXX-X", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"\u00c1rea Respons\u00e1vel pela identifica\u00e7\u00e3o:*", None))
        self.cmb_areaResp.setPlaceholderText(QCoreApplication.translate("Dialog", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Respons\u00e1vel pela identifica\u00e7\u00e3o:*", None))
        self.text_respIden.setPlaceholderText(QCoreApplication.translate("Dialog", u"u123XXX", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.group_geral), QCoreApplication.translate("Dialog", u"Dados Gerais", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Qtde. Total:*", None))
        self.text_qtde.setPlaceholderText(QCoreApplication.translate("Dialog", u"100", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Qtde. Reprovada:*", None))
        self.text_qtdeRep.setPlaceholderText(QCoreApplication.translate("Dialog", u"50", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"\u00c1res respons\u00e1vel da NC:*", None))
        self.cmb_areaNC.setPlaceholderText(QCoreApplication.translate("Dialog", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"Motivo da NC:*", None))
        self.cmb_Motivos.setPlaceholderText(QCoreApplication.translate("Dialog", u"Selecione uma op\u00e7\u00e3o..", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"A\u00e7\u00e3o a ser tomada:*", None))
        self.text_acao.setPlaceholderText(QCoreApplication.translate("Dialog", u"Retornou ao setor respons\u00e1vel", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"Observa\u00e7\u00f5es:", None))
        self.text_Obs.setPlaceholderText(QCoreApplication.translate("Dialog", u"Escreva algo aqui..", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.group_Nc), QCoreApplication.translate("Dialog", u"Dados da NCs", None))
        self.group_SRo.setTitle(QCoreApplication.translate("Dialog", u"Deseja abrir S.RO?*", None))
        self.btnSimRo.setText(QCoreApplication.translate("Dialog", u"SIM", None))
        self.btnNaoRo.setText(QCoreApplication.translate("Dialog", u"N\u00c3O", None))
        self.group_Email.setTitle(QCoreApplication.translate("Dialog", u"Deseja enviar por e-mail?*", None))
        self.btn_SimEmail.setText(QCoreApplication.translate("Dialog", u"SIM", None))
        self.btn_NaoEmail.setText(QCoreApplication.translate("Dialog", u"N\u00c3O", None))
        self.group_addressEmail.setTitle(QCoreApplication.translate("Dialog", u"Selecione os e-mails que deseja enviar:", None))
        self.check_acabamento.setText(QCoreApplication.translate("Dialog", u"Acabamento", None))
        self.check_tnc.setText(QCoreApplication.translate("Dialog", u"TNC", None))
        self.check_cnc.setText(QCoreApplication.translate("Dialog", u"CNC", None))
        self.check_higienizacao.setText(QCoreApplication.translate("Dialog", u"Higieniza\u00e7\u00e3o", None))
        self.check_recebimento.setText(QCoreApplication.translate("Dialog", u"Recebimento", None))
        self.check_usinagem.setText(QCoreApplication.translate("Dialog", u"Usinagem", None))
        self.check_trs.setText(QCoreApplication.translate("Dialog", u"TRS", None))
        self.check_usiAnaLid.setText(QCoreApplication.translate("Dialog", u"USI - Analista e L\u00edderes", None))
        self.check_pcp.setText(QCoreApplication.translate("Dialog", u"PCP", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.group_disp), QCoreApplication.translate("Dialog", u"Disposi\u00e7\u00e3o", None))
        self.btnVoltar1.setText(QCoreApplication.translate("Dialog", u"CANCELAR", None))
        self.btn_DadosNcs.setText(QCoreApplication.translate("Dialog", u"SALVAR", None))
    # retranslateUi

