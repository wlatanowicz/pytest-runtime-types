from dataclasses import dataclass

import pytest

import pytest_runtime_types


@dataclass
class DataclassDummyData:
    number: int
    text: str


class PlainDummyData:
    def __init__(self, number: int, text: str):
        self.number = number
        self.text = text


@pytest.mark.runtime_types
def test_passed_object_by_class():
    def function(obj: PlainDummyData):
        return obj.number

    obj = PlainDummyData(123, "abc")
    result = function(obj)

    assert result == 123


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_failed_passed_object_by_class():
    def function(obj: PlainDummyData):
        return obj.number

    obj = DataclassDummyData(123, "abc")
    result = function(obj)

    assert result == 123


@pytest.mark.runtime_types
def test_passed_object_by_string():
    def function(obj: "PlainDummyData"):
        return obj.number

    obj = PlainDummyData(123, "abc")
    result = function(obj)

    assert result == 123


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_failed_passed_object_by_string():
    def function(obj: "PlainDummyData"):
        return obj.number

    obj = DataclassDummyData(123, "abc")
    result = function(obj)

    assert result == 123
