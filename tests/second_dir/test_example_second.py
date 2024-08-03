import time

import pytest


@pytest.mark.xfail(reason="Test is expected to fail")
def test_second(driver):
    print("second test")
    print(driver)
    time.sleep(0.2)
    # print(gecko_driver)
    # print(chrome_driver)
    # gecko_driver.get("https://www.google.com/")
    # chrome_driver.get("https://www.google.com/")



# content of test_sample.py
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    # assert 0  # to see what was printed