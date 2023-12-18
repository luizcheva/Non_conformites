from db.conn import DataBase
from information import Message
from widgets.pages.ui_pages import Ui_StackedWidget
from widgets.tables import tableEdit
from datetime import datetime


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

    def searchPeriodo(
        self, ui_page: Ui_StackedWidget,
        data_inicio='',
        data_fim=''
    ):
        try:
            dataInicio_format = datetime.strptime(data_inicio, '%d/%m/%Y')
            dataFim_format = datetime.strptime(data_fim, '%d/%m/%Y')

            if dataInicio_format > dataFim_format:
                msg = Message(
                    'Erro - Período Inválido',
                    'Desculpe,\nA data inicial não pode ser maior '
                    'que a data final.'
                )
                msg.errorMsg()
                return

            db = DataBase()
            cursor = db.pesquisaPeriodo(
                'nao_conformidade', dataInicio_format, dataFim_format
            )

            if len(cursor) > 0:
                window = ui_page
                tb = tableEdit(window)
                tb.carregaTable_pesquisa(cursor)

            else:
                msg = Message(
                    'Não Encontrado',
                    f'Desculpe,\nNenhum registro encontrado no período de '
                    f'{data_inicio} até {data_fim}.'
                )
                msg.errorMsg()

        except ValueError:
            msg = Message('Error', 'Data inválida.')
            msg.errorMsg()
