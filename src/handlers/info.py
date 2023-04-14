from telegram import Update
from telegram.ext import CallbackContext

def info(update: Update, context: CallbackContext) -> None:

    username = str(update.message.chat.username)

    categoria = "Nessuna"
    livello = "Nessuna"

    if ('livello' in context.user_data):
        livello = context.user_data['livello']
    
    if ('categoria' in context.user_data):
        categoria = context.user_data['categoria']

    context.bot.sendMessage(chat_id=update.message.chat_id,text="Username: " + username + 
                                                                "\nCategoria: " + categoria +
                                                                "\nDifficoltà: " + livello + 
                                                                "Per modificare categoria e difficoltà usare rispettivamente i comandi /categoria e /difficolta")
