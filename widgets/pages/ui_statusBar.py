from PySide6.QtWidgets import QHBoxLayout, QLabel, QSpacerItem, QSizePolicy


class LayoutTopBar(QHBoxLayout):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setContentsMargins(10, 0, 10, 0)
        self.setSpacing(0)

        self.left_lbl = QLabel('Cadastros de Não Conformidades')
        self.top_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.right_lbl = QLabel('| Página Inicial')
        self.right_lbl.setStyleSheet('font: 700 9pt "Segoe UI"')

        self.addWidget(self.left_lbl)
        self.addItem(self.top_spacer)
        self.addWidget(self.right_lbl)


class LayoutBottomBar(QHBoxLayout):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setContentsMargins(10, 0, 10, 0)
        self.setSpacing(0)

        self.left_lbl = QLabel('Criado por: Luiz Cheva')
        self.top_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.right_lbl = QLabel('© 2024')

        self.addWidget(self.left_lbl)
        self.addItem(self.top_spacer)
        self.addWidget(self.right_lbl)
