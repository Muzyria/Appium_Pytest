import pytest


@pytest.mark.xfail(reason="Test is expected to fail")
def test_second(driver, some_driver):
    print("second test")
    print(driver)
    print(some_driver)


