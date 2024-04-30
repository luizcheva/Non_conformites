from PySide6.QtWidgets import QMessageBox, QApplication
from db.conn import DataBase
import sys
import os


class verificaUsuario(DataBase):
    def __init__(self) -> None:
        super().__init__()
        self.usuario_atual = os.environ.get('USERNAME')

    def buscaUsuario(self):
        query = (
            f'SELECT USERNAME FROM usuarios '
            f'WHERE USERNAME = "{self.usuario_atual}"'
        )
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def verificarUsuario(self):
        busca = self.buscaUsuario()
        msg = QMessageBox()

        if not len(busca) > 0:
            msg.setWindowTitle('Cadastro de novo usuário')
            msg.setText(
                f'Seja bem-vindo {self.usuario_atual},\n'
                f'Por gentileza informe sua planta atual.'
            )
            btn_neodent = msg.addButton("4400", QMessageBox.ActionRole)
            btn_clear = msg.addButton("4401", QMessageBox.ActionRole)
            msg.exec()
            if msg.clickedButton() == btn_neodent:
                return 4400
            elif msg.clickedButton() == btn_clear:
                return 4401

        return None

    def cadastroUsuario(self):
        verifica = self.verificarUsuario()
        if verifica is None:
            return

        planta = verifica
        uNumber = self.usuario_atual
        tipo = 'COLABORADOR'
        nome = 'SYSTEM'
        query = (
            f'INSERT INTO usuarios (USERNAME, NAME, PLANTA, TIPO) '
            f'VALUES("{uNumber}", "{nome}", {planta}, "{tipo}");'
        )
        self.cursor.execute(query)
        self.connection.commit()
        self.closeDB()
        registro_planta = 'NEODENT' if planta == 4400 else 'CLEAR CORRECT'
        return f'Usuário {uNumber} foi registrado na {registro_planta}.'

    def identificacao(self):
        verifica = self.cadastroUsuario()
        if verifica is not None:
            print(verifica)

        db = DataBase()
        user = os.environ.get('USERNAME')
        db.cursor.execute(
            f'SELECT * FROM usuarios WHERE USERNAME = "{user}"'
        )
        data_user = db.cursor.fetchall()
        planta = data_user[0][3]
        db.closeDB()
        return planta


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user = verificaUsuario()
    verifica = user.cadastroUsuario()
    print(verifica)
