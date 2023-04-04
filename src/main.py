from telegram.ext import (Updater, MessageHandler, CommandHandler, Filters)
import logging

from handlers.start import start
from handlers.difficolta import difficolta
from handlers.categoria import categoria
from handlers.add_commands import add_commands
from handlers.livello_selezionato import livello_selezionato
from handlers.categoria_selezionata import categoria_selezionata

TOKEN = open("token.txt", "r", encoding="utf-8").read().strip()

# Funzione main del programma per l'avvio del bot


def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    # logger = logging.getLogger(__name__) #Non usato
    logging.info('Starting bot...')

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

# Command handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('difficolta', difficolta))
    dp.add_handler(CommandHandler('categoria', categoria))

# Message handlers
    dp.add_handler(MessageHandler(Filters.text, categoria_selezionata))
    dp.add_handler(MessageHandler(Filters.text, livello_selezionato))
    

    add_commands(updater)

# Logging
    updater.start_polling()
    updater.idle()  # ctrl+c


if __name__ == "__main__":
    main()
