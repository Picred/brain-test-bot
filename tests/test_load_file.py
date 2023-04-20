from pytest_mock import MockerFixture
import json
from src.data.costanti import CATEGORIA, LIVELLO
from src.handlers.domanda import load_file


def test_load_file(mocker: MockerFixture) -> None:
    context=mocker.Mock()
    context.user_data= {LIVELLO : '1: Facile', CATEGORIA : 'Logica'}

    load_file(context)
    with open('src/data/intermedio.json', 'r', encoding="utf-8") as f:
        mock_load = mocker.patch('json.load')
    json.load(f)
    mock_load.assert_called_once_with(f)


def test1_load_file(mocker: MockerFixture) -> None:
    context=mocker.Mock()
    context.user_data= {LIVELLO : '2: Intermedio', CATEGORIA : 'Logica'}

    load_file(context)
    
    with open('src/data/difficile.json', 'r', encoding="utf-8") as f:
        mock_load = mocker.patch('json.load')
    json.load(f)
    
    mock_load.assert_called_once_with(f)


def test2_load_file(mocker: MockerFixture) -> None:
    context=mocker.Mock()
    context.user_data= {LIVELLO : '3: Difficile', CATEGORIA : 'Logica'}

    load_file(context)

    with open('src/data/facile.json', 'r', encoding="utf-8") as f:
        mock_load = mocker.patch('json.load')
    json.load(f)
    mock_load.assert_called_once_with(f)
