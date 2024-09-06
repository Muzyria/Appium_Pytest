import time

import pytest

from base.base_test import BaseTest

@pytest.mark.skip
class TestSecond:
    def test_second(self, start_chrome_base):
        print()
        print("test second")
        print("----------------------------second------------------------------")
        print()
        print("HOW TO CHECK CHROME DRIVER ?")
        print(BaseTest.driver_chrome.session_id)
        time.sleep(2)
        print("----------------------------second------------------------------")

