from PySide6.QtWidgets import QFrame, QStackedWidget
from PySide6.QtGui import QIntValidator
from widgets.pages.ui_pages import Ui_StackedWidget
from typing import TYPE_CHECKING
from widgets.slots import EventsBtn
from widgets.tables import tableEdit
from widgets.combobox import UploadCB
from widgets.dialog import ShowDialog
from information import Message
if TYPE_CHECKING:
    from main_window import MainWindows


class LeftMenu(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background-color: #853275')
        self.setMaximumWidth(50)
        self.setMinimumWidth(50)


class ContentObject(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet('background-color: white')


class StatusBar(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet('background-color: #222425; color: #A7A8A9;')
        self.setMaximumHeight(30)
        self.setMinimumHeight(30)


class ContentPage(QStackedWidget):
    def __init__(self, window: 'MainWindows', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.windows = window

        self.setStyleSheet('font-size: 12pt; color: black')
        self.ui_page = Ui_StackedWidget()
        self.ui_page.setupUi(self)
        self.setCurrentWidget(self.ui_page.page_home)
        self.ui_page.stackedWidget.setCurrentWidget(self.ui_page.page_geral)

        # UPLOADED TABLE
        self.table_edit = tableEdit(self.ui_page)
        self.table_edit.carregaTable()

        # UPLOADED COMBOBOX
        self.cb = UploadCB()
        self.cb.AreasIdentificacao(self.ui_page.cmb_areaResp)
        self.cb.AreaNC(self.ui_page.cmb_areaNC)
        self.cb.motivosNC(self.ui_page.cmb_Motivos)
        self.cb.fiedsBuscar(self.ui_page.cmb_catgPergunta)

        self.def_Slot()
        self.validaCampos()

    def def_Slot(self):
        self.events = EventsBtn(self.ui_page)
        self.ui_page.btn_DadoGerais.clicked.connect(self.events.show_dadosNC)
        self.ui_page.btn_DadosNcs.clicked.connect(self.events.show_dadosDisp)
        self.ui_page.btnVoltar1.clicked.connect(self.events.btnVoltar1)
        self.ui_page.btnVoltar2.clicked.connect(self.events.btnVoltar2)
        self.ui_page.btn_Disposicao.clicked.connect(self.events.salvarInfo)
        self.ui_page.btn_buscarGeral.clicked.connect(self.events.requests)
        self.ui_page.btn_buscarPeriodo.clicked.connect(self.events.requestTime)
        self.ui_page.btn_limparFiltros.clicked.connect(self.events.clearFil)
        self.ui_page.btnAlterarRegistro.clicked.connect(self.editReg)

    def validaCampos(self):
        self.ui_page.text_qtde.setValidator(QIntValidator())
        self.ui_page.text_qtdeRep.setValidator(QIntValidator())
        self.ui_page.text_data.setInputMask('99/99/9999')
        self.ui_page.text_data.editingFinished.connect(self.events.dataValida)

    def editReg(self):
        selected_item = self.table_edit.table.selectedItems()
        is_sro = False
        if not selected_item:
            msg = Message(
                'Error: Valor Inválido',
                'Favor selecionar ao menos um item.'
            )
            msg.errorMsg()
            return
        row = selected_item[0].row()

        sro = self.table_edit.table.item(row, 12).text()
        if sro == 'Sim':
            is_sro = True

        dialog = ShowDialog(self.windows)
        dialog.initUI(
            self.table_edit.table.item(row, 0).text(),
            self.table_edit.table.item(row, 10).text(),
            '4400',
            self.table_edit.table.item(row, 2).text(),
            self.table_edit.table.item(row, 3).text(),
            self.table_edit.table.item(row, 1).text(),
            self.table_edit.table.item(row, 5).text(),
            self.table_edit.table.item(row, 11).text(),
            self.table_edit.table.item(row, 7).text(),
            self.table_edit.table.item(row, 8).text(),
            self.table_edit.table.item(row, 4).text(),
            self.table_edit.table.item(row, 6).text(),
            self.table_edit.table.item(row, 9).text(),
            self.table_edit.table.item(row, 13).text(),
            is_sro
        )
        dialog.exec()
