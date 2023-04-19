from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

def livello_selezionato(update: Update, context: CallbackContext) -> None:
    livello = update.message.text

    if 'livello' not in context.user_data:
        context.user_data['livello'] = livello
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Hai selezionato il livello {livello}.", reply_markup=ReplyKeyboardRemove())
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Il livello {context.user_data['livello']} è già stato selezionato.\n Per cambiare la difficolta utilizzare /difficolta", reply_markup=ReplyKeyboardRemove())
