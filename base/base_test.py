import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request: pytest.FixtureRequest):
        request.cls.my_atr = "it is My atr"


