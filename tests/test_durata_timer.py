"""Test of the durata_timer function"""
from pytest_mock import MockerFixture
from src.data.costanti import LIVELLO
from src.handlers.durata_timer import durata_timer


def test_durata_timer(mocker: MockerFixture) -> None:
    """Tests the durata_timer function.

    Args:
        mocker: mocker used to simulate events
    """
    context = mocker.Mock()
    context.user_data = {LIVELLO: '1: Facile'}

    res = durata_timer(context)

    assert res == 10


def test2_durata_timer(mocker: MockerFixture) -> None:
    """Tests the durata_timer function.

    Args:
        mocker: mocker used to simulate events
    """
    context = mocker.Mock()
    context.user_data = {LIVELLO: '2: Intermedio'}

    res = durata_timer(context)

    assert res == 7


def test3_durata_timer(mocker: MockerFixture) -> None:
    """Tests the durata_timer function.

    Args:
        mocker: mocker used to simulate events
    """
    context = mocker.Mock()
    context.user_data = {LIVELLO: '3: Difficile'}

    res = durata_timer(context)

    assert res == 5
