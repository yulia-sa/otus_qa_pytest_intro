import pytest


def test_clear(test_dict):
    """
    Проверка, что метод clear() удаляет все элементы из словаря.
    """
    test_dict.clear()
    assert test_dict == {}


def test_setdefault(test_dict):
    """
    Проверка, что метод setdefault() возвращает значение ключа, а если его нет —
    создает такой ключ со значением
    """
    test_dict.setdefault("new_key", "new_value")
    assert test_dict["new_key"] == "new_value"


def test_keys(test_dict):
    """
    Проверка, что метод keys() возвращает ключи словаря.
    """
    assert list(test_dict.keys()) == ["integer", "float", "string", "boolean"]


def test_pop(test_dict):
    """
    Проверка, что метод pop() удаляет ключ и возвращает его значение.
    """
    assert (test_dict.pop("float") == 0.001 and test_dict == {
                                                                'integer': 1,
                                                                'string': "some random string",
                                                                'boolean': True
                                                            })


@pytest.mark.parametrize("key", ["integer", "float", "string", "boolean"])
def test_get(test_dict, key):
    """
    Проверки, что метод get() возвращает значение по ключу.
    """
    assert all(test_dict.get(key) for value in test_dict.values())
