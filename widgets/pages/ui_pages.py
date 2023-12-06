# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageskDdXYK.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(989, 671)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout = QVBoxLayout(self.page_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        StackedWidget.addWidget(self.page_home)
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.verticalLayout_4 = QVBoxLayout(self.page_edit)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.page_edit)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        StackedWidget.addWidget(self.page_edit)
        self.page_del = QWidget()
        self.page_del.setObjectName(u"page_del")
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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_add)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        StackedWidget.addWidget(self.page_add)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"P\u00e1gina Inicial", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Editar um registro", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Deletar um registro", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Configura\u00e7\u00f5es", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Adicionar um novo registro", None))
    # retranslateUi

