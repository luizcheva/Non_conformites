from PySide6.QtWidgets import (
    QVBoxLayout, QFrame, QSpacerItem, QSizePolicy, QLabel,
    QPushButton
)
from PySide6.QtCore import Qt


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

        toggle_btn = QPushButton()
        toggle_btn.setText('Menu')
        toggle_btn.setStyleSheet('color: white')

        home_btn = QPushButton()
        home_btn.setText('HOME')
        home_btn.setStyleSheet('color: white')

        new_btn = QPushButton()
        new_btn.setText('NEW')
        new_btn.setStyleSheet('color: white')

        edit_btn = QPushButton()
        edit_btn.setText('EDIT')
        edit_btn.setStyleSheet('color: white')

        del_btn = QPushButton()
        del_btn.setText('DEL')
        del_btn.setStyleSheet('color: white')

        btn_layout.addWidget(toggle_btn)
        btn_layout.addWidget(home_btn)
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(del_btn)

    def SettingsBtn(self):
        settings_layout = QVBoxLayout(self.settings_frame)
        settings_layout.setContentsMargins(0, 0, 0, 0)
        settings_layout.setSpacing(0)

        settings_btn = QPushButton()
        settings_btn.setText('SETTINGS')
        settings_btn.setStyleSheet('color: white')

        settings_layout.addWidget(settings_btn)
