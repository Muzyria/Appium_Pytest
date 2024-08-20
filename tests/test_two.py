import time

import pytest
from base.base_test import BaseTest




class TestTwo(BaseTest):
    # @pytest.mark.skipif('config.getoption("--run_slow") == "False"')
    def test_two(self):
        print()
        print("test two")
        print("----------------------------2------------------------------")
        print()
        print("HOW TO CHECK GECO DRIVER ?")
        print(BaseTest.driver_geco.session_id)
        BaseTest.driver_geco.get("https://www.google.com/")
        time.sleep(2)
        print()
        BaseTest.stop_gecko_driver()
        print()

        BaseTest.set_gecko_driver()
        print("HOW TO CHECK GECO DRIVER ?")
        print(BaseTest.driver_geco.session_id)
        BaseTest.driver_geco.get("https://www.google.com/")
        time.sleep(2)
        print("----------------------------2------------------------------")