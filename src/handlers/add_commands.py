from telegram import BotCommand
from telegram.ext import Updater

def add_commands(up: Updater) -> None:
    commands = [
        BotCommand("start", "Messaggio di benvenuto"),
        BotCommand("difficolta", "Imposta la difficolta"),
        BotCommand("categoria", "Imposta la categoria"),
        BotCommand("quiz", "Inizia il quiz")
    ]
    up.bot.set_my_commands(commands=commands)
