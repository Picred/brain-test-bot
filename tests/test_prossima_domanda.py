from unittest.mock import patch
from pytest_mock import MockerFixture
from src.handlers.risposta import prossima_domanda
from src.data.costanti import DOMANDA_CORRENTE, PUNTEGGIO

def test_prossima_domanda(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    context=mocker.Mock()
    data=mocker.Mock()
    context.user_data={DOMANDA_CORRENTE: 0}
    with patch('src.handlers.risposta.len', return_value=5):
        with patch('src.handlers.risposta.domanda') as mocked_domanda:
            prossima_domanda(update,context,data)

            mocked_domanda.assert_called_once_with(update,context)

def test1_prossima_domanda(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    context=mocker.Mock()
    data=mocker.Mock()
    context.user_data={DOMANDA_CORRENTE: 5, PUNTEGGIO: 0}
    punteggio = 0
    len_data = 5
    with patch('src.handlers.risposta.len', return_value=len_data):
        with patch('src.handlers.risposta.genera_commento') as mocked_genera_commento:
            prossima_domanda(update,context,data)

            context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id, text=f"Hai terminato il quiz!\nHai totalizzato {punteggio}/{len_data} punti!")
            mocked_genera_commento.assert_called_once_with(update,context)
