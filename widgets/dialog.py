from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from widgets.pages.ui_dialog import Ui_Dialog
from information import Message
from widgets.combobox import UploadCB
from datetime import datetime
from db.conn import DataBase
from validation.form_validator import FormValidator


class ShowDialog(QDialog):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.Dialog)
        self.setWindowTitle('Alteração do registro: XX')
        self.cb = UploadCB()
        self.cb.AreasIdentificacao(self.ui.cmb_areaResp)
        self.cb.AreaNC(self.ui.cmb_areaNC)
        self.cb.motivosNC(self.ui.cmb_Motivos)
        self.events()
        self.validaCampos()

    def initUI(
        self, id,
        data, planta, ordem, lote, item, area, responsavel,
        qtde, qtde_rep, area_nc, motivo, acao, obs, sro
    ):
        try:
            self.id_number = int(id)
        except ValueError:
            pass

        self.ui.text_data.setText(data)
        self.ui.text_planta.setText(planta)
        self.ui.text_ordem.setText(ordem)
        self.ui.text_lote.setText(lote)
        self.ui.text_item.setText(item)
        self.ui.cmb_areaResp.setCurrentText(area)
        self.ui.text_respIden.setText(responsavel)
        self.ui.text_qtde.setText(qtde)
        self.ui.text_qtdeRep.setText(qtde_rep)
        self.ui.cmb_areaNC.setCurrentText(area_nc)
        self.ui.cmb_Motivos.setCurrentText(motivo)
        self.ui.text_acao.setText(acao)
        self.ui.text_Obs.setText(obs)
        if sro:
            self.ui.btnSimRo.setChecked(True)
        else:
            self.ui.btnNaoRo.setChecked(True)

        self.setWindowTitle(f'Alteração do registro: {self.id_number}')

    def events(self):
        self.ui.btnVoltar1.clicked.connect(self.fechar)
        self.ui.btn_DadosNcs.clicked.connect(self.editData)

    def fechar(self):
        msg = Message('Atenção', 'Deseja cancelar a edição do registro?')
        resposta = msg.questionMsg()
        if resposta == QMessageBox.StandardButton.Yes:
            self.accept()

    def editData(self):
        question = Message(
            'Atenção',
            f'Deseja editar o registro "{self.id_number}"? '
        )
        result = question.questionMsg()

        if not result == QMessageBox.StandardButton.Yes:
            return

        if not FormValidator.validate_form(self):
            return

        try:
            data_format = datetime.strptime(
                    self.ui.text_data.text(), "%d/%m/%Y"
                )
            sro_value = 'true' if self.ui.btnSimRo.isChecked() else 'false'

            data_value = (
                self.ui.text_item.text(),
                int(self.ui.text_ordem.text()),
                self.ui.text_lote.text(),
                self.ui.cmb_areaNC.currentText(),
                self.ui.cmb_areaResp.currentText(),
                self.ui.cmb_Motivos.currentText(),
                float(self.ui.text_qtde.text()),
                float(self.ui.text_qtdeRep.text()),
                self.ui.text_acao.text(),
                str(data_format),
                self.ui.text_respIden.text(),
                sro_value,
                self.ui.text_Obs.toPlainText(),
                self.id_number
            )

            db = DataBase()
            db.updateData('nao_conformidade', data_value)

            msg = Message(
                'Sucesso',
                'Registro editado com sucesso.'
            )
            msg.informationMsg()

            self.accept()
        except Exception as err:
            print(err)
            msg = Message(
                'Error ao converter',
                f'Valores Inválidos.\n Error: "{err}"'
            )
            msg.errorMsg()
            return

    def validaCampos(self):
        self.ui.text_qtde.setValidator(QIntValidator())
        self.ui.text_qtdeRep.setValidator(QIntValidator())
        self.ui.text_data.setInputMask('99/99/9999')
        self.ui.text_data.editingFinished.connect(self.dataValida)
        self.ui.text_data.setProperty("validator", "date")
        self.ui.text_planta.setProperty("validator", "text")
        self.ui.text_ordem.setProperty("validator", "number")
        self.ui.text_lote.setProperty("validator", "required")
        self.ui.text_item.setProperty("validator", "required")
        self.ui.cmb_areaResp.setProperty("validator", "combo")
        self.ui.text_respIden.setProperty("validator", "required")
        self.ui.text_qtde.setProperty("validator", "number")
        self.ui.text_qtdeRep.setProperty("validator", "number")
        self.ui.cmb_areaNC.setProperty("validator", "combo")
        self.ui.cmb_Motivos.setProperty("validator", "combo")
        self.ui.text_acao.setProperty("validator", "required")
        self.ui.group_SRo.setProperty("validator", "radio_group")
        self.ui.group_Email.setProperty("validator", "radio_group")

    def dataValida(self):
        data_str = self.ui.text_data.text()
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            return data
        except ValueError:
            msg = Message('Data Errada', f'A data {data_str} é inválida.')
            msg.errorMsg()
            self.ui.text_data.clear()
            self.ui.text_data.setFocus()

        return None
