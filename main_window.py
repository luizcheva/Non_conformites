from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Registros de Não Conformidades - NEODENT')
        self.resize(1200, 720)
        self.setMinimumSize(960, 540)

        self.cw = QWidget()
        self.main_window = QHBoxLayout(self.cw)
        self.main_window.setContentsMargins(0, 0, 0, 0)
        self.main_window.setSpacing(0)
        self.setCentralWidget(self.cw)
