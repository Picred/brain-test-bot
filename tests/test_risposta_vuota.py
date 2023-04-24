from pytest_mock import MockerFixture
from unittest.mock import patch
from src.handlers.risposta import risposta_vuota
import src.handlers.load_file
from src.data.costanti import ESEMPIO_DATA as mock_data


def test_risposta_vuota(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    rm_id = mocker.Mock()
    mocker.patch.object(src.handlers.risposta, "load_file", return_value=mock_data)

    with patch('src.handlers.risposta.prossima_domanda') as mocked_prossima_domanda:
        risposta_vuota(update,context,rm_id)

    context.bot.sendMessage.assert_called_once_with(chat_id=update.effective_chat.id, text="Tempo scaduto!")
    context.bot.editMessageReplyMarkup.assert_called_once_with(chat_id=update.effective_chat.id, message_id=rm_id)
    mocked_prossima_domanda.assert_called_once_with(update,context,mock_data)


def test1_risposta_vuota(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    update.callback_query=mocker.Mock()
    context = mocker.Mock()
    rm_id = mocker.Mock()
    mocker.patch.object(src.handlers.risposta, "load_file", return_value=mock_data)

    with patch('src.handlers.risposta.prossima_domanda') as mocked_prossima_domanda:
        risposta_vuota(update,context,rm_id)

    context.bot.sendMessage.assert_called_once_with(chat_id=update.effective_chat.id, text="Tempo scaduto!")
    context.bot.editMessageReplyMarkup.assert_called_once_with(chat_id=update.effective_chat.id, message_id=rm_id)
    mocked_prossima_domanda.assert_called_once_with(update,context,mock_data)
