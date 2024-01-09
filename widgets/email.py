import win32com.client as win32
from datetime import datetime
from libary.requests_excel import BuscarDescricao


class NewEmail:
    def __init__(self):
        super().__init__()
        outlook = win32.Dispatch('outlook.application')
        self.mail = outlook.CreateItem(0)
        self.emails = {
            "Acabamento": "m.br03.acabamento@neodent.com",
            "Higienização": "m.br03.higieni@straumann.com",
            "TRS": "m.br.tratamentosuperficie@neodent.com",
            "PCP": "me.br.pcp@neodent.com",
            "TNC": "m.br.cqtnc@neodent.com",
            "Recebimento": "me.br.recebimento@neodent.com",
            "Usinagem": "M.BR.CQUsinagem_4401@straumann.com",
            "Usinagem - Analista e Lideres": "BR05_Org_cq-usinagem-4401-\
                analistas-e-lideres@stgcs.onmicrosoft.com",
            "CNC": "M.BR05.CNC4401@neodent.com",
        }

    def new_email(
            self, setores: list, planta: int = 4400, motivo: str = '',
            ordem: int | float = 0, item: str = '', lote: str = ''
    ):
        hora = datetime.now().time().hour
        saudacao = ''

        descricao = BuscarDescricao()
        descricao_item = descricao.buscarItem(item)

        if hora >= 6 and hora <= 12:
            saudacao = 'Bom dia'
        elif hora > 12 and hora <= 18:
            saudacao = 'Boa Tarde'
        else:
            saudacao = 'Boa noite'

        email_to = ''
        for email in setores:
            email_to += self.emails[email] + ';'

        self.mail.To = email_to
        if planta == 4400:
            self.mail.CC = 'M.BR.CQLAB@straumann.com'
        else:
            self.mail.CC = 'm.br05.cq_lab_4401@straumann.com'

        self.mail.Subject = f'Não Conformidade: {motivo}'
        self.mail.display()
        assinatura = self.mail.HTMLBody

        self.mail.HTMLBody = (
            "<html><body>"
            f"<p>{saudacao},<br> A ordem retornou ao setor. <br> "
            f"Motivo {motivo.upper()}.</p>"
            "<table style='border-collapse: collapse; width: 100%; "
            "border: 1px solid black;'>"
            "<tr style='background-color: #f2f2f2;'>"
            "<td style='border: 1px solid black; padding: 8px; "
            "text-align: center;'>ORDEM</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            "text-align: center;'>ITEM</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            "text-align: center;'>DESCRIÇÃO</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            "text-align: center;'>LOTE</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            "text-align: center;'>MOTIVO</td>"
            "</tr>"
            "<tr>"
            "<td style='border: 1px solid black; padding: 8px; "
            f"text-align: center;'>{ordem}</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            f"text-align: center;'>{item}</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            f"text-align: center;'>{descricao_item}</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            f"text-align: center;'>{lote}</td>"
            "<td style='border: 1px solid black; padding: 8px; "
            f"text-align: center;'>{motivo}</td>"
            "</tr>"
            "</table>"
            "<p>Qualquer dúvida estou à disposição.</p>"
            f"</body></html> {assinatura}"
        )
        return True


if __name__ == "__main__":
    email = NewEmail()
    emails = ['Acabamento', 'TNC',]
    email.new_email(
        emails, 4400, 'Teste de motivos',
        5010201313, '109.1021-1', 'AAA156'
    )
