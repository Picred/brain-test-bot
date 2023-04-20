from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import LIVELLO, CATEGORIA

def info(update: Update, context: CallbackContext) -> None:
    username = str(update.message.chat.username)
    if username == str(None):
        username = "Non impostato"

    categoria = "Da selezionare"
    livello = "Da selezionare"

    if LIVELLO in context.user_data:
        livello = context.user_data[LIVELLO]
    if CATEGORIA in context.user_data:
        categoria = context.user_data[CATEGORIA]

    context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Username: {username} \nCategoria: {categoria}\nDifficoltà: {livello}")
