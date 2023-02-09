import pytest

import pytest_runtime_types


@pytest.mark.runtime_types
def test_call_local_function():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(123, "abc")
    assert result == "123 abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_call_local_function():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(123, 456)
    assert result == "123 456"
