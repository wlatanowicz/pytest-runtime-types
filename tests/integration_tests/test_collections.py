import typing

import pytest

import pytest_runtime_types


@pytest.mark.runtime_types
def test_returns_a_list_of_ints():
    def function() -> typing.List[int]:
        return [1, 2, 3]

    result = function()
    assert result == [1, 2, 3]


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_inner_type_returns_a_list_of_ints():
    def function() -> typing.List[int]:
        return ["a", "b", "c"]

    result = function()
    assert result == ["a", "b", "c"]


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_outer_type_returns_a_list_of_ints():
    def function() -> typing.List[int]:
        return (1, 2, 3)

    result = function()
    assert result == (1, 2, 3)


@pytest.mark.runtime_types
def test_returns_a_tuple_of_ints():
    def function() -> typing.Tuple[int]:
        return (1, 2, 3)

    result = function()
    assert result == (1, 2, 3)


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_inner_type_returns_a_tuple_of_ints():
    def function() -> typing.Tuple[int]:
        return ("a", "b", "c")

    result = function()
    assert result == ("a", "b", "c")


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_outer_type_returns_a_tuple_of_ints():
    def function() -> typing.Tuple[int]:
        return [1, 2, 3]

    result = function()
    assert result == [1, 2, 3]


@pytest.mark.runtime_types
def test_returns_a_dict_of_str_to_ints():
    def function() -> typing.Dict[str, int]:
        return {"a": 1, "b": 2}

    result = function()
    assert result == {"a": 1, "b": 2}


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_inner_type_value_returns_a_dict_of_str_to_ints():
    def function() -> typing.Dict[str, int]:
        return {"a": "1", "b": 2}

    result = function()
    assert result == {"a": "1", "b": 2}


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_inner_type_key_returns_a_dict_of_str_to_ints():
    def function() -> typing.Dict[str, int]:
        return {"a": 1, 3: 2}

    result = function()
    assert result == {"a": 1, 3: 2}


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_outer_type_returns_a_dict_of_str_to_ints():
    def function() -> typing.Dict[str, int]:
        return [1, 2, 3]

    result = function()
    assert result == [1, 2, 3]
