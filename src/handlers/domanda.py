"""Quiz functions"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from src.data.costanti import DOMANDA_CORRENTE, PUNTEGGIO
from src.handlers.durata_timer import durata_timer
from src.handlers.load_file import load_file
from src.handlers.genera_commento import genera_commento


def domanda(update: Update, context: CallbackContext) -> None:
    """Replies to the user with a keyboard that contains the question and all of possible answers and starts the timer.

    Args:
        update: update event
        context: context passed by the handler
    """
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
    rm_message = context.bot.send_message(chat_id=update.effective_chat.id, text=testo, reply_markup=reply_markup)
    durata = durata_timer(context)
    context.job_queue.run_once(timer,durata,context=(update,rm_message.message_id, context))


def prossima_domanda(update:Update, context:CallbackContext,data: dict) -> None:
    """Generates the following questions with the respective answers.

    Args:
        update: update event
        context: context passed by the handler
        data: file that contains all questions/answers
    """
    context.user_data[DOMANDA_CORRENTE] += 1
    if context.user_data[DOMANDA_CORRENTE] < len(data):
        domanda(update, context)
    else:
        punteggio = context.user_data[PUNTEGGIO]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hai terminato il quiz!\nHai totalizzato {punteggio}/{len(data)} punti!")
        genera_commento(update, context)


def timer(call_context: CallbackContext) -> None:
    """Sends a message when the timer is expired.
    
    Args:
        update: update event
        context: context passed by the handler
    """
    args = call_context.job.context
    update = args[0]
    rm_id = args[1]
    context = args[2]

    update.callback_query=None
    data = load_file(context)
    chat_id=update.effective_chat.id

    context.bot.sendMessage(chat_id=chat_id,text="Tempo scaduto!")
    context.bot.editMessageReplyMarkup(chat_id=chat_id, message_id=rm_id)

    prossima_domanda(update,context,data)
