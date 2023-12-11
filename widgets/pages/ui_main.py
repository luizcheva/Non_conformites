from PySide6.QtWidgets import QFrame, QStackedWidget
from widgets.pages.ui_pages import Ui_StackedWidget


class LeftMenu(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background-color: #853275')
        self.setMaximumWidth(50)
        self.setMinimumWidth(50)


class ContentObject(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('background-color: white')


class StatusBar(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background-color: #222425; color: #A7A8A9;')
        self.setMaximumHeight(30)
        self.setMinimumHeight(30)


class ContentPage(QStackedWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('font-size: 12pt; color: black')
        self.ui_page = Ui_StackedWidget()
        self.ui_page.setupUi(self)
        self.setCurrentWidget(self.ui_page.page_home)
