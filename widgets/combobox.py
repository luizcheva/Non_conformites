from db.conn import DataBase
from PySide6.QtWidgets import QComboBox


class UploadCB():
    def AreasIdentificacao(self, combobox: QComboBox):
        setores = ('CQ_ACQ', 'CQ_HIG', 'CQ_INF', 'CQ_LAB', 'CQ_TRS')
        for setor in setores:
            combobox.addItem(setor)

    def AreaNC(self, combobox: QComboBox):
        conn = DataBase()
        cursor = conn.selectColumn('Sectors', 'SECTOR')

        for values in cursor:
            for setor in values:
                combobox.addItem(setor)

        conn.closeDB()

    def motivosNC(self, combobox: QComboBox):
        conn = DataBase()
        cursor = conn.selectColumn('Reasons', 'DESCRIPTION')

        for values in cursor:
            for motivo in values:
                combobox.addItem(motivo)

        conn.closeDB()

    def fiedsBuscar(self, combobox: QComboBox):
        conn = DataBase()
        cursor = conn.cursor.execute(
            'SELECT * FROM nao_conformidade ORDER BY ID DESC LIMIT 1;'
        )

        for col in cursor.description:
            nome_col = col[0]
            combobox.addItem(nome_col)

        conn.closeDB()
