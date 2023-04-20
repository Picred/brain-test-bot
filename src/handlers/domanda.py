from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from src.data.costanti import CATEGORIA, LIVELLO, DOMANDA_CORRENTE
import json

def domanda(update: Update, context: CallbackContext) -> None:
    data = load_file(context)

    domanda_corrente = context.user_data[DOMANDA_CORRENTE]
    question = data[domanda_corrente]
    testo = question['testo']
    risposte = question['risposte']
    
    keyboard = []
    for i, j in enumerate(risposte):
        button = InlineKeyboardButton(j['testo_risposta'], callback_data=f'{domanda_corrente}:{i}')
        keyboard.append([button])

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=testo, reply_markup=reply_markup)


def load_file(context: CallbackContext) -> dict:
    if context.user_data[LIVELLO] == "1: Facile":
        path = 'facile.json'
    elif context.user_data[LIVELLO] == "2: Intermedio":
        path = 'intermedio.json'
    elif context.user_data[LIVELLO] == "3: Difficile":
        path = 'difficile.json'

    f = open(f'src/data/{path}', 'r', encoding="utf-8")
    data = json.load(f)[f"{context.user_data[CATEGORIA]}"]

    return data
