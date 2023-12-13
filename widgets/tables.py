from db.conn import DataBase
from PySide6.QtWidgets import QTableWidgetItem


class tableEdit():
    def __init__(self, ui_page) -> None:
        self.ui_page = ui_page
        self.db_instance = DataBase()

    def carregaTable(self):
        table = self.ui_page.tab_dados
        results = self.db_instance.selectTable()

        table.clearContents()
        table.setRowCount(len(results))

        for row, text in enumerate(results):
            table.setItem(row, 0, QTableWidgetItem(str(text["ID"])))
            try:
                item = int(text["ITEM"])
            except ValueError:
                item = text["ITEM"]

            table.setItem(row, 1, QTableWidgetItem(str(item)))
            table.setItem(row, 2, QTableWidgetItem(str(text["ORDEM"])))
            table.setItem(row, 3, QTableWidgetItem(str(text["LOTE"])))
            table.setItem(
                row, 4, QTableWidgetItem(str(text["AREA_RESPONSAVEL"]))
            )
            table.setItem(row, 5, QTableWidgetItem(str(text["OPERACAO"])))
            table.setItem(
                row, 6, QTableWidgetItem(str(text["NAO_CONFORMIDADE"]))
            )
            table.setItem(row, 7, QTableWidgetItem(str(text["QUANTIDADE"])))
            table.setItem(
                row, 8, QTableWidgetItem(str(text["QUANTIDADE_REPROVADA"]))
            )
            table.setItem(row, 9, QTableWidgetItem(str(text["ACAO"])))

            data_format = self.db_instance.convertDate(text["DATA"])
            table.setItem(row, 10, QTableWidgetItem(str(data_format)))
            table.setItem(row, 11, QTableWidgetItem(str(text["RESPONSAVEL"])))

            s_ro = 'Não'
            if str(text["S_RO"]) == 'true':
                s_ro = 'Sim'
            table.setItem(row, 12, QTableWidgetItem(str(s_ro)))
            table.setItem(row, 13, QTableWidgetItem(str(text["OBS"])))

        self.db_instance.closeDB()
