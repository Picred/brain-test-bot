"""Add commands handler"""
from telegram import BotCommand
from telegram.ext import Updater


def add_commands(up: Updater) -> None:
    """Adds the list of commands with their description to the bot

    Args:
        up (Updater): supplyed Updater
    """
    commands = [
        BotCommand("start", "Messaggio di benvenuto"),
        BotCommand("difficolta", "Imposta la difficolta"),
        BotCommand("categoria", "Imposta la categoria"),
        BotCommand("info", "Mostra categoria e difficoltà selezionate"),
        BotCommand("quiz", "Inizia il quiz")
    ]
    up.bot.set_my_commands(commands=commands)
