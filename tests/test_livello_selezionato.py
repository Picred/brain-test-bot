from telegram import ReplyKeyboardRemove
from pytest_mock import MockerFixture
from src.handlers.livello_selezionato import livello_selezionato

def test_categoria_selezionata(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    update.message.text = '1: Facile'
    livello = update.message.text
    livello_selezionato(update, context)
    context.bot.sendMessage.assert_called_with(chat_id=update.message.chat_id,text=f"Hai selezionato il livello {livello}.", reply_markup=ReplyKeyboardRemove())
    assert context.user_data['livello'] == '1: Facile'

    # difficoltà (o livello) già selezionata
    update.message.text = '2: Intermedio'
    livello_selezionato(update, context)
    context.bot.sendMessage.assert_called_with(chat_id=update.message.chat_id,text=f"Il livello {context.user_data['livello']} è già stato selezionato.\n Per cambiare la difficolta utilizzare /difficolta", reply_markup=ReplyKeyboardRemove())
    assert context.user_data['livello'] == '1: Facile'
