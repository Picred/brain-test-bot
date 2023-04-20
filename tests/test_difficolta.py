from pytest_mock import MockerFixture
from src.handlers.difficolta import difficolta

def test_difficolta(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    difficolta(update,context)

    assert 'livello' not in context.user_data


def test2_difficolta(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'livello' : '2: Intermedio'}

    difficolta(update,context)

    assert 'livello' not in context.user_data
