from db.conn import DataBase
from PySide6.QtWidgets import QTableWidgetItem
from widgets.pages.ui_pages import Ui_StackedWidget


class tableEdit():
    def __init__(self, ui_pages: Ui_StackedWidget = '') -> None:
        self.db_instance = DataBase()
        self.ui_page = ui_pages
        self.table = self.ui_page.tab_dados

    def carregaTable(self):
        results = self.db_instance.selectTable()

        self.table.clearContents()
        self.table.setRowCount(0)

        for row, text in enumerate(results):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(text["ID"])))
            try:
                item = int(text["ITEM"])
            except ValueError:
                item = text["ITEM"]

            self.table.setItem(row, 1, QTableWidgetItem(str(item)))
            self.table.setItem(row, 2, QTableWidgetItem(str(text["ORDEM"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(text["LOTE"])))
            self.table.setItem(
                row, 4, QTableWidgetItem(str(text["AREA_RESPONSAVEL"]))
            )
            self.table.setItem(row, 5, QTableWidgetItem(str(text["OPERACAO"])))
            self.table.setItem(
                row, 6, QTableWidgetItem(str(text["NAO_CONFORMIDADE"]))
            )
            self.table.setItem(
                row, 7, QTableWidgetItem(str(text["QUANTIDADE"]))
            )
            self.table.setItem(
                row, 8, QTableWidgetItem(str(text["QUANTIDADE_REPROVADA"]))
            )
            self.table.setItem(row, 9, QTableWidgetItem(str(text["ACAO"])))

            data_format = self.db_instance.convertDate(text["DATA"])
            self.table.setItem(row, 10, QTableWidgetItem(str(data_format)))
            self.table.setItem(
                row, 11, QTableWidgetItem(str(text["RESPONSAVEL"]))
            )

            s_ro = 'Não'
            if str(text["S_RO"]) == 'true':
                s_ro = 'Sim'
            self.table.setItem(row, 12, QTableWidgetItem(str(s_ro)))
            self.table.setItem(row, 13, QTableWidgetItem(str(text["OBS"])))

        self.db_instance.closeDB()
        self.ui_page.lbl_totalRegistros.setText(
            f'Total de registro(s): {len(results)}'
        )

    def carregaTable_pesquisa(self, lista: dict = {}):
        self.table.clearContents()
        self.table.setRowCount(0)

        for row, text in enumerate(lista):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(text["ID"])))
            try:
                item = int(text["ITEM"])
            except ValueError:
                item = text["ITEM"]

            self.table.setItem(row, 1, QTableWidgetItem(str(item)))
            self.table.setItem(row, 2, QTableWidgetItem(str(text["ORDEM"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(text["LOTE"])))
            self.table.setItem(
                row, 4, QTableWidgetItem(str(text["AREA_RESPONSAVEL"]))
            )
            self.table.setItem(row, 5, QTableWidgetItem(str(text["OPERACAO"])))
            self.table.setItem(
                row, 6, QTableWidgetItem(str(text["NAO_CONFORMIDADE"]))
            )
            self.table.setItem(
                row, 7, QTableWidgetItem(str(text["QUANTIDADE"]))
            )
            self.table.setItem(
                row, 8, QTableWidgetItem(str(text["QUANTIDADE_REPROVADA"]))
            )
            self.table.setItem(row, 9, QTableWidgetItem(str(text["ACAO"])))

            data_format = self.db_instance.convertDate(text["DATA"])
            self.table.setItem(row, 10, QTableWidgetItem(str(data_format)))
            self.table.setItem(
                row, 11, QTableWidgetItem(str(text["RESPONSAVEL"]))
            )

            s_ro = 'Não'
            if str(text["S_RO"]) == 'true':
                s_ro = 'Sim'
            self.table.setItem(row, 12, QTableWidgetItem(str(s_ro)))
            self.table.setItem(row, 13, QTableWidgetItem(str(text["OBS"])))

        self.db_instance.closeDB()
        self.ui_page.lbl_totalRegistros.setText(
            f'Total de registro(s): {len(lista)}'
        )
