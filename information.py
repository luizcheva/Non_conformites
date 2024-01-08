from PySide6.QtWidgets import QMessageBox, QApplication
import sys


class Message(QMessageBox):
    def __init__(self, title='Error', text='Error message'):
        super().__init__()
        self.title = title
        self.texto = text
        self.setMinimumWidth(400)

    def errorMsg(self):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle(self.title)
        self.setText(self.texto)
        self.exec()

    def informationMsg(self):
        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(self.title)
        self.setText(self.texto)
        self.exec()

    def noButtons(self):
        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(self.title)
        self.setText(self.texto)
        self.setStandardButtons(QMessageBox.StandardButton.NoButton)
        self.exec()

    def questionMsg(self):
        self.setIcon(QMessageBox.Icon.Question)
        self.setWindowTitle(self.title)
        self.setText(self.texto)
        self.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        result = self.exec()
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    message = Message()
    sys.exit(app.exec_())
