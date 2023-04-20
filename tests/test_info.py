from pytest_mock import MockerFixture
from src.handlers.info import info
from telegram import Update, Message, Chat
from telegram.ext import CallbackContext


def test_info(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'categoria':None, 'livello':None}
    
    info(update,context)

    assert context.user_data['livello'] == None
    assert context.user_data['categoria'] == None


def test2_info(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'categoria':'Logica', 'livello':None}
    
    info(update,context)

    assert context.user_data['livello'] == None
    assert context.user_data['categoria'] == 'Logica'


def test3_info(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'categoria':'Logica', 'livello':'1: Facile'}
    
    info(update,context)

    assert context.user_data['livello'] == '1: Facile'
    assert context.user_data['categoria'] == 'Logica'


def test4_info(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'categoria': None, 'livello': '2: Intermedio'}
    
    info(update,context)

    assert context.user_data['livello'] == '2: Intermedio'
    assert context.user_data['categoria'] == None


def test5_info(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'categoria':'Logica', 'livello':'1: Facile'}
    update.message.chat.username = None

    info(update,context)
    categoria = context.user_data['categoria']
    livello = context.user_data['livello']

    context.bot.sendMessage.assert_called_once_with(chat_id=update.message.chat_id, text=f"Username: Non impostato \nCategoria: {categoria}\nDifficoltà: {livello}")
