from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

def categoria_selezionata(update: Update, context: CallbackContext) -> None:
    categoria = update.message.text
    if'categoria' not in context.user_data:
        context.user_data['categoria'] = categoria
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Hai selezionato la categoria {categoria}.", reply_markup=ReplyKeyboardRemove())
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"La categoria {context.user_data['categoria']} è già stata selezionata.", reply_markup=ReplyKeyboardRemove())
        context.bot.sendMessage(chat_id=update.message.chat_id,text="Per cambiare la categoria utilizzare /categoria")
