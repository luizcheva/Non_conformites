from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QPushButton, QWidget
)
from widgets.pages.ui_main import (
    LeftMenu, ContentObject, StatusBar, ContentPage
)
from widgets.pages.ui_menu import LayoutMenu
from widgets.pages.settings import Settings_
from widgets.pages.ui_statusBar import LayoutTopBar, LayoutBottomBar
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Slot
from db.conn import DataBase
import os
from information import Message


class MainWindows(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

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
        self.content_page = ContentPage(self)

        # ADD TO LAYOUT CONTENT
        self.content_layout.addWidget(self.top_stuatus_bar)
        self.content_layout.addWidget(self.content_page)
        self.content_layout.addWidget(self.bottom_status_bar)

        # LAYOUT LEFT MENU
        self.lMenuLyt = LayoutMenu(self.left_menu)

        # EVENT TOGGLE
        self.lMenuLyt.toggle_btn.clicked.connect(self.toggle_button)

        # LAYOUT TOP BAR
        self.top_bar_layout = LayoutTopBar(self.top_stuatus_bar)

        # LAYOUT BOTTOM BAR
        self.bottom_bar_layout = LayoutBottomBar(self.bottom_status_bar)

        # UPLOADING PAGE SETTINGS DATA
        self.page_settings = Settings_(self)

        # EVENTS BTNS
        self.lMenuLyt.home_btn.clicked.connect(self.show_page_home)
        self.lMenuLyt.new_btn.clicked.connect(self.show_page_add)
        self.lMenuLyt.edit_btn.clicked.connect(self.show_page_edit)
        self.lMenuLyt.del_btn.clicked.connect(self.show_page_del)
        self.lMenuLyt.settings_btn.clicked.connect(
            self.show_page_settings
        )

        # HIDE CLEAR FILTER BTN
        self.content_page.ui_page.btn_limparFiltros.setVisible(False)

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

    @Slot()
    def show_page_home(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.content_page.ui_page.page_home)
        self.lMenuLyt.home_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Página Inicial')

    def show_page_add(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.content_page.ui_page.page_add)
        self.lMenuLyt.new_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Novo Registro')

    def show_page_edit(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(self.content_page.ui_page.page_edit)
        self.lMenuLyt.edit_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Editar Registro')

    def show_page_del(self):
        db = DataBase()
        user_access = db.users()
        usuario_atual = os.environ.get('USERNAME')

        if usuario_atual not in user_access:
            msg = Message(
                'Usuário não permitido',
                'Desculpe, você não possui acesso a essa seção!'
                '\n Caso deseja excluir algum registro falar com seu líder '
                'direto ou o responsável do sistema.'
            )
            msg.errorMsg()
            return

        self.reset_selection()
        self.content_page.setCurrentWidget(self.content_page.ui_page.page_del)
        self.lMenuLyt.del_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Deletar Registro')

    def show_page_settings(self):
        self.reset_selection()
        self.content_page.setCurrentWidget(
            self.content_page.ui_page.page_settings
        )
        self.lMenuLyt.settings_btn.set_active(True)
        self.top_bar_layout.right_lbl.setText('| Configurações')
