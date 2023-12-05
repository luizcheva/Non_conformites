from PySide6.QtWidgets import (
    QVBoxLayout, QFrame, QSpacerItem, QSizePolicy, QLabel
)
from PySide6.QtCore import Qt
from widgets.py_pushbutton import PyPushButton


class LayoutMenu(QVBoxLayout):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        # FRAME BTNS
        self.top_frame = QFrame()
        self.top_frame.setMinimumHeight(40)

        # SPACER
        self.spacer_menu = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        # FRAME SETTINGS
        self.settings_frame = QFrame()
        self.settings_frame.setMinimumHeight(40)

        # VERSION
        versao = 'v1.0.0'
        self.version_label = QLabel(versao)
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.version_label.setMinimumHeight(30)
        self.version_label.setMaximumHeight(30)
        self.version_label.setStyleSheet(
            'color: white; background-color: #550044;'
        )

        self.addWidget(self.top_frame)
        self.addItem(self.spacer_menu)
        self.addWidget(self.settings_frame)
        self.addWidget(self.version_label)

        # ADD BTNS
        self.BtnsTop()
        self.SettingsBtn()

    def BtnsTop(self):
        btn_layout = QVBoxLayout(self.top_frame)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(0)

        self.toggle_btn = PyPushButton(
            text='Ocultar Menu', icon_path='btn_toggle.svg'
        )

        self.home_btn = PyPushButton(
            text='Página Inicial', icon_path='btn_home.svg',
            is_active=True
        )

        self.new_btn = PyPushButton(
            text='Novo registro', icon_path='btn_add.svg'
        )

        self.edit_btn = PyPushButton(
            text='Editar registro', icon_path='btn_edit.svg'
        )

        self.del_btn = PyPushButton(
            text='Excluir registro', icon_path='btn_del.svg'
        )

        btn_layout.addWidget(self.toggle_btn)
        btn_layout.addWidget(self.home_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.del_btn)

    def SettingsBtn(self):
        settings_layout = QVBoxLayout(self.settings_frame)
        settings_layout.setContentsMargins(0, 0, 0, 0)
        settings_layout.setSpacing(0)

        self.settings_btn = PyPushButton(
            text='Configurações', icon_path='btn_settings.svg',
        )

        settings_layout.addWidget(self.settings_btn)
