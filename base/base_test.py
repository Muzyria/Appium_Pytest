import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    driver_geco: webdriver.Firefox = None
    driver_chrome: webdriver.Chrome = None

    # @pytest.fixture(autouse=True)
    # def setup(self, request: pytest.FixtureRequest):
    #     request.cls.my_atr = "it is My atr"

    @classmethod
    def set_gecko_driver(cls):
        cls.driver_geco = webdriver.Firefox()
        print()
        print("START GECKO")
        print(cls.driver_geco.session_id)

    @classmethod
    def stop_gecko_driver(cls):
        cls.driver_geco.quit()
        print()
        print("STOP GECKO")

    @classmethod
    def set_chrome_driver(cls):
        cls.driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print()
        print("START CHROME")
        print(cls.driver_chrome.session_id)

    @classmethod
    def stop_chrome_driver(cls):
        cls.driver_chrome.quit()
        print()
        print("STOP CHROME")


