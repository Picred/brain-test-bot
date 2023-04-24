from pytest_mock import MockerFixture
from src.handlers.genera_commento import genera_commento
from src.data.costanti import PUNTEGGIO, CATEGORIA, ESEMPIO_COMMENTO as data
from unittest.mock import mock_open, patch
from telegram.ext import CallbackContext
from telegram import Update
import json


def test_genera_commento(mocker: MockerFixture):
    update = mocker.Mock(Update)
    update.effective_chat.id = 12345
    context = mocker.Mock(CallbackContext)
    context.user_data = {PUNTEGGIO: 0, CATEGORIA: 'Logica'}
    m = mock_open(read_data=json.dumps(data))

    with patch('builtins.open', m):
        genera_commento(update, context)

    context.bot.sendMessage.assert_called_with(chat_id=12345, text="commento1")


def test2_genera_commento(mocker: MockerFixture):
    update = mocker.Mock(Update)
    update.effective_chat.id = 12345
    context = mocker.Mock(CallbackContext)
    context.user_data = {PUNTEGGIO: 5, CATEGORIA: 'Logica'}
    m = mock_open(read_data=json.dumps(data))

    with patch('builtins.open', m):
        genera_commento(update, context)

    context.bot.sendMessage.assert_called_with(chat_id=12345, text="commento3")


def test3_genera_commento(mocker: MockerFixture):
    update = mocker.Mock(Update)
    update.effective_chat.id = 12345
    context = mocker.Mock(CallbackContext)
    context.user_data = {PUNTEGGIO: 3, CATEGORIA: 'Logica'}

    m = mock_open(read_data=json.dumps(data))

    with patch('builtins.open', m):
        genera_commento(update, context)

    context.bot.sendMessage.assert_called_with(chat_id=12345, text="commento2")
