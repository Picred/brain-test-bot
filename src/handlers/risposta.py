from telegram import Update
from telegram.ext import CallbackContext
from domanda import domanda
import json

with open('src/data/facile.json', 'r', encoding="utf-8") as f:
    data = json.load(f)['domande']

def risposta(update: Update, context: CallbackContext):
    # Numero della domanda corrente
    domanda_corrente = context.user_data['domanda_corrente']
    query = update.callback_query
    question_index, answer_index = map(int, query.data.split(':'))
    question = data[question_index]
    answer = question['risposte'][answer_index]

    # Verifica se la risposta è True
    if answer['corretta']:
        context.bot.send_message(chat_id=query.message.chat_id, text="Hai risposto correttamente!")
    else:
        context.bot.send_message(chat_id=query.message.chat_id, text="Spiacente, la risposta è errata.")
    domanda_corrente += 1
    context.user_data['domanda_corrente'] = domanda_corrente

    if domanda_corrente < len(data):
        domanda(update, context)
    else:
        context.bot.send_message(chat_id=query.message.chat_id, text="Hai terminato il quiz!")
