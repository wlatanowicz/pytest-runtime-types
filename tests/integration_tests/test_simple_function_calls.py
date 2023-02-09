import pytest

import pytest_runtime_types


@pytest.mark.runtime_types
def test_function_str_int():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(123, "abc")
    assert result == "123 abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_function_str_int():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(123, 456)
    assert result == "123 456"


@pytest.mark.runtime_types
def test_function_str_int_kwargs():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(a=123, b="abc")
    assert result == "123 abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_function_str_int_kwargs():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(a=123, b=456)
    assert result == "123 456"


@pytest.mark.runtime_types
def test_function_str_int_args_and_kwargs():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(123, b="abc")
    assert result == "123 abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_function_str_int_args_and_kwargs():
    def function(a: int, b: str) -> str:
        return f"{a} {b}"

    result = function(123, b=456)
    assert result == "123 456"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_return_type():
    def function(a: int, b: str) -> str:
        return a

    result = function(123, "567")
    assert result == 123


@pytest.mark.runtime_types
def test_no_annotations():
    def function(a, b):
        return f"{a} {b}"

    result = function(123, 456)
    assert result == "123 456"
