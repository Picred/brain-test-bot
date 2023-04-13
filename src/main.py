from telegram.ext import (Updater, MessageHandler, CommandHandler, Filters)
import logging
import json

from src.handlers.start import start
from src.handlers.categoria import categoria
from src.handlers.difficolta import difficolta
from src.handlers.add_commands import add_commands
from src.handlers.livello_selezionato import livello_selezionato
from src.handlers.categoria_selezionata import categoria_selezionata



with open("token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

with open('src/data/livelli.json', 'r') as f:
    livelli = list(json.load(f))

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
    dp.add_handler(MessageHandler(Filters.text & Filters.regex(f"({'|'.join(livelli)})"), livello_selezionato))
    dp.add_handler(MessageHandler(Filters.text, categoria_selezionata))

    add_commands(updater)

# Logging
    updater.start_polling()
    updater.idle()  # ctrl+c


if __name__ == "__main__":
    main()
