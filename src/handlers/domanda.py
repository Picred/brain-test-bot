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
    match context.user_data[LIVELLO]:
        case "1: Facile":
            path = 'facile.json'
        case "2: Intermedio":
            path = 'intermedio.json'
        case "3: Difficile":
            path = 'difficile.json'

    with open(f'src/data/{path}', 'r', encoding="utf-8") as f:
        data = json.load(f)[f"{context.user_data[CATEGORIA]}"]

    return data
