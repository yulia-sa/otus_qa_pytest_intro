import pytest


@pytest.fixture
def test_list():
    return [0, 1000000, 0.001, "some random string", True]


@pytest.fixture
def test_set():
    return {0, 1000000, 0.001, "some random string", True}


@pytest.fixture
def test_dict():
    return {
        'integer': 1,
        'float': 0.001,
        'string': "some random string",
        'boolean': True
    }


@pytest.fixture
def test_str():
    return "   some string with whitespaces   "
