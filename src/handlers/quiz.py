from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import PUNTEGGIO, DOMANDA_CORRENTE
from src.handlers.domanda import domanda


def quiz(update: Update, context: CallbackContext) -> None:
    if DOMANDA_CORRENTE in context.user_data:
        del context.user_data[DOMANDA_CORRENTE]

    context.user_data[PUNTEGGIO] = 0
    context.user_data[DOMANDA_CORRENTE] = 0
    context.bot.send_message(chat_id=update.effective_chat.id,text="Iniziamo con la prima domanda:")
    domanda(update, context)
