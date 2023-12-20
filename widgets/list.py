from widgets.pages.ui_pages import Ui_StackedWidget
from PySide6.QtWidgets import QTableWidget, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from information import Message
from db.conn import DataBase
from widgets.tables import tableEdit


class listView():
    def __init__(self, ui_page: Ui_StackedWidget):
        self.ui_page = ui_page
        self.initUI()

    def initUI(self):
        self.lista = self.ui_page.list_IDs
        self.unique_ids = set()
        self.addItems = []
        # self.lista.clear()

    def uploadList(self, tabela: QTableWidget):
        selected_index = tabela.selectedIndexes()
        for index in selected_index:
            row = index.row()
            col = index.column()

            if col == 0:
                _id = tabela.item(row, col)
                if _id.text() not in self.addItems:
                    self.addItems.append(_id.text())
                    item = QListWidgetItem(_id.text())
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.lista.addItem(item)
                else:
                    valor = _id.text()
                    msg = Message(
                        'Error ao adicionar o registro',
                        f'Desculpe, o registro "{valor}" já foi adicionado.'
                    )
                    msg.errorMsg()

    def deleteItems(self):
        msg = Message(
            'Atenção',
            'Deseja realmente excluir o(s) itens da lista?'
        )
        result = msg.questionMsg()

        if not result == QMessageBox.StandardButton.Yes:
            return

        if self.lista.count() == 0:
            msg = Message(
                'Lista Vazia',
                'Nenhum registro para excluir.'
            )
            msg.informationMsg()
            return

        for row in range(self.lista.count()):
            item = self.lista.item(row)
            db = DataBase()
            db.deleteRegister('nao_conformidade', item.text())
            self.lista.takeItem(row)

        table_edit = tableEdit(self.ui_page)
        table_edit.carregaTable(self.ui_page.tabDados_del)
        table_edit.carregaTable(self.ui_page.tab_dados)
        msg = Message('Sucesso', 'Registros deletados com sucesso!')
        msg.informationMsg()

    def removeItem(self):
        selected_item = self.lista.selectedIndexes()
        if self.lista.count() == 0 or not selected_item:
            msg = Message(
                'Error',
                'Nenhum registro selecionado.'
            )
            msg.errorMsg()
            return

        for index in selected_item:
            item = self.lista.item(index.row())
            self.lista.takeItem(index.row())
            if item.text() in self.addItems:
                self.addItems.remove(item.text())
