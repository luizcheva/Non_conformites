from typing import TYPE_CHECKING
from db.conn import DataBase
from widgets.tables import tableEdit
from identify import verificaUsuario
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

        planta = verificaUsuario().identificacao()
        db = DataBase()
        data_results = db.uploadListUser(planta, user)

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

        if planta == 4400:
            self.ui_page.btn4400.setChecked(True)
            self.ui_page.btn4400.setDisabled(True)
        else:
            self.ui_page.btn4401.setChecked(True)
            self.ui_page.btn4401.setDisabled(True)
