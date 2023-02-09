import pytest

import pytest_runtime_types


class SomeClass:
    @staticmethod
    def do_something(a: int, b: str) -> str:
        return f"{a} {b}"


@pytest.mark.skip("Static methods are not supported yet")
@pytest.mark.runtime_types
def test_call_object_function():
    result = SomeClass.do_something(123, "abc")
    assert result == "123 abc"


@pytest.mark.skip("Static methods are not supported yet")
@pytest.mark.xfail(strict=True, raises=pytest_runtime_types.fail.Exception)
@pytest.mark.runtime_types
def test_fail_call_object_function():
    result = SomeClass.do_something(123, 456)
    assert result == "123 456"
