from src.handlers.domanda import load_file
from pytest_mock import MockerFixture
import json

def test_load_file(mocker: MockerFixture) -> None:
    context=mocker.Mock()
    context.user_data= {'livello' : '1: Facile', 'categoria' : 'Logica'}

    load_file(context)
    f = open('src/data/intermedio.json', 'r', encoding="utf-8")
    mock_load = mocker.patch('json.load')
    json.load(f)
    mock_load.assert_called_once_with(f)

def test1_load_file(mocker: MockerFixture) -> None:
    context=mocker.Mock()
    context.user_data= {'livello' : '2: Intermedio', 'categoria' : 'Logica'}

    load_file(context)
    f = open('src/data/difficile.json', 'r', encoding="utf-8")
    mock_load = mocker.patch('json.load')
    json.load(f)
    mock_load.assert_called_once_with(f)

def test2_load_file(mocker: MockerFixture) -> None:
    context=mocker.Mock()
    context.user_data= {'livello' : '3: Difficile', 'categoria' : 'Logica'}

    load_file(context)
    f = open('src/data/facile.json', 'r', encoding="utf-8")
    mock_load = mocker.patch('json.load')
    json.load(f)
    mock_load.assert_called_once_with(f)
