from pytest_mock import MockerFixture
from src.handlers.categoria import categoria

def test_categoria(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    categoria(update,context)

    assert 'categoria' not in context.user_data


def test2_categoria(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {'categoria' : 'Logica'}

    categoria(update,context)

    assert 'categoria' not in context.user_data
