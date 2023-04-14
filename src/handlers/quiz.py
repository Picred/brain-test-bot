from telegram import Update
from telegram.ext import CallbackContext
from domanda import domanda

def quiz(update: Update, context: CallbackContext):
    if 'domanda_corrente' in context.user_data:
        del context.user_data['domanda_corrente']
    context.user_data['domanda_corrente'] = 0
    context.bot.send_message(chat_id=update.effective_chat.id,text="Iniziamo con la prima domanda:")
    domanda(update, context)
