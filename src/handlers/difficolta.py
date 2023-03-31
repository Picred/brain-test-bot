from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

livelli = ["1: Facile", "2: Intermedio", "3: Difficile"]


# Imposta la difficolta
def difficolta(update: Update, context: CallbackContext) -> None:
    # Genera la tastiera per la scelta  dei livelli
    reply_markup = ReplyKeyboardMarkup([ [l] for l in livelli], resize_keyboard=True, one_time_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id,text="Scegli il livello di difficoltà:",reply_markup=reply_markup)
