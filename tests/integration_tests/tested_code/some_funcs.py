from dataclasses import dataclass


def called_function(a: int, b: str) -> str:
    if a is None:
        return None
    return f"{a} {b}"


def first_function():
    return called_function(4, "5")


def second_function():
    return called_function("3", 123)


def third_function():
    return called_function("3", 123)


def fourth_function():
    return called_function(None, None)


def fifth_function():
    data = DummyData(12, "sdf")
    return data_func(data)


def sixth_function():
    data = DummyData.factory(12, 13)
    return data_func(data)


def seventh_function():
    data = AnotherDummyData(12, 13)
    return data_func(data)


def data_func(data: "DummyData") -> str:
    return f"{data.number} {data.text}"


@dataclass
class DummyData:
    number: int
    text: str

    @classmethod
    def factory(cls, number: int, text: str):
        return cls(number, text)


class AnotherDummyData:
    def __init__(self, number: int, text: str):
        self.number = number
        self.text = text

    @classmethod
    def factory(cls, number: int, text: str):
        return cls(number, text)
