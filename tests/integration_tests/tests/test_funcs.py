import pytest
from tested_code.some_funcs import (
    fifth_function,
    first_function,
    fourth_function,
    second_function,
    seventh_function,
    sixth_function,
    third_function,
)

import pytest_runtime_types


@pytest.mark.runtime_types
def test_fist_function():
    result = first_function()
    assert result == "4 5"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_second_function():
    result = second_function()
    assert result == "3 123"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_third_function():
    result = third_function()
    assert result == "3 123"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fourth_function():
    result = fourth_function()
    assert result is None


@pytest.mark.runtime_types
def test_fifth_function():
    result = fifth_function()
    assert result == "12 sdf"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_sixth_function():
    result = sixth_function()
    assert result == "12 13"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_seventh_function():
    result = seventh_function()
    assert result == "12 13"
