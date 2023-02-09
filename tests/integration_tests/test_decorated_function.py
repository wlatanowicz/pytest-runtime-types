from functools import wraps

import pytest

import pytest_runtime_types


def untyped_func_decorator(fn):
    @wraps(fn)
    def untyped_inner_func(*args, **kwargs):
        return fn(*args, **kwargs)

    return untyped_inner_func


def typed_func_decorator(fn):
    @wraps(fn)
    def typed_inner_func(a: int, b: str):
        return fn(a, b)

    return typed_inner_func


@untyped_func_decorator
def function(a: int, b: str) -> str:
    return f"{a} {b}"


@typed_func_decorator
def function_typed_decorator(a, b) -> str:
    return f"{a} {b}"


@pytest.mark.runtime_types
def test_function_untyped_decorator():
    result = function(123, "abc")
    assert result == "123 abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_function_untyped_decorator():
    result = function(123, 456)
    assert result == "123 456"


@pytest.mark.runtime_types
def test_function_typed_decorator():
    result = function_typed_decorator(123, "abc")
    assert result == "123 abc"


@pytest.mark.skip("Inner functions in decorators are not supported.")
@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_function_typed_decorator():
    result = function_typed_decorator(123, 456)
    assert result == "123 456"
