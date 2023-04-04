from telegram import Update
from telegram.ext import CallbackContext

livelli = ["1: Facile", "2: Intermedio", "3: Difficile"]

# Salva il livello selezionato nei dati di User, in context.user_data['livello']
def livello_selezionato(update: Update, context: CallbackContext) -> None:
    livello = update.message.text

    if(livello in livelli):
        # Salva il livello scelto in input
        context.user_data['livello'] = livello

        # Messaggio di conferma
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Hai selezionato il livello {livello}.")
    else:
        pass
