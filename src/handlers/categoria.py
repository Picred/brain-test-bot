from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
import json

with open("src/Data/categorie.json", "r") as f:
   categorie=json.load(f)

# Imposta la categoria
def categoria(update: Update, context: CallbackContext) -> None:
    # Genera la tastiera per la scelta  delle categorie
    reply_markup = ReplyKeyboardMarkup([ [c] for c in categorie], resize_keyboard=True, one_time_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id,text="Scegli il livello di difficoltà:",reply_markup=reply_markup)