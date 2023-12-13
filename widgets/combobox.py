from widgets.pages.ui_pages import Ui_StackedWidget
from db.conn import DataBase


class UploadCB():
    def __init__(self, ui_pages: Ui_StackedWidget) -> None:
        self.ui_pages = ui_pages

    def AreasIdentificacao(self):
        setores = ('CQ_ACQ', 'CQ_HIG', 'CQ_INF', 'CQ_LAB', 'CQ_TRS')
        for setor in setores:
            self.ui_pages.cmb_areaResp.addItem(setor)

    def AreaNC(self):
        conn = DataBase()
        cursor = conn.selectColumn('Sectors', 'SECTOR')

        for values in cursor:
            for setor in values:
                self.ui_pages.cmb_areaNC.addItem(setor)

    def motivosNC(self):
        conn = DataBase()
        cursor = conn.selectColumn('Reasons', 'DESCRIPTION')

        for values in cursor:
            for motivo in values:
                self.ui_pages.cmb_Motivos.addItem(motivo)
