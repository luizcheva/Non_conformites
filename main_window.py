from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QLabel,
    QTableWidgetItem
)
from widgets.pages.ui_main import (
    LeftMenu, ContentObject, StatusBar, ContentPage
)
from widgets.pages.ui_menu import LayoutMenu
from widgets.pages.ui_statusBar import LayoutTopBar, LayoutBottomBar
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from db.conn import DataBase


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Registros de Não Conformidades - NEODENT')
        self.resize(1200, 720)
        self.setMinimumSize(960, 540)

        self.cf = QFrame()
        self.main_window = QHBoxLayout(self.cf)
        self.main_window.setContentsMargins(0, 0, 0, 0)
        self.main_window.setSpacing(0)

        # LEFT MENU
        self.left_menu = LeftMenu()

        # CONTENT
        self.content = ContentObject()

        # ADD TO LAYOUT
        self.main_window.addWidget(self.left_menu)
        self.main_window.addWidget(self.content)

        # LAYOUT FOR CONTENT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # STATUS BAR
        self.top_stuatus_bar = StatusBar()
        self.bottom_status_bar = StatusBar()

        # CONTENT PAGE
        self.content_page = ContentPage()

        # ADD TO LAYOUT CONTENT
        self.content_layout.addWidget(self.top_stuatus_bar)
        self.content_layout.addWidget(self.content_page)
        self.content_layout.addWidget(self.bottom_status_bar)

        # LAYOUT LEFT MENU
        self.left_menu_layout = LayoutMenu(self.left_menu)

        # EVENT TOGGLE
        self.left_menu_layout.toggle_btn.clicked.connect(self.toggle_button)

        # LAYOUT TOP BAR
        self.top_bar_layout = LayoutTopBar(self.top_stuatus_bar)

        # LAYOUT BOTTOM BAR
        self.bottom_bar_layout = LayoutBottomBar(self.bottom_status_bar)

        # WORK WITH PAGES ON STACKEDWIDGET
        self.ui_pages = self.content_page.ui_page

        # EVENTS BTNS
        self.left_menu_layout.home_btn.clicked.connect(self.show_page_home)
        self.left_menu_layout.new_btn.clicked.connect(self.show_page_add)
        self.left_menu_layout.edit_btn.clicked.connect(self.show_page_edit)
        self.left_menu_layout.del_btn.clicked.connect(self.show_page_del)
        self.left_menu_layout.settings_btn.clicked.connect(
            self.show_page_settings
        )
        self.ui_pages.btn_DadoGerais.clicked.connect(self.show_dadosNC)
        self.ui_pages.btn_DadosNcs.clicked.connect(self.show_dadosDisp)
        self.ui_pages.btn_Disposicao.clicked.connect(self.salvarInfo)
        self.ui_pages.btnVoltar1.clicked.connect(self.btnVoltar1)
        self.ui_pages.btnVoltar2.clicked.connect(self.btnVoltar2)

        # CURRENT PAGE FROM INSERT
        self.pagesInsert = self.ui_pages.stackedWidget
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_geral)

        # UPLOAD TABLE
        self.carregaTable()

        self.setCentralWidget(self.cf)

    def toggle_button(self):
        menu_width = self.left_menu.width()

        width = 50
        if menu_width == 50:
            width = 200

        self.animation = QPropertyAnimation(self.left_menu, b'minimumWidth')
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()

    def reset_selection(self):
        for btn in self.left_menu.findChildren(QPushButton):
            if btn.set_active:
                btn.set_active(False)

    def reset_labels(self):
        for lbl in self.ui_pages.frame_4.findChildren(QLabel):
            opts = (1, 2, 3)
            if not lbl.text() in str(opts):
                lbl.setStyleSheet(
                    'color: #e6e6e6;'
                )
            else:
                lbl.setStyleSheet(
                    'background-color: #A7A8A9;'
                    'color: #fff;'
                    'border-radius: 10%;'
                    'font: 10pt "KonsensLight" bold;'
                )

    def show_page_home(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.ui_pages.page_home)
        self.left_menu_layout.home_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Página Inicial')

    def show_page_add(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.ui_pages.page_add)
        self.left_menu_layout.new_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Novo Registro')

    def show_page_edit(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.ui_pages.page_edit)
        self.left_menu_layout.edit_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Editar Registro')

    def show_page_del(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.ui_pages.page_del)
        self.left_menu_layout.del_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Deletar Registro')

    def show_page_settings(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(
            self.ui_pages.page_settings
        )
        self.left_menu_layout.settings_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Configurações')

    def show_dadosNC(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_NC)
        self.ui_pages.label_6.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_9.setStyleSheet('color: black;')

    def show_dadosDisp(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_Disp)
        self.ui_pages.label_7.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_10.setStyleSheet('color: black;')

    def btnVoltar1(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_geral)
        self.ui_pages.label_2.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_8.setStyleSheet('color: black;')

    def btnVoltar2(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_NC)
        self.ui_pages.label_6.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_9.setStyleSheet('color: black;')

    def salvarInfo(self):
        print('Adicionando os dados....')

    def carregaTable(self):
        db = DataBase()
        table = self.ui_pages.tab_dados
        results = db.selectTable()

        table.clearContents()
        table.setRowCount(len(results))

        for row, text in enumerate(results):
            table.setItem(row, 0, QTableWidgetItem(str(text["ID"])))
            try:
                item = int(text["ITEM"])
            except ValueError:
                item = text["ITEM"]

            table.setItem(row, 1, QTableWidgetItem(str(item)))
            table.setItem(row, 2, QTableWidgetItem(str(text["ORDEM"])))
            table.setItem(row, 3, QTableWidgetItem(str(text["LOTE"])))
            table.setItem(
                row, 4, QTableWidgetItem(str(text["AREA_RESPONSAVEL"]))
            )
            table.setItem(row, 5, QTableWidgetItem(str(text["OPERACAO"])))
            table.setItem(
                row, 6, QTableWidgetItem(str(text["NAO_CONFORMIDADE"]))
            )
            table.setItem(row, 7, QTableWidgetItem(str(text["QUANTIDADE"])))
            table.setItem(
                row, 8, QTableWidgetItem(str(text["QUANTIDADE_REPROVADA"]))
            )
            table.setItem(row, 9, QTableWidgetItem(str(text["ACAO"])))

            data_format = db.convertDate(text["DATA"])
            table.setItem(row, 10, QTableWidgetItem(str(data_format)))
            table.setItem(row, 11, QTableWidgetItem(str(text["RESPONSAVEL"])))
            table.setItem(row, 12, QTableWidgetItem(str(text["S_RO"])))
            table.setItem(row, 13, QTableWidgetItem(str(text["OBS"])))

        db.closeDB()
