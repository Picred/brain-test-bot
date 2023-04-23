from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import DOMANDA_CORRENTE, PUNTEGGIO, CATEGORIA
from .domanda import domanda 
from src.handlers.load_file import load_file
import json

def risposta_vuota(update: Update, context: CallbackContext,rm_id: int) -> None:
    update.callback_query=None
    data = load_file(context)
    chat_id=update.effective_chat.id

    context.bot.sendMessage(chat_id=chat_id,text="Tempo scaduto!")
    context.bot.editMessageReplyMarkup(chat_id=chat_id, message_id=rm_id)

    prossima_domanda(update,context,data)
    
    


def risposta(update: Update, context: CallbackContext) -> None:
    data = load_file(context)
    chat_id=update.effective_chat.id
    query = update.callback_query

    for j in context.job_queue.jobs():
        j.remove()

    question_index, answer_index = map(int, query.data.split(':'))
    question = data[question_index]
    answer = question['risposte'][answer_index]

    # Rimuove la tastiera con le risposte
    context.bot.editMessageReplyMarkup(chat_id=chat_id, message_id=query.message.message_id)

    if answer['corretta']:
        esito = "Hai risposto correttamente!"
        context.user_data[PUNTEGGIO] += 1 
    else:
        esito = "Spiacente, la risposta è errata."
        # Trovo la risposta corretta
        risposte_domanda = data[question_index]['risposte']
        indice_risposta_corretta = next(i for i, r in enumerate(risposte_domanda) if r['corretta'] == True)
        risposta_corretta = risposte_domanda[indice_risposta_corretta]['testo_risposta']
        context.bot.sendMessage(chat_id=chat_id, text=f"La risposta corretta era \"{risposta_corretta}\"")

    context.bot.send_message(chat_id=chat_id, text=esito)


    prossima_domanda(update,context,data)



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



def prossima_domanda(update:Update, context:CallbackContext,data: dict) -> None:
    context.user_data[DOMANDA_CORRENTE] += 1
    if context.user_data[DOMANDA_CORRENTE] < len(data):
        domanda(update, context)
    else:
        punteggio = context.user_data[PUNTEGGIO]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hai terminato il quiz!\nHai totalizzato {punteggio}/{len(data)} punti!")
        genera_commento(update, context)

