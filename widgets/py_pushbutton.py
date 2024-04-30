from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPixmap
from variables import FILES_DIR


class PyPushButton(QPushButton):
    def __init__(
            self,
            text='',
            height=50,
            minimum_width=50,
            text_padding=55,
            text_color='#ffffff',
            icon_path='',
            icon_color='#ffffff',
            btn_color='#853275',
            btn_hover='#A74D71',
            btn_pressed='#550044',
            is_active=False
    ):
        super().__init__()

        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=is_active_menu
        )

    def set_style(
            self,
            text_padding=55,
            text_color="#ffffff",
            btn_color="#853275",
            btn_hover="#A74D71",
            btn_pressed="#550044",
            is_active=False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {btn_pressed};
            border-right: 3px solid #ffffff;
        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.minimum_width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp, image, rect, color):
        # Path
        icon_path = FILES_DIR / image

        # Drawn Icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
