"""/categoria command"""
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from src.data.costanti import CATEGORIA
import json

with open("src/data/categorie.json", "r", encoding="utf-8") as f:
    categorie = json.load(f)


def categoria(update: Update, context: CallbackContext) -> None:
    """Sets the category of the questions.

    Args:
        update: update event
        context: context passed by the handler
    """
    if CATEGORIA in context.user_data:
        del context.user_data[CATEGORIA]

    categorie_reply_markup = [[c] for c in categorie]
    reply_markup = ReplyKeyboardMarkup(categorie_reply_markup, resize_keyboard=True, one_time_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id,text="Scegli la categoria delle domande:", reply_markup=reply_markup)
