from PySide6.QtWidgets import QFrame


class LeftMenu(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background-color: #853276')
        self.setMaximumWidth(50)
        self.setMinimumWidth(50)


class ContentObject(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('background-color: white')


class StatusBar(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background-color: #f2d0d9; color: #853276;')
        self.setMaximumHeight(30)
        self.setMinimumHeight(30)


class ContentPage(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
