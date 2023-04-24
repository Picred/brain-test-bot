from telegram.ext import CallbackContext
from telegram import Update
from src.data.costanti import CATEGORIA, PUNTEGGIO
import json


def genera_commento(update: Update, context: CallbackContext) -> None:
    with open('src/data/commenti.json', 'r', encoding='utf-8') as f:
        data = json.load(f)[context.user_data[CATEGORIA]]

    punteggio = context.user_data[PUNTEGGIO]

    if punteggio < 2:
        key = "0 punti"
    elif 2 <= punteggio <= 4:
        key = "3 punti"
    elif punteggio > 4:
        key = "5 punti"

    commento = data[0][key]
    context.bot.sendMessage(chat_id=update.effective_chat.id, text=commento)
