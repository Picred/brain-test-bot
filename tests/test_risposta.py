from pytest_mock import MockerFixture
from unittest.mock import patch
from src.handlers.risposta import risposta
from src.data.costanti import PUNTEGGIO, ESEMPIO_DATA as data


def test_risposta(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    update.callback_query.data="0:0"
    context=mocker.Mock()
    job = mocker.Mock()
    mocker.patch.object(context.job_queue, "jobs", return_value=tuple([job]))
    context.user_data = {PUNTEGGIO : 0}

    with patch("src.handlers.risposta.load_file", return_value=data):
        with patch("src.handlers.risposta.prossima_domanda") as mocked_prossima_domanda:

            risposta(update,context)

            mocked_prossima_domanda.assert_called_once_with(update,context,data)

    job.remove.assert_called_once()
    context.bot.editMessageReplyMarkup.assert_called_once_with(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
    context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id,text="Hai risposto correttamente!")
    assert context.user_data[PUNTEGGIO] == 1


def test1_risposta(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    update.callback_query.data="0:1"
    context=mocker.Mock()
    job = mocker.Mock()
    mocker.patch.object(context.job_queue, "jobs", return_value=tuple([job]))
    context.user_data = {PUNTEGGIO : 0}

    risposta_corretta = data[0]['risposte'][0]['testo_risposta']


    with patch("src.handlers.risposta.load_file", return_value=data):
        with patch("src.handlers.risposta.prossima_domanda") as mocked_prossima_domanda:
            risposta(update,context)
            mocked_prossima_domanda.assert_called_once_with(update,context,data)

    job.remove.assert_called_once()
    context.bot.editMessageReplyMarkup.assert_called_once_with(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
    context.bot.sendMessage.assert_called_once_with(chat_id=update.effective_chat.id,text=f"La risposta corretta era \"{risposta_corretta}\"")
    context.bot.send_message.assert_called_once_with(chat_id=update.effective_chat.id,text="Spiacente, la risposta è errata.")
    assert context.user_data[PUNTEGGIO] == 0
