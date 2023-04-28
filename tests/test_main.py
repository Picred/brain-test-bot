"""Test of the main function"""
from unittest.mock import patch
from main import main


@patch('main.Updater')
def test_main(mock_updater) -> None:
    """Tests the main function.

    Args:
        mocker_updater: mocker used to assert events
    """
    main()

    assert mock_updater.return_value.dispatcher.add_handler.called
    assert mock_updater.return_value.idle.called
