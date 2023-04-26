from pytest_mock import MockerFixture
from src.handlers.domanda import domanda
from unittest.mock import patch
from src.data.costanti import DOMANDA_CORRENTE, LIVELLO, ESEMPIO_DATA as data


def test_domanda(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {DOMANDA_CORRENTE: 0, LIVELLO: '1: Facile'}

    with patch('src.handlers.domanda.load_file', return_value=data):
        domanda(update, context) # Chiamata alla funzione domanda con gli oggetti mock

    assert context.bot.send_message.call_count == 1
