from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
)
from widgets.pages.ui_main import (
    LeftMenu, ContentObject, StatusBar, ContentPage
)
from widgets.pages.ui_menu import LayoutMenu
from PySide6.QtCore import QPropertyAnimation, QEasingCurve


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
