from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QDialog, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Nome', 'Idade', 'Profissão'])
        self.tableWidget.setRowCount(5)

        for row in range(5):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(f"Nome {row}"))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(20 + row)))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f"Profissão {row}"))

        self.editButton = QPushButton('Editar', self)
        self.editButton.clicked.connect(self.editSelectedRow)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.editButton)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def editSelectedRow(self):
        selected_items = self.tableWidget.selectedItems()

        if not selected_items:
            return

        row = selected_items[0].row()

        edit_dialog = EditDialog(self)
        edit_dialog.setFormData(
            self.tableWidget.item(row, 0).text(),
            self.tableWidget.item(row, 1).text(),
            self.tableWidget.item(row, 2).text()
        )

        if edit_dialog.exec_() == QDialog.Accepted:
            # Atualizar os dados na tabela
            self.tableWidget.item(row, 0).setText(edit_dialog.nameLineEdit.text())
            self.tableWidget.item(row, 1).setText(edit_dialog.ageLineEdit.text())
            self.tableWidget.item(row, 2).setText(edit_dialog.professionLineEdit.text())

class EditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Popup)
        self.initUI()


    def initUI(self):
        self.nameLabel = QLabel('Nome:', self)
        self.nameLineEdit = QLineEdit(self)

        self.ageLabel = QLabel('Idade:', self)
        self.ageLineEdit = QLineEdit(self)

        self.professionLabel = QLabel('Profissão:', self)
        self.professionLineEdit = QLineEdit(self)

        self.saveButton = QPushButton('Salvar', self)
        self.cancelButton = QPushButton('Cancelar', self)

        self.saveButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.nameLineEdit)
        layout.addWidget(self.ageLabel)
        layout.addWidget(self.ageLineEdit)
        layout.addWidget(self.professionLabel)
        layout.addWidget(self.professionLineEdit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.saveButton)
        button_layout.addWidget(self.cancelButton)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def setFormData(self, name, age, profession):
        self.nameLineEdit.setText(name)
        self.ageLineEdit.setText(age)
        self.professionLineEdit.setText(profession)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainForm()
    mainWindow.show()
    sys.exit(app.exec_())
