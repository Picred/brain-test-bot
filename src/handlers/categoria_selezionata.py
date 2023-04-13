from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
import json

with open("src/data/categorie.json", "r") as f:
   categorie=json.load(f)


def categoria_selezionata(update: Update, context: CallbackContext) -> None:
    categoria = update.message.text

    # Verifico se l'input è coerente con le categorie disponibile
    if(categoria not in categorie):
        context.bot.sendMessage(chat_id=update.message.chat_id,text="La categoria inserita non è valida. Utilizzare le categorie disponibili in /categoria", reply_markup=ReplyKeyboardRemove())
        return

    if('categoria' not in context.user_data):
        context.user_data['categoria'] = categoria
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Hai selezionato la categoria {categoria}.", reply_markup=ReplyKeyboardRemove())
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"La categoria {context.user_data['categoria']} è già stata selezionata.", reply_markup=ReplyKeyboardRemove())
        context.bot.sendMessage(chat_id=update.message.chat_id,text="Per cambiare la categoria utilizzare /categoria")
