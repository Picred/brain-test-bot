from src.handlers.start import start, start_txt
from unittest.mock import Mock
from telegram import Update
from telegram.ext import CallbackContext


def test_start():
    # Arrange
    update = Mock(Update)
    context = Mock(CallbackContext)

    # Act
    start(update, context)

    # Assert
    # verifica che la funzione sendMessage() del bot sia stata chiamata con gli argomenti corretti
    context.bot.sendMessage.assert_called_once_with(chat_id=update.message.chat_id, text=start_txt)
