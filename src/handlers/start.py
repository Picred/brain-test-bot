from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import START_TXT

def start(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(chat_id=update.message.chat_id, text=START_TXT)
