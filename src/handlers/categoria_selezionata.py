from telegram import Update
from telegram.ext import CallbackContext
import json

with open("src/data/categorie.json", "r") as f:
   categorie=json.load(f)


# Salva la categoria selezionato nei dati di User, in context.user_data['categoria']
def categoria_selezionata(update: Update, context: CallbackContext) -> None:
    categoria = update.message.text

    if(categoria in categorie):
        # Salva il categoria scelto in input
        context.user_data['categoria'] = categoria

        # Messaggio di conferma
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Hai selezionato la categoria {categoria}.")
    else:
        pass
