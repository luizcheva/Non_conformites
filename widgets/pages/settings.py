from typing import TYPE_CHECKING
from db.conn import DataBase
from widgets.tables import tableEdit
import os
if TYPE_CHECKING:
    from main_window import MainWindows


class Settings_():
    def __init__(self, windows: 'MainWindows') -> None:
        self.windows = windows
        self.ui_page = self.windows.content_page.ui_page
        self.initUI()

    def initUI(self):
        user = os.getlogin()
        self.ui_page.text_Colaborador.setText(user)
        self.ui_page.text_Colaborador.setEnabled(False)

        db = DataBase()
        data_results = db.uploadListUser('nao_conformidade', user)

        if data_results is None:
            return

        self.ui_page.lcd_totalRegistro.display(len(data_results))
        contador = 0.0
        for data in data_results:
            if data['S_RO'] == 'true':
                contador += 1

        self.ui_page.lcd_TotalSRO.display(contador)

        tb = tableEdit(self.ui_page)
        tb.carregaTable_Col(
            self.ui_page.tab_DadosColaborador,
            data_results
        )
