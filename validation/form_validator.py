from PySide6.QtWidgets import (
    QLineEdit, QMessageBox, QComboBox, QRadioButton, QGroupBox
)
from datetime import datetime


class FormValidator:
    def __init__(self):
        super().__init__()

    @staticmethod
    def is_valid_date(date_edit):
        date_text = date_edit.text()
        date_format = "%d/%m/%Y"

        try:
            datetime.strptime(date_text, date_format)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_number(line_edit):
        try:
            float(line_edit.text())
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_text(line_edit):
        valid_values = ('4400', '4401')
        planta = line_edit.text()
        if planta in valid_values:
            return True
        return False

    @staticmethod
    def is_required_field(line_edit):
        return len(line_edit.text().strip()) > 0

    @staticmethod
    def is_valid_combo_box(combo_box):
        return combo_box.currentIndex() != -1

    @staticmethod
    def is_valid_radio_button_in_group(group_box):
        for child in group_box.findChildren(QRadioButton):
            if child.isChecked():
                return True
        return False

    @staticmethod
    def validate_form(form):
        for child in form.findChildren(QLineEdit):
            if child.property("validator") == "date" and \
                    not FormValidator.is_valid_date(child):
                FormValidator.show_error_message(
                    "Erro de validação", "Campo de data inválido."
                )
                return False
            elif child.property("validator") == "number" and \
                    not FormValidator.is_valid_number(child):
                FormValidator.show_error_message(
                    "Erro de validação", f"Campo numérico inválido.\n "
                    f"O campo '{child.text()}' necessita de um número."
                )
                return False
            elif child.property("validator") == "text" and \
                    not FormValidator.is_valid_text(child):
                FormValidator.show_error_message(
                    "Erro de validação", "Campo de planta inválido."
                )
                return False
            elif child.property("validator") == "required" and \
                    not FormValidator.is_required_field(child):
                FormValidator.show_error_message(
                    "Erro de validação",
                    "Campos obrigatórios(*) não preenchido."
                )
                return False

        for child in form.findChildren(QComboBox):
            if child.property("validator") == "combo" and \
                    not FormValidator.is_valid_combo_box(child):
                FormValidator.show_error_message(
                    "Erro de validação",
                    "Você esqueceu de selecionar uma opção nos demais campos."
                    f"\n{child.objectName}"
                )
                return False

        for child in form.findChildren(QGroupBox):
            if child.property("validator") == "radio_group" and \
                    not FormValidator.is_valid_radio_button_in_group(child):
                FormValidator.show_error_message(
                    "Erro de validação",
                    f"Você deve marcar alguma opção do campo '{child.title()}'"
                )
                return False

        return True

    @staticmethod
    def show_error_message(title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
