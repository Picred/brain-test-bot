from telegram import Update
from telegram.ext import CallbackContext, Filters

start_txt = "Benvenuto al Brain Test Quiz! Scegli la categoria: /difficolta o /categoria2"

def start(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(chat_id=update.message.chat_id, text=start_txt)
