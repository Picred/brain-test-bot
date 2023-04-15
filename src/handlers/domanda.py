from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import json

def domanda(update: Update, context: CallbackContext) -> None:
    data = load_file(context)

    domanda_corrente = context.user_data['domanda_corrente']
    question = data[domanda_corrente]
    testo = question['testo']
    risposte = question['risposte']

    keyboard = [[InlineKeyboardButton(j['testo_risposta'], callback_data=f'{domanda_corrente}:{i}')] for i, j in enumerate(risposte)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=testo, reply_markup=reply_markup)

def load_file(context: CallbackContext) -> dict:
    if context.user_data['livello'] == "1: Facile":
        f = open('src/data/facile.json', 'r', encoding="utf-8")
    elif context.user_data['livello'] == "2: Intermedio":
        f = open('src/data/intermedio.json', 'r', encoding="utf-8")
    elif context.user_data['livello'] == "3: Difficile":
        f = open('src/data/difficile.json', 'r', encoding="utf-8")

    data = json.load(f)[f"{context.user_data['categoria']}"]

    return data
