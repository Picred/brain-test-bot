from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from src.data.costanti import LIVELLO

def livello_selezionato(update: Update, context: CallbackContext) -> None:
    livello = update.message.text

    if LIVELLO not in context.user_data:
        context.user_data[LIVELLO] = livello
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Hai selezionato il livello {livello}.", reply_markup=ReplyKeyboardRemove())
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Il livello {context.user_data[LIVELLO]} è già stato selezionato.\n Per cambiare la difficolta utilizzare /difficolta", reply_markup=ReplyKeyboardRemove())
