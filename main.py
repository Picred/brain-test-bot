from telegram import BotCommand
from telegram.ext import(
	Updater,
	MessageHandler,
	CommandHandler,
	Filters
)
import logging
from modules.handlers.start import start

TOKEN = open("token.txt", "r").read().strip()

# Aggiunge l'anteprima dei comandi con la relativa descrizione
def add_commands(up: Updater) -> None:
    commands = [
	BotCommand("start", "Messaggio di benvenuto") ]
    up.bot.set_my_commands(commands=commands)


# Funzione main del programma per l'avvio del bot
def main():
	logging.basicConfig(format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", level = logging.INFO)
	# logger = logging.getLogger(__name__) #Non usato
	logging.info('Starting bot...') 
	
	updater = Updater(TOKEN, use_context=True)

	dp = updater.dispatcher
	
    # Command handlers
	dp.add_handler(CommandHandler('start', start))
	
    # Message handlers

	add_commands(updater)
	
    # Logging
	updater.start_polling()
	updater.idle() #ctrl+c

if __name__ == "__main__":
	main()
