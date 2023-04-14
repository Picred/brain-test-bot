from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
import json

with open("src/data/categorie.json", "r", encoding="utf-8") as f:
    categorie = json.load(f)


def categoria(update: Update, context: CallbackContext) -> None:
    # Reset della categoria
    if 'categoria' in context.user_data:
        del context.user_data['categoria']
    reply_markup = ReplyKeyboardMarkup(
        [[c] for c in categorie], resize_keyboard=True, one_time_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Scegli la categoria delle domande:", reply_markup=reply_markup)
