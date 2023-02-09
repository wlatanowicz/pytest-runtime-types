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
def test_plain_object_constructor():
    obj = PlainDummyData(123, "abc")
    assert obj.number == 123
    assert obj.text == "abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_plain_object_constructor():
    obj = PlainDummyData(123, 456)
    assert obj.number == 123
    assert obj.text == 456


@pytest.mark.runtime_types
def test_dataclass_constructor():
    obj = DataclassDummyData(123, "abc")
    assert obj.number == 123
    assert obj.text == "abc"


@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_dataclass_constructor():
    obj = DataclassDummyData(123, 456)
    assert obj.number == 123
    assert obj.text == 456
