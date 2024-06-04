
# utils/appium_utils.py
from appium import webdriver


def initialize_appium_driver():
    desired_caps = {
        'platformName': 'Android',  # или 'iOS'
        'platformVersion': 'ваша_версия_платформы',
        'deviceName': 'ваше_устройство',
        'app': 'путь_к_вашему_приложению.apk',  # или .ipa для iOS
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
