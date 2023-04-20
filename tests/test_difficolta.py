from pytest_mock import MockerFixture
from src.handlers.difficolta import difficolta
from src.data.costanti import LIVELLO

def test_difficolta(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    difficolta(update,context)

    assert LIVELLO not in context.user_data


def test2_difficolta(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {LIVELLO : '2: Intermedio'}

    difficolta(update,context)

    assert LIVELLO not in context.user_data
