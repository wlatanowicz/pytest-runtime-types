import pytest

import pytest_runtime_types


def function(a: int, b: str) -> str:
    return f"{a} {b}"


@pytest.mark.runtime_types
def test_call_global_function():
    result = function(123, "abc")
    assert result == "123 abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_call_global_function():
    result = function(123, 456)
    assert result == "123 456"
