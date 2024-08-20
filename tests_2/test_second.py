import time

from base.base_test import BaseTest


class TestSecond:
    def test_second(self):
        print()
        print("test second")
        print("----------------------------second------------------------------")
        print()
        print("HOW TO CHECK GECO DRIVER ?")
        print(BaseTest.driver_chrome.session_id)
        time.sleep(2)
        print("----------------------------second------------------------------")