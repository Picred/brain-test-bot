from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import json

# todo apri il file in base alla dif. selezionata e imposta il timer
with open('src/data/facile.json', 'r', encoding="utf-8") as f:
    data = json.load(f)['domande']

def domanda(update: Update, context: CallbackContext):
    domanda_corrente = context.user_data['domanda_corrente']   
    
    question = data[domanda_corrente]
    testo = question['testo']
    risposte = question['risposte']

    keyboard = [[InlineKeyboardButton(j['testo'], callback_data=f'{domanda_corrente}:{i}')] for i, j in enumerate(risposte)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=testo, reply_markup=reply_markup)
