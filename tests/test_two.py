import pytest
from base.base_test import BaseTest


class TestTwo(BaseTest):
    def test_two(self, driver, request: pytest.FixtureRequest):
        print()
        print("test two")
        print("----------------------------2------------------------------")
        print(request.node.attr1)
        print(request.cls.my_atr)

        print("----------------------------2------------------------------")