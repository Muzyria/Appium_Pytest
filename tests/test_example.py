import time

import pytest

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(driver, order):
    print("test string")
    print(driver)
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


def test_one(driver):
    print("test one")
    print(driver)
    time.sleep(0.3)