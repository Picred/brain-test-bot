"""/start command test"""
from src.handlers.start import start
from src.data.costanti import START_TXT
from pytest_mock import MockerFixture
from telegram import Update
from telegram.ext import CallbackContext


def test_start(mocker: MockerFixture) -> None:
    """Tests the /start command.

    Args:
        mocker: mocker used to simulate events
    """
    update = mocker.Mock(Update)
    context = mocker.Mock(CallbackContext)

    start(update, context)

    context.bot.sendMessage.assert_called_once_with(chat_id=update.message.chat_id, text=START_TXT)
