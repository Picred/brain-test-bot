"""/info command"""
from telegram import Update
from telegram.ext import CallbackContext
from src.data.costanti import LIVELLO, CATEGORIA


def info(update: Update, context: CallbackContext) -> None:
    """Shows the main infos of the user.

    Args:
        update: update event
        context: context passed by the handler
    """
    username = str(update.message.chat.username)
    if username == str(None):
        username = "Non impostato"

    categoria = livello = "Da selezionare"
    livello = context.user_data.get(LIVELLO, livello)
    categoria = context.user_data.get(CATEGORIA, categoria)

    context.bot.sendMessage(chat_id=update.message.chat_id,text=f"Username: {username} \nCategoria: {categoria}\nDifficoltà: {livello}")
