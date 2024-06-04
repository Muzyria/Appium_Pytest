
# utils/appium_utils.py
from appium import webdriver


def initialize_appium_driver():
    desired_caps = {
        'platformName': 'Android',  # или 'iOS'
        'platformVersion': '13',
        'deviceName': 'POCO X3 PRO',
        # 'app': 'путь_к_вашему_приложению.apk',  # или .ipa для iOS
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
