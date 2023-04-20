from telegram import BotCommand
from telegram.ext import Updater
from pytest_mock import MockerFixture
from src.handlers.add_commands import add_commands

expected_commands = [
        BotCommand("start", "Messaggio di benvenuto"),
        BotCommand("difficolta", "Imposta la difficolta"),
        BotCommand("categoria", "Imposta la categoria"),
        BotCommand("info", "Mostra categoria e difficoltà selezionate"),
        BotCommand("quiz", "Inizia il quiz")
    ]

def test_add_commands(mocker: MockerFixture):
    updater = mocker.Mock(Updater)

    add_commands(updater)

    updater.bot.set_my_commands.assert_called_once_with(commands=expected_commands)
