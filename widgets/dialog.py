from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt
from widgets.pages.ui_dialog import Ui_Dialog
from information import Message
from widgets.combobox import UploadCB


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

    def initUI(
        self, id,
        data, planta, ordem, lote, item, area, responsavel,
        qtde, qtde_rep, area_nc, motivo, acao, obs, sro
    ):
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

        self.setWindowTitle(f'Alteração do registro: {id}')

    def events(self):
        self.ui.btnVoltar1.clicked.connect(self.fechar)

    def fechar(self):
        msg = Message('Atenção', 'Deseja cancelar a edição do registro?')
        resposta = msg.questionMsg()
        if resposta == QMessageBox.StandardButton.Yes:
            self.accept()
