from pytest_mock import MockerFixture
from src.handlers.info import info
from src.data.costanti import LIVELLO, CATEGORIA


def test_info(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {CATEGORIA:None, LIVELLO:None}

    info(update,context)

    assert context.user_data[LIVELLO] is None
    assert context.user_data[CATEGORIA] is None


def test2_info(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {CATEGORIA:'Logica', LIVELLO:None}

    info(update,context)

    assert context.user_data[LIVELLO] is None
    assert context.user_data[CATEGORIA] == 'Logica'


def test3_info(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {CATEGORIA:'Logica', LIVELLO:'1: Facile'}

    info(update,context)

    assert context.user_data[LIVELLO] == '1: Facile'
    assert context.user_data[CATEGORIA] == 'Logica'


def test4_info(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {CATEGORIA: None, LIVELLO: '2: Intermedio'}

    info(update,context)

    assert context.user_data[LIVELLO] == '2: Intermedio'
    assert context.user_data[CATEGORIA] is None


def test5_info(mocker: MockerFixture) -> None:
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {CATEGORIA:'Logica', LIVELLO:'1: Facile'}
    update.message.chat.username = None

    info(update,context)
    categoria = context.user_data[CATEGORIA]
    livello = context.user_data[LIVELLO]

    context.bot.sendMessage.assert_called_once_with(chat_id=update.message.chat_id, text=f"Username: Non impostato \nCategoria: {categoria}\nDifficoltà: {livello}")
