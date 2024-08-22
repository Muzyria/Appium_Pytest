import time

import pytest
from base.base_test import BaseTest

@pytest.mark.skip
class TestTwo(BaseTest):
    # @pytest.mark.skipif('config.getoption("--run_slow") == "False"')
    def test_two(self, start_geco_base):
        print()
        print("test two")
        print("----------------------------2------------------------------")
        print()
        print("HOW TO CHECK GECO DRIVER ?")
        print(BaseTest.driver_geco.session_id)
        BaseTest.driver_geco.get("https://www.google.com/")
        time.sleep(1)
        print()
        BaseTest.stop_gecko_driver()
        print()

        BaseTest.set_gecko_driver()
        print("HOW TO CHECK GECO DRIVER ?")
        print(BaseTest.driver_geco.session_id)
        BaseTest.driver_geco.get("https://www.google.com/")
        time.sleep(1)
        print("----------------------------2------------------------------")