from widgets.pages.ui_pages import Ui_StackedWidget
from PySide6.QtCore import Slot, QDate
from PySide6.QtWidgets import QLabel
from information import Message
from widgets.requests import requestsBD
from widgets.tables import tableEdit
from widgets.combobox import UploadCB
from datetime import datetime


class EventsBtn():
    def __init__(self, ui_page: Ui_StackedWidget):
        self.ui_page = ui_page

    def reset_labels(self):
        for lbl in self.ui_page.frame_4.findChildren(QLabel):
            opts = (1, 2, 3)
            if not lbl.text() in str(opts):
                lbl.setStyleSheet(
                    'color: #e6e6e6;'
                )
            else:
                lbl.setStyleSheet(
                    'background-color: #A7A8A9;'
                    'color: #fff;'
                    'border-radius: 10%;'
                    'font: 10pt "KonsensLight" bold;'
                )

    def dataValida(self):
        data_str = self.ui_page.text_data.text()
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            return data
        except ValueError:
            msg = Message('Data Errada', f'A data {data_str} é inválida.')
            msg.errorMsg()
            self.ui_page.text_data.clear()
            self.ui_page.text_data.setFocus()

        return None

    @Slot()
    def show_dadosNC(self):
        self.reset_labels()
        self.ui_page.stackedWidget.setCurrentWidget(self.ui_page.page_NC)
        self.ui_page.label_6.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_page.label_9.setStyleSheet('color: black;')

    def show_dadosDisp(self):
        self.reset_labels()
        self.ui_page.stackedWidget.setCurrentWidget(self.ui_page.page_Disp)
        self.ui_page.label_7.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_page.label_10.setStyleSheet('color: black;')

    def btnVoltar1(self):
        self.reset_labels()
        self.ui_page.stackedWidget.setCurrentWidget(self.ui_page.page_geral)
        self.ui_page.label_2.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_page.label_8.setStyleSheet('color: black;')

    def btnVoltar2(self):
        self.reset_labels()
        self.ui_page.stackedWidget.setCurrentWidget(self.ui_page.page_NC)
        self.ui_page.label_6.setStyleSheet(
            'background-color: #853275; color: #fff;'
            'border-radius: 10%; font: 10pt "KonsensLight" bold;'
        )
        self.ui_page.label_9.setStyleSheet('color: black;')

    def requests(self):
        request = requestsBD()
        request.searchDB(
            self.ui_page.cmb_catgPergunta.currentText(),
            self.ui_page.text_pergunta.text(),
            self.ui_page
        )
        self.ui_page.btn_limparFiltros.setVisible(True)

    def clearFil(self):
        self.ui_page.cmb_catgPergunta.clear()
        cb = UploadCB()
        cb.fiedsBuscar(self.ui_page.cmb_catgPergunta)
        self.ui_page.text_pergunta.clear()
        self.ui_page.pesq_periodoInicial.setDate(QDate(2023, 1, 1))
        self.ui_page.pesq_periodoFinal.setDate(QDate(2023, 1, 1))
        tb = tableEdit(self.ui_page)
        tb.carregaTable()
        self.ui_page.btn_limparFiltros.setVisible(False)

    def requestTime(self):
        data_inicio = self.ui_page.pesq_periodoInicial.text()
        data_fim = self.ui_page.pesq_periodoFinal.text()

        request = requestsBD()
        request.searchPeriodo(self.ui_page, data_inicio, data_fim)
        self.ui_page.btn_limparFiltros.setVisible(True)
