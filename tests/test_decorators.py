import os
import tempfile
from typing import Any

from _pytest.capture import CaptureFixture

from src.decorators import log, my_function


def test_log_1() -> None:
    assert my_function(1, 2) == 3


def test_log_2() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
    try:

        @log(filename=temp_filename)
        def test_func(x: Any, y: Any) -> Any:
            return x + y

        test_func(1, 2)
        with open(temp_filename, "r") as f:
            log_content = f.read()
        assert "test_func ok" in log_content
    finally:
        os.remove(temp_filename)


def test_log_3(capsys: CaptureFixture[str]) -> None:
    @log()
    def test_func(a: Any, b: Any) -> Any:

        raise ValueError("test error")

    try:
        test_func(1, 2)
    except ValueError:
        pass

    captured = capsys.readouterr()
    assert "test_func error: ValueError. Inputs: (1, 2), {}\n" in captured.out
