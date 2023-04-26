from unittest.mock import patch
from pytest_mock import MockerFixture
import main

def test_init(mocker: MockerFixture) -> None:
    mocker.patch.object(main, "__name__", "__main__")

    with patch("main.main") as mocked_main:
        main.init()

        mocked_main.assert_called_once()

def test1_init(mocker: MockerFixture) -> None:
    mocker.patch.object(main, "__name__", "")

    with patch("main.main") as mocked_main:
        main.init()

        assert mocked_main.call_count == 0
