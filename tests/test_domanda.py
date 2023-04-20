from pytest_mock import MockerFixture
from src.handlers.domanda import domanda
from unittest.mock import patch
from src.data.costanti import DOMANDA_CORRENTE

def test_domanda(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {DOMANDA_CORRENTE: 0}

    data = [
        {
            'testo': 'Questa è una domanda di esempio',
            'risposte': [
                {'testo_risposta': 'Risposta 1'},
                {'testo_risposta': 'Risposta 2'}
            ]
        }
    ]

    # sostituisco la funzione load_file con un mock (data)
    with patch('src.handlers.domanda.load_file', return_value=data):
        domanda(update, context) # Chiamata alla funzione domanda con gli oggetti mock

    assert context.bot.send_message.call_count == 1
