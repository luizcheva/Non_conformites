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

    def selectTable(self, table_name='nao_conformidade'):
        self.table_name = table_name
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f'SELECT * FROM {table_name} ORDER BY "ID" DESC;'
        )
        columns = [column[0] for column in self.cursor.description]
        data_table = [
            dict(zip(columns, row)) for row in self.cursor.fetchall()
        ]
        return data_table

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
