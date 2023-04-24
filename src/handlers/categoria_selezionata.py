from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from src.data.costanti import CATEGORIA


def categoria_selezionata(update: Update, context: CallbackContext) -> None:
    categoria = update.message.text
    if CATEGORIA not in context.user_data:
        context.user_data[CATEGORIA] = categoria
        testo= f"Hai selezionato la categoria {categoria}."
    else:
        testo = f"La categoria {context.user_data[CATEGORIA]} è già stata selezionata. \nPer cambiare la categoria utilizzare /categoria"

    context.bot.sendMessage(chat_id=update.message.chat_id, text=testo, reply_markup=ReplyKeyboardRemove())
