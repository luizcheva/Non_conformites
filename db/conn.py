import sqlite3
from datetime import datetime
from information import Message
import os

ROOT_DIR = (
    "\\\\straumann.com\\public\\br03\\pcoudir\\Controle de Qualidade"
    "\\01. 4400\\01. CQ Geral\\04. Pessoal\\01. Luiz Cheva"
    "\\NaoConformidades\\_database\\"
)
DB_NAME = 'db_qualitson.sqlite3'
DB_FILE = ROOT_DIR + DB_NAME


class DataBase():
    def __init__(self) -> None:
        self.name = DB_FILE
        self.connectDB()

    def connectDB(self):
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()
        except Exception as err:
            msg_erro = Message(
                'Error', f'Ops, algo deu errado ao se conectar.\n"{err}"'
            )
            msg_erro.errorMsg()

    def selectTable(self, table_name='4400'):
        table = table_name
        self.cursor.execute(
            f'SELECT * FROM [{table}] ORDER BY "ID" DESC;'
        )
        columns = [column[0] for column in self.cursor.description]
        data_table = [
            dict(zip(columns, row)) for row in self.cursor.fetchall()
        ]
        return data_table

    def selectQueries(
        self, table_name='4400', column='', search=''
    ):
        table = table_name
        coluna = column
        pesquisa = search
        self.cursor.execute(
            f"SELECT * FROM [{table}] WHERE {coluna} LIKE '%{pesquisa}%';"
        )
        columns = [column[0] for column in self.cursor.description]
        data = [
            dict(zip(columns, row)) for row in self.cursor.fetchall()
        ]
        return data

    def selectColumn(self, table_name='4400', column=''):
        table = table_name
        coluna = column
        self.cursor.execute(
            f'SELECT {coluna} FROM [{table}];'
        )
        data = self.cursor.fetchall()
        return data

    def insertData(
        self, table_name='4400', fullDataSet: dict = {}
    ):
        fieldsTable = (
            'ITEM', 'ORDEM', 'LOTE', 'AREA_RESPONSAVEL', 'OPERACAO',
            'NAO_CONFORMIDADE', 'QUANTIDADE', 'QUANTIDADE_REPROVADA',
            'ACAO', 'DATA', 'RESPONSAVEL', 'S_RO', 'OBS'
        )
        valuesTable = (
            ":item, :ordem, :lote, :area, :operacao, :nc, :qtde, :qtde_rep,"
            ":acao, :data, :responsavel, :s_ro, :obs"
        )
        sql = (
            f'INSERT INTO [{table_name}] {fieldsTable} VALUES ({valuesTable})'
        )
        self.cursor.execute(sql, fullDataSet)
        self.connection.commit()
        self.closeDB()
        return "OK"

    def updateData(
        self, table_name='4400', fullDataSet: tuple = ()
    ):
        sql = f"UPDATE [{table_name}] SET " \
                "ITEM = ?, ORDEM = ?, " \
                "LOTE = ?, AREA_RESPONSAVEL = ?, " \
                "OPERACAO = ?, NAO_CONFORMIDADE = ?, " \
                "QUANTIDADE = ?, QUANTIDADE_REPROVADA = ?, " \
                "ACAO = ?, DATA = ?, " \
                "RESPONSAVEL = ?, S_RO = ?, " \
                "OBS = ? WHERE ID = ?;"
        try:
            self.cursor.execute(sql, fullDataSet)
            self.connection.commit()
            self.closeDB()
            return "OK"
        except ValueError as err:
            msg = Message(
                'Error ao editar o registro.',
                f'Desculpe, algo inesperado aconteceu.\n Erro: {err}'
            )
            msg.errorMsg()
            pass

    def pesquisaPeriodo(
        self, table_name='4400', data_inicio='', data_fim=''
    ):
        dataInicio = str(datetime.strftime(data_inicio, '%Y-%m-%d'))
        dataFim = (datetime.strftime(data_fim, '%Y-%m-%d'))
        sql = (
            f"SELECT * FROM [{table_name}] WHERE DATA >= '{dataInicio}' "
            f"AND DATA <= '{dataFim}';"
        )
        self.cursor.execute(sql)
        columns = [column[0] for column in self.cursor.description]
        data = [
            dict(zip(columns, row)) for row in self.cursor.fetchall()
        ]
        return data

    def closeDB(self):
        try:
            self.cursor.close
            self.connection.close
        except AttributeError:
            pass

    def convertDate(self, data_str):
        try:
            data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")

        data_formatada = data_hora.strftime("%d/%m/%Y")

        return data_formatada

    def users(self):
        usuario_atual = os.environ.get('USERNAME')
        table_name = 'usuarios'
        sql = f'SELECT * FROM {table_name} WHERE USERNAME = "{usuario_atual}"'
        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        self.closeDB
        return data

    def deleteRegister(self, table_name='4400', id_number=''):
        try:
            id_ = int(id_number)
            sql = f'DELETE FROM [{table_name}] WHERE ID = {id_};'
            self.cursor.execute(sql)
            self.connection.commit()
            self.closeDB()
            return True
        except ValueError:
            msg = Message(
                'Error ao deletar',
                f'Desculpe, erro ao deleta o ID "{id_number}".'
            )
            msg.errorMsg()

        return False

    def uploadListUser(self, table_name='4400', colaborador=''):
        try:
            sql = f"SELECT * FROM [{table_name}] WHERE \
                    RESPONSAVEL LIKE '%{colaborador}%';"
            self.cursor.execute(sql)
            columns = [column[0] for column in self.cursor.description]
            data = [
                dict(zip(columns, row)) for row in self.cursor.fetchall()
            ]
            self.closeDB()
            return data
        except Exception:
            return

    def searchAll(self, table_name='4400', text=''):
        sql = f"SELECT * FROM [{table_name}] WHERE ID LIKE '%{text}%' " \
                f"OR ITEM LIKE '%{text}%' OR ORDEM LIKE '%{text}%' " \
                f"OR LOTE LIKE '%{text}%' " \
                f"OR AREA_RESPONSAVEL LIKE '%{text}%' " \
                f"OR OPERACAO LIKE '%{text}%' " \
                f"OR NAO_CONFORMIDADE LIKE '%{text}%' " \
                f"OR QUANTIDADE LIKE '%{text}%' " \
                f"OR QUANTIDADE_REPROVADA LIKE '%{text}%' " \
                f"OR ACAO LIKE '%{text}%' OR DATA LIKE '%{text}%' " \
                f"OR RESPONSAVEL LIKE '%{text}%' OR S_RO LIKE '%{text}%' " \
                f"OR OBS LIKE '%{text}%';"
        try:
            self.cursor.execute(sql)
            columns = [column[0] for column in self.cursor.description]
            data = [
                dict(zip(columns, row)) for row in self.cursor.fetchall()
            ]
            self.closeDB()
            return data
        except Exception:
            return


if __name__ == '__main__':
    db = DataBase()
    users = db.users()
    print(len(users))

    for u in users:
        for us in u:
            print(us)
