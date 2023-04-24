from telegram import ReplyKeyboardRemove
from pytest_mock import MockerFixture
from src.handlers.categoria_selezionata import categoria_selezionata
from src.data.costanti import CATEGORIA


def test_categoria_selezionata(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    update.message.text = 'Logica'
    categoria = update.message.text
    categoria_selezionata(update, context)
    
    assert context.bot.sendMessage.call_args[1]['chat_id'] == update.message.chat_id
    assert context.bot.sendMessage.call_args[1]['text'] == f"Hai selezionato la categoria {categoria}."
    assert isinstance(context.bot.sendMessage.call_args[1]['reply_markup'], ReplyKeyboardRemove)

    # categoria già selezionata
    update.message.text = 'Grammatica'
    categoria_selezionata(update, context)
    
    assert context.bot.sendMessage.call_args[1]['chat_id'] == update.message.chat_id
    assert context.bot.sendMessage.call_args[1]['text'] == f"La categoria {context.user_data[CATEGORIA]} è già stata selezionata. \nPer cambiare la categoria utilizzare /categoria"
    assert isinstance(context.bot.sendMessage.call_args[1]['reply_markup'], ReplyKeyboardRemove)