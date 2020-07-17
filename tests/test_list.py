import pytest


def test_clear(test_list):
    """
    Проверка, что метод clear() удаляет все элементы из списка.
    """
    test_list.clear()
    assert test_list == []


def test_copy(test_list):
    """
    Проверка, что метод copy() создаёт поверхностную копию списка.
    """
    test_list_copy = test_list[:]
    assert test_list_copy == test_list


def test_reverse(test_list):
    """
    Проверка, что метод reverse() разворачивает список.
    """
    list_reversed = []
    for i in range(len(test_list)):
        list_reversed.insert(-i, test_list[i])

    test_list.reverse()
    assert test_list == list_reversed


@pytest.mark.parametrize("last_element", [1, 0.0001, "test", False])
def test_append(test_list, last_element):
    """
    Проверки, что метод append() добавляет элемент в конец списка.
    """
    test_list.append(last_element)
    assert test_list[-1] == last_element


@pytest.mark.parametrize("pop_element_pos", [-1, 0])
def test_insert(test_list, pop_element_pos):
    """
    Проверки, что метод pop() возвращает удалённый элемент.
    """
    test_list_copy = test_list.copy()
    pop_element = test_list.pop(pop_element_pos)
    assert pop_element == test_list_copy[pop_element_pos]
