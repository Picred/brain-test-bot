"""/start command"""
from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import START_TXT


def start(update: Update, context: CallbackContext) -> None:
    """Called by the /start command.
    Sends a welcome message

    Args:
        update: update event
        context: context passed by the handler
    """
    context.bot.sendMessage(chat_id=update.message.chat_id, text=START_TXT)
