from pytest_mock import MockerFixture
from src.handlers.quiz import quiz

def test_quiz(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    context=mocker.Mock()
    context.user_data={'livello' : '1: Facile', 'categoria' : 'Logica'}

    quiz(update, context)

    assert context.user_data['domanda_corrente'] == 0
    assert context.user_data['punteggio'] == 0



def test2_quiz(mocker: MockerFixture) -> None:
    update=mocker.Mock()
    context=mocker.Mock()
    context.user_data={'livello' : '1: Facile', 'categoria' : 'Logica', 'domanda_corrente' : mocker.Mock()}

    quiz(update, context)

    assert context.user_data['domanda_corrente'] == 0
    assert context.user_data['punteggio'] == 0

