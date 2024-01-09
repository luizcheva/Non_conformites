import os
from datetime import datetime
from PySide6.QtWidgets import (
    QFrame, QStackedWidget, QCheckBox, QLineEdit,
    QGroupBox, QRadioButton, QComboBox, QTextEdit
)
from PySide6.QtGui import QIntValidator
from widgets.pages.ui_pages import Ui_StackedWidget
from typing import TYPE_CHECKING
from widgets.slots import EventsBtn
from widgets.tables import tableEdit
from widgets.combobox import UploadCB
from widgets.dialog import ShowDialog
from information import Message
from db.insertDB import insertNew
from validation.form_validator import FormValidator
from widgets.list import listView
from widgets.email import NewEmail
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
        self.lista = listView(self.ui_page)

        # UPLOADED TABLE
        self.atualizarTabelas()

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
        self.ui_page.btn_Disposicao.clicked.connect(self.salvarInfo)
        self.ui_page.btn_buscarGeral.clicked.connect(self.events.requests)
        self.ui_page.btn_buscarPeriodo.clicked.connect(self.events.requestTime)
        self.ui_page.btn_limparFiltros.clicked.connect(self.events.clearFil)
        self.ui_page.btnAlterarRegistro.clicked.connect(self.editReg)
        self.ui_page.btnAddId.clicked.connect(self.addIDtoList)
        self.ui_page.btnDeleteRegister.clicked.connect(self.lista.deleteItems)
        self.ui_page.btnDelId.clicked.connect(self.deleteIDtoList)
        self.ui_page.btnBuscar_del.clicked.connect(self.events.searchDel)
        self.ui_page.btn_NaoEmail.clicked.connect(self.desabilitaEmail)
        self.ui_page.btn_SimEmail.clicked.connect(self.habilitaEmail)

    def validaCampos(self):
        self.ui_page.text_qtde.setValidator(QIntValidator())
        self.ui_page.text_qtdeRep.setValidator(QIntValidator())
        self.ui_page.text_data.setInputMask('99/99/9999')
        self.ui_page.text_data.editingFinished.connect(self.events.dataValida)
        self.ui_page.text_data.setProperty("validator", "date")
        self.ui_page.text_planta.setProperty("validator", "text")
        self.ui_page.text_ordem.setProperty("validator", "number")
        self.ui_page.text_lote.setProperty("validator", "required")
        self.ui_page.text_item.setProperty("validator", "required")
        self.ui_page.cmb_areaResp.setProperty("validator", "combo")
        self.ui_page.text_respIden.setProperty("validator", "required")
        self.ui_page.text_qtde.setProperty("validator", "number")
        self.ui_page.text_qtdeRep.setProperty("validator", "number")
        self.ui_page.cmb_areaNC.setProperty("validator", "combo")
        self.ui_page.cmb_Motivos.setProperty("validator", "combo")
        self.ui_page.text_acao.setProperty("validator", "required")
        self.ui_page.group_SRo.setProperty("validator", "radio_group")
        self.ui_page.group_Email.setProperty("validator", "radio_group")

    def salvarInfo(self):
        msg = Message(
           'Salvar dados no Banco de dados',
           'Deseja realmente salvar os dados?'
        )
        result = msg.questionMsg()
        if result == msg.StandardButton.Yes:
            if not FormValidator.validate_form(self.windows):
                return

            if self.ui_page.btn_SimEmail.isChecked():
                self.list_email = []
                for opt in self.ui_page.group_addressEmail.findChildren(
                    QCheckBox
                ):
                    if isinstance(opt, QCheckBox):
                        if opt.isChecked():
                            self.list_email.append(opt.text())
                if len(self.list_email) == 0:
                    msg_email = Message(
                        'Nenhum e-mail selecionado',
                        'Desculpe, não foi selecionado nenhum e-mail '
                        'para envio.'
                    )
                    msg_email.errorMsg()
                    return

            inserir = insertNew(self.windows)
            inserir.salvarDados()

            if self.ui_page.btn_SimEmail.isChecked():
                self.enviarEmail()

            self.clearData()
            self.camposPadrao()
            self.ui_page.stackedWidget.setCurrentWidget(
                self.ui_page.page_geral
            )
            self.atualizarTabelas()

    def editReg(self):
        selected_item = self.table_edit.ui_page.tab_dados.selectedItems()
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
        self.atualizarTabelas()

    def addIDtoList(self):
        self.lista.uploadList(self.ui_page.tabDados_del)

    def deleteIDtoList(self):
        self.lista.removeItem()

    def atualizarTabelas(self):
        self.table_edit = tableEdit(self.ui_page)
        self.table_edit.carregaTable(self.ui_page.tab_dados)
        self.table_edit.carregaTable(self.ui_page.tabDados_del)

    def habilitaEmail(self):
        self.ui_page.group_addressEmail.setEnabled(True)

    def desabilitaEmail(self):
        self.ui_page.group_addressEmail.setEnabled(False)

    def enviarEmail(self):
        self.windows.bottom_bar_layout.left_lbl.setText(
            'Aguarde estamos enviando o e-mail.'
        )
        email = NewEmail()
        ordem = self.ui_page.text_ordem.text()
        print(ordem)
        email.new_email(
            self.list_email,
            4400,
            self.ui_page.cmb_Motivos.currentText(),
            int(self.ui_page.text_ordem.text()),
            self.ui_page.text_item.text(),
            self.ui_page.text_lote.text()
        )
        self.windows.bottom_bar_layout.left_lbl.setText(
            'Criado por: Luiz Cheva'
        )

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

    def camposPadrao(self):
        data_hoje = datetime.now()
        data_hoje = data_hoje.strftime("%d/%m/%Y")
        self.ui_page.text_data.setText(data_hoje)
        self.ui_page.text_respIden.setText(os.getlogin())
