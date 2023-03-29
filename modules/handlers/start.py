
from telegram import Update
from telegram.ext import CallbackContext

start_txt = "Benvenuto al Brain Test Quiz! Scegli la categoria: /categoria1 o /categoria2"


def start(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.message.chat_id, text=start_txt)
