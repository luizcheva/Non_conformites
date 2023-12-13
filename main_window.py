from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
)
from widgets.pages.ui_main import (
    LeftMenu, ContentObject, StatusBar, ContentPage
)
from widgets.pages.ui_menu import LayoutMenu
from widgets.pages.ui_statusBar import LayoutTopBar, LayoutBottomBar
from widgets.tables import tableEdit
from widgets.combobox import UploadCB
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Slot
from PySide6.QtGui import QIntValidator
from datetime import datetime
from information import Message
from db.insertDB import insertNew


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
        self.table_edit = tableEdit(self.ui_pages)
        self.table_edit.carregaTable()

        # UPLOAD CB
        self.combo_box = UploadCB(self.ui_pages)
        self.combo_box.AreasIdentificacao()
        self.combo_box.AreaNC()
        self.combo_box.motivosNC()

        # VALIDATION
        self.ui_pages.text_qtde.setValidator(QIntValidator())
        self.ui_pages.text_qtdeRep.setValidator(QIntValidator())
        self.ui_pages.text_data.setInputMask('99/99/9999')
        self.ui_pages.text_data.editingFinished.connect(self.verificar_data)

        self.setCentralWidget(self.cf)

    def verificar_data(self):
        data_str = self.ui_pages.text_data.text()
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            msg = Message('Data Válida', f'A data {data} é válida.')
            msg.informationMsg()
        except ValueError:
            msg = Message('Data Errada', f'A data {data_str} é inválida.')
            msg.errorMsg()

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

    @Slot()
    def show_page_edit(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.ui_pages.page_edit)
        self.left_menu_layout.edit_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Editar Registro')

    @Slot()
    def show_page_del(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.ui_pages.page_del)
        self.left_menu_layout.del_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Deletar Registro')

    @Slot()
    def show_page_settings(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(
            self.ui_pages.page_settings
        )
        self.left_menu_layout.settings_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Configurações')

    @Slot()
    def show_dadosNC(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_NC)
        self.ui_pages.label_6.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_9.setStyleSheet('color: black;')

    @Slot()
    def show_dadosDisp(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_Disp)
        self.ui_pages.label_7.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_10.setStyleSheet('color: black;')

    @Slot()
    def btnVoltar1(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_geral)
        self.ui_pages.label_2.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_8.setStyleSheet('color: black;')

    @Slot()
    def btnVoltar2(self):
        self.reset_labels()
        self.pagesInsert.setCurrentWidget(self.ui_pages.page_NC)
        self.ui_pages.label_6.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_pages.label_9.setStyleSheet('color: black;')

    @Slot()
    def salvarInfo(self):
        msg = Message(
           'Salvar dados no Banco de dados',
           'Deseja realmente salvar os dados?'
        )
        result = msg.questionMsg()
        if result == msg.StandardButton.Yes:
            inserir = insertNew(self.ui_pages)
            inserir.salvarDados()
