from PySide6.QtWidgets import QFrame, QStackedWidget
from PySide6.QtGui import QIntValidator
from widgets.pages.ui_pages import Ui_StackedWidget
from typing import TYPE_CHECKING
from widgets.slots import EventsBtn
from widgets.tables import tableEdit
from widgets.combobox import UploadCB
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
        self.table = tableEdit(self.ui_page)
        self.table.carregaTable()

        # UPLOADED COMBOBOX
        self.cb = UploadCB(self.ui_page)
        self.cb.AreasIdentificacao()
        self.cb.AreaNC()
        self.cb.motivosNC()
        self.cb.fiedsBuscar()

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

    def validaCampos(self):
        self.ui_page.text_qtde.setValidator(QIntValidator())
        self.ui_page.text_qtdeRep.setValidator(QIntValidator())
        self.ui_page.text_data.setInputMask('99/99/9999')
        self.ui_page.text_data.editingFinished.connect(self.events.dataValida)
