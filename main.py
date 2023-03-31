from telegram.ext import(Updater, MessageHandler, CommandHandler, Filters)
import logging

from src.handlers.start import start
from src.handlers.difficolta import difficolta
from src.handlers.add_commands import add_commands
from src.handlers.livello_selezionato import livello_selezionato

TOKEN = open("token.txt", "r").read().strip()

# Funzione main del programma per l'avvio del bot
def main():
	logging.basicConfig(format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", level = logging.INFO)
	# logger = logging.getLogger(__name__) #Non usato
	logging.info('Starting bot...') 
	
	updater = Updater(TOKEN, use_context=True)

	dp = updater.dispatcher
	
    # Command handlers
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('difficolta', difficolta))
	
    # Message handlers
	dp.add_handler(MessageHandler(Filters.text, livello_selezionato))


	add_commands(updater)
	
    # Logging
	updater.start_polling()
	updater.idle() #ctrl+c

if __name__ == "__main__":
	main()
