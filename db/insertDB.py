from datetime import datetime
from PySide6.QtWidgets import (
    QRadioButton, QLineEdit, QTextEdit,
    QGroupBox, QComboBox
)
from db.conn import DataBase
from information import Message
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main_window import MainWindows


class insertNew():
    def __init__(self, windows: 'MainWindows') -> None:
        self.windows = windows
        self.ui_page = self.windows.content_page.ui_page

    def salvarDados(self):
        item = self.ui_page.text_item.text()
        ordem = self.ui_page.text_ordem.text()
        lote = self.ui_page.text_lote.text()
        area = self.ui_page.cmb_areaNC.currentText()
        operacao = self.ui_page.cmb_areaResp.currentText()
        nc = self.ui_page.cmb_Motivos.currentText()
        qtde = self.ui_page.text_qtde.text()
        qtde_rep = self.ui_page.text_qtdeRep.text()
        acao = self.ui_page.text_acao.text()
        data = self.ui_page.text_data.text()
        resp = self.ui_page.text_respIden.text()
        obs = self.ui_page.text_Obs.toPlainText()

        data_format = datetime.strptime(data, "%d/%m/%Y")

        sro = ''
        for control in self.ui_page.group_SRo.findChildren(QRadioButton):
            if control.isChecked():
                sro = control.text()

        if sro == 'NÃO':
            sro = 'false'
        else:
            sro = 'true'

        values = {
            'item': f'{item}',
            'ordem': int(ordem),
            'lote': f'{lote}',
            'area': f'{area}',
            'operacao': f'{operacao}',
            'nc': f'{nc}',
            'qtde': int(qtde),
            'qtde_rep': int(qtde_rep),
            'acao': f'{acao}',
            'data': f'{str(data_format)}',
            'responsavel': f'{resp}',
            's_ro': f'{sro}',
            'obs': f'{obs}'
        }
        db = DataBase()
        inserir = db.insertData('nao_conformidade', values)

        if inserir == "OK":
            msg = Message('Parabens', 'Registro adicionado com sucesso')
            msg.informationMsg()
            self.clearData()

    def clearData(self):
        for child in self.ui_page.stackedWidget.findChildren(QLineEdit):
            child.clear()

        for child in self.ui_page.stackedWidget.findChildren(QGroupBox):
            for child1 in child.findChildren(QRadioButton):
                if isinstance(child1, QRadioButton):
                    child1.setChecked(False)

        for child in self.ui_page.stackedWidget.findChildren(QComboBox):
            child.setCurrentIndex(-1)

        for child in self.ui_page.stackedWidget.findChildren(QTextEdit):
            child.clear()
