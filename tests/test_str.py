import pytest


def test_clear():
    """
    Проверка, что метод upper() капитализирует строку.
    """
    test_string_upper = "some test string".upper()
    assert test_string_upper == "SOME TEST STRING"


def test_replace():
    """
    Проверка, что метод replace() возвращает копию строки, в которой заменены
    вхождения указанной строки новым значением.
    """
    test_string = "barbarian"
    test_string_replaced = test_string.replace("bar", "mur")
    assert test_string_replaced == "murmurian"


def test_split(test_str):
    """
    Проверка, что метод split() разделяет строку на элементы списка
    по заданному разделителю (пробел по умолчанию).
    """
    lst = test_str.split()
    assert isinstance(lst, list)
    assert " " not in lst


@pytest.mark.parametrize("idx", [0, -1])
def test_strip(test_str, idx):
    """
    Проверки, что метод strip() обрезает пробелы в начале и конце строки.
    """
    stripped_str = test_str.strip()
    assert not stripped_str[idx].isspace()


@pytest.mark.parametrize("some_string", ["123456789", "000", "1", "7000"])
def test_isdigit(some_string):
    """
    Проверки, что метод isdigit() возвращает True, если строка содержит
    только цифры.
    """
    assert some_string.isdigit()
