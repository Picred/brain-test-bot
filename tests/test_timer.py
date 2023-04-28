"""Timer test"""
from pytest_mock import MockerFixture
from unittest.mock import patch
from src.handlers.domanda import timer
from src.data.costanti import ESEMPIO_DATA as mock_data


def test_timer(mocker: MockerFixture) -> None:
    """Tests the timer function.

    Args:
        mocker: mocker used to simulate events
    """
    call_context = mocker.Mock()
    call_context.job.context = [mocker.Mock(), mocker.Mock(), mocker.Mock()]
    update = call_context.job.context[0]
    rm_id = call_context.job.context[1]
    context = call_context.job.context[2]

    with patch('src.handlers.domanda.load_file', return_value=mock_data):
        with patch('src.handlers.domanda.prossima_domanda') as mocked_prossima_domanda:
            timer(call_context)

    context.bot.sendMessage.assert_called_once_with(chat_id=update.effective_chat.id, text="Tempo scaduto!")
    context.bot.editMessageReplyMarkup.assert_called_once_with(chat_id=update.effective_chat.id, message_id=rm_id)
    mocked_prossima_domanda.assert_called_once_with(update,context,mock_data)


def test1_timer(mocker: MockerFixture) -> None:
    """Tests the timer function.

    Args:
        mocker: mocker used to simulate events
    """
    call_context = mocker.Mock()
    call_context.job.context = [mocker.Mock(), mocker.Mock(), mocker.Mock()]
    update = call_context.job.context[0]
    rm_id = call_context.job.context[1]
    context = call_context.job.context[2]

    with patch('src.handlers.domanda.load_file', return_value=mock_data):
        with patch('src.handlers.domanda.prossima_domanda') as mocked_prossima_domanda:
            timer(call_context)

    context.bot.sendMessage.assert_called_once_with(chat_id=update.effective_chat.id, text="Tempo scaduto!")
    context.bot.editMessageReplyMarkup.assert_called_once_with(chat_id=update.effective_chat.id, message_id=rm_id)
    mocked_prossima_domanda.assert_called_once_with(update,context,mock_data)
