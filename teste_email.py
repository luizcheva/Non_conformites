from widgets.email import NewEmail

if __name__ == "__main__":
    envia = NewEmail()
    envia.new_email(
        ['Acabamento', 'PCP', 'TNC'],
        4400,
        'Teste de Motivo',
        5010201313,
        '109.1021-1',
        'AA123'
    )
