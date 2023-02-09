import typing

import pytest

import pytest_runtime_types


@pytest.mark.runtime_types
def test_generator():
    def function() -> typing.Generator[int, None, None]:
        yield 123
        yield 456

    assert list(function()) == [123, 456]


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_type_generator():
    def function() -> typing.Generator[str, None, None]:
        yield 123
        yield 456

    assert list(function()) == [123, 456]


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_regular_function_annotated_as_generator():
    def function() -> typing.Generator[str, None, None]:
        return 123, 456

    assert list(function()) == [123, 456]


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_generator_annotated_as_regular_function_iterable():
    def function() -> typing.Tuple[int, int]:
        yield 123
        yield 456

    assert list(function()) == [123, 456]


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_generator_annotated_as_regular_function_simple():
    def function() -> typing.Optional[int]:
        yield 123
        yield 456

    assert list(function()) == [123, 456]
