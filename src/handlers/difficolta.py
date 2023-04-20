from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from src.data.costanti import LIVELLO
import json

with open("src/data/livelli.json", "r", encoding="utf-8") as f:
    livelli = json.load(f)

def difficolta(update: Update, context: CallbackContext) -> None:
    if LIVELLO in context.user_data:
        del context.user_data[LIVELLO]

    categorie_reply_markup = [[l] for l in livelli]
    reply_markup = ReplyKeyboardMarkup(categorie_reply_markup, resize_keyboard=True, one_time_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id,text="Scegli il livello di difficoltà:",reply_markup=reply_markup)
