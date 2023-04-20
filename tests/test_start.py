from src.handlers.start import start
from src.data.costanti import START_TXT
from pytest_mock import MockerFixture
from telegram import Update
from telegram.ext import CallbackContext


def test_start(mocker: MockerFixture) -> None:
    # Arrange
    update = mocker.Mock(Update)
    context = mocker.Mock(CallbackContext)

    # Act
    start(update, context)

    # Assert
    # verifica che la funzione sendMessage() del bot sia stata chiamata con gli argomenti corretti
    context.bot.sendMessage.assert_called_once_with(chat_id=update.message.chat_id, text=START_TXT)
