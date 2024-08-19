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


        print("----------------------------2------------------------------")