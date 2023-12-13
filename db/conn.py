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

    def queries(self, table_name='nao_conformidade', column='', search=''):
        table = table_name
        coluna = column
        pesquisa = search
        self.cursor.execute(
            f'SELECT * FROM {table} WHERE {coluna} = {pesquisa};'
        )
        data = self.cursor.fetchall()
        return data

    def selectColumn(self, table_name='nao_conformidade', column=''):
        table = table_name
        coluna = column
        self.cursor.execute(
            f'SELECT {coluna} FROM {table};'
        )
        data = self.cursor.fetchall()
        return data

    def closeDB(self):
        try:
            self.cursor.close
            self.connection.close
        except AttributeError:
            pass

    def convertDate(self, data_str):
        data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f")
        data_formatada = data_hora.strftime("%d/%m/%Y")

        return data_formatada


if __name__ == '__main__':
    db = DataBase()
    consulta = db.selectTable()

    for text in consulta:
        data_ant = text["DATA"]
        datac = db.convertDate(data_ant)
        # print(datac)

        try:
            item_int = int(text["ITEM"])
        except ValueError:
            item_int = text["ITEM"]

        print(item_int)

    db.closeDB()
