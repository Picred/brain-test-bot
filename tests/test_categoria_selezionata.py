from telegram import ReplyKeyboardRemove
from pytest_mock import MockerFixture
from src.handlers.categoria_selezionata import categoria_selezionata

def test_categoria_selezionata(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    update.message.text = 'Logica'
    categoria = update.message.text
    categoria_selezionata(update, context)
    context.bot.sendMessage.assert_called_with(chat_id=update.message.chat_id,text=f"Hai selezionato la categoria {categoria}.", reply_markup=ReplyKeyboardRemove())

    # categoria già selezionata
    update.message.text = 'Grammatica'
    categoria_selezionata(update, context)
    context.bot.sendMessage.assert_called_with(chat_id=update.message.chat_id,text=f"La categoria {context.user_data['categoria']} è già stata selezionata. \nPer cambiare la categoria utilizzare /categoria", reply_markup=ReplyKeyboardRemove())
