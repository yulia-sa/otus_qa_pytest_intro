import pytest


def test_clear(test_set):
    """
    Проверка, что метод clear() удаляет все элементы из множества.
    """
    test_set.clear()
    assert test_set == set()


def test_discard(test_set):
    """
    Проверка, что метод discard() удаляет из множества заданный элемент.
    """
    test_set.discard("some random string")
    assert "some random string" not in test_set


def test_difference(test_set):
    """
    Проверка, что метод difference() выводит множество всех элементов, не
    принадлежащих другому множеству.
    """
    other_set = {1000000, 0.001, True}
    assert test_set.difference(other_set) == {0, "some random string"}


def test_update(test_set):
    """
    Проверка, что метод update() объединяет два множества.
    """
    other_set = {500, None, 4}
    test_set.update(other_set)
    assert test_set == {0, 1000000, 0.001, "some random string", True, 500, None, 4}


@pytest.mark.parametrize("new_element", [123, 0.111, "new_string"])
def test_add(test_set, new_element):
    """
    Проверки, что метод add() добавляет элементы в множество.
    """
    test_set.add(new_element)
    assert new_element in test_set
