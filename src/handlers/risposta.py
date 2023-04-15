from telegram import Update
from telegram.ext import CallbackContext
from .domanda import domanda, load_file
import json


def risposta(update: Update, context: CallbackContext) -> None:
    data = load_file(context)
    domanda_corrente = context.user_data['domanda_corrente']
    query = update.callback_query
    question_index, answer_index = map(int, query.data.split(':'))
    question = data[question_index]
    answer = question['risposte'][answer_index]

    # Rimuove la tastiera con le risposte
    context.bot.editMessageReplyMarkup(chat_id=query.message.chat_id, message_id=query.message.message_id)
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
