from pytest_mock import MockerFixture
from src.handlers.quiz import quiz
from src.data.costanti import LIVELLO, CATEGORIA, PUNTEGGIO, DOMANDA_CORRENTE


def test_quiz(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    context=mocker.Mock()
    context.user_data={LIVELLO : '1: Facile', CATEGORIA : 'Logica'}

    quiz(update, context)

    assert context.user_data[DOMANDA_CORRENTE] == 0
    assert context.user_data[PUNTEGGIO] == 0


def test2_quiz(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    context=mocker.Mock()
    context.user_data={LIVELLO : '1: Facile', CATEGORIA : 'Logica', DOMANDA_CORRENTE : mocker.Mock()}

    quiz(update, context)

    assert context.user_data[DOMANDA_CORRENTE] == 0
    assert context.user_data[PUNTEGGIO] == 0
