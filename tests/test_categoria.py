from pytest_mock import MockerFixture
from src.handlers.categoria import categoria
from src.data.costanti import CATEGORIA

def test_categoria(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {}

    categoria(update,context)

    assert CATEGORIA not in context.user_data


def test2_categoria(mocker: MockerFixture):
    update = mocker.Mock()
    context = mocker.Mock()
    context.user_data = {CATEGORIA : 'Logica'}

    categoria(update,context)

    assert CATEGORIA not in context.user_data
