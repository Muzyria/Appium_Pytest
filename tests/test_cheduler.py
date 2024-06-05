import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import os
import time

class TestSheduler:
    @pytest.fixture(scope="function")
    def appium_driver(self):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='dbe407da',
            # appPackage='com.android.settings',
            # appActivity='.Settings',
            # language='en',
            # locale='US'
        )

        appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        yield self.driver
        self.driver.quit()

    def test_sheduller_switch(self, appium_driver):
        os.system('adb shell am start -a android.settings.DATE_SETTINGS')

        date_time_menu = self.driver.find_element(AppiumBy.ID, 'com.android.settings:id/list')
        print(date_time_menu.__dict__)

        set_power_off_time = self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[8]')
        set_power_off_time.click()

        for h in range(1, 13):
            self.driver.find_element(AppiumBy.ID, 'android:id/hours').click()
            time_hours = self.driver.find_element(AppiumBy.XPATH,f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{h}"]').click()
            # time.sleep(0.1)

        for m in range(0, 60, 5):
            self.driver.find_element(AppiumBy.ID, 'android:id/minutes').click()
            time_minuts = self.driver.find_element(AppiumBy.XPATH,f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{m}"]').click()
            # time.sleep(0.1)

        time.sleep(5)

        ok_button = self.driver.find_element(AppiumBy.ID, 'android:id/button1').click()
