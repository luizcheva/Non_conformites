import sqlite3
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


class DataBase():
    def __init__(self, name=DB_FILE) -> None:
        self.name = name
        self.connectDB()

    def connectDB(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    def selectTable(self, table_name='nao_conformidade'):
        table = table_name
        self.cursor.execute(
            f'SELECT * FROM {table} ORDER BY "ID" DESC;'
        )
        columns = [column[0] for column in self.cursor.description]
        data_table = [
            dict(zip(columns, row)) for row in self.cursor.fetchall()
        ]
        return data_table

    def selectQueries(
        self, table_name='nao_conformidade', column='', search=''
    ):
        table = table_name
        coluna = column
        pesquisa = search
        self.cursor.execute(
            f"SELECT * FROM {table} WHERE {coluna} LIKE '%{pesquisa}%';"
        )
        columns = [column[0] for column in self.cursor.description]
        data = [
            dict(zip(columns, row)) for row in self.cursor.fetchall()
        ]
        return data

    def selectColumn(self, table_name='nao_conformidade', column=''):
        table = table_name
        coluna = column
        self.cursor.execute(
            f'SELECT {coluna} FROM {table};'
        )
        data = self.cursor.fetchall()
        return data

    def insertData(
        self, table_name='nao_conformidade', fullDataSet: dict = {}
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
        sql = f'INSERT INTO {table_name} {fieldsTable} VALUES ({valuesTable})'
        self.cursor.execute(sql, fullDataSet)
        self.connection.commit()
        self.closeDB()
        return "OK"

    def pesquisaPeriodo(
        self, table_name='nao_conformidade', data_inicio='', data_fim=''
    ):
        dataInicio = str(datetime.strftime(data_inicio, '%Y-%m-%d'))
        dataFim = (datetime.strftime(data_fim, '%Y-%m-%d'))
        sql = (
            f"SELECT * FROM {table_name} WHERE DATA >= '{dataInicio}' "
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
