from telegram import Update
from telegram.ext import CallbackContext

start_txt = "Benvenuto al Brain Test Quiz! Puoi metterti alla prova scegliendo una /categoria e una /difficolta\nPuoi vedere le tue informazioni con /info e, dopo aver completato le operazioni preliminari, puoi iniziare il /quiz."

def start(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(chat_id=update.message.chat_id, text=start_txt)
