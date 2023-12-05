from PySide6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
)
from widgets.pages.ui_main import (
    LeftMenu, ContentObject, StatusBar, ContentPage
)


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

        self.setCentralWidget(self.cf)
