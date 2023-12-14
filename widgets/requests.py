from db.conn import DataBase
from information import Message
from widgets.pages.ui_pages import Ui_StackedWidget
from widgets.tables import tableEdit


class requestsBD():
    def __init__(self) -> None:
        pass

    def searchDB(
        self, column_name='', value='', ui_page: Ui_StackedWidget = ''
    ):
        db = DataBase()
        cursor = db.selectQueries('nao_conformidade', column_name, value)

        if len(cursor) > 0:
            window = ui_page
            tb = tableEdit(window)
            tb.carregaTable_pesquisa(cursor)

        else:
            msg = Message(
                'Não Encontrado',
                f'Desculpe,\nNada encontrado na coluna {column_name} '
                f'com o valor de {value}.'
            )
            msg.errorMsg()
