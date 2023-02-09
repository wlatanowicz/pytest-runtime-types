import pytest

import pytest_runtime_types


def function_factory():
    def inner_function(a: int, b: str) -> str:
        return f"{a} {b}"

    return inner_function


@pytest.mark.runtime_types
def test_returned_function():
    result = function_factory()(123, "abc")
    assert result == "123 abc"


@pytest.mark.skip("Returned anonymous functions are not supported.")
@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_function_untyped_decorator():
    result = function_factory()(123, 456)
    assert result == "123 456"
