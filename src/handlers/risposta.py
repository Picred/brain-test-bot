from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import PUNTEGGIO
from src.handlers.load_file import load_file
from src.handlers.domanda import prossima_domanda


def risposta(update: Update, context: CallbackContext) -> None:
    data = load_file(context)
    chat_id=update.effective_chat.id
    query = update.callback_query

    for j in context.job_queue.jobs():
        j.remove()

    question_index, answer_index = map(int, query.data.split(':'))
    question = data[question_index]
    answer = question['risposte'][answer_index]

    context.bot.editMessageReplyMarkup(chat_id=chat_id, message_id=query.message.message_id)

    if answer['corretta']:
        esito = "Hai risposto correttamente!"
        context.user_data[PUNTEGGIO] += 1
    else:
        esito = "Spiacente, la risposta è errata."
        # Trovo la risposta corretta
        risposte_domanda = data[question_index]['risposte']
        indice_risposta_corretta = next(i for i, r in enumerate(risposte_domanda) if r['corretta'] is True)
        risposta_corretta = risposte_domanda[indice_risposta_corretta]['testo_risposta']
        context.bot.sendMessage(chat_id=chat_id, text=f"La risposta corretta era \"{risposta_corretta}\"")

    context.bot.send_message(chat_id=chat_id, text=esito)

    prossima_domanda(update,context,data)
