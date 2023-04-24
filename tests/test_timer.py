from pytest_mock import MockerFixture
from telegram.ext import CallbackContext
from src.handlers.timer import timer
from unittest.mock import patch


def test_timer(mocker: MockerFixture):     
    context = mocker.Mock(spec=CallbackContext)
    context.job.context = ['arg1', 'arg2', 'arg3']
    
    with patch('src.handlers.risposta.risposta_vuota') as mocked_risposta_vuota:
        timer(context)        

    mocked_risposta_vuota.assert_called_with('arg1', 'arg2', 'arg3')
