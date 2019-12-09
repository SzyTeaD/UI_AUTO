import time


class Clock():
    '''签到中心'''
    def __init__(self,driver):
        self.driver = driver

    def select_address(self,address):
        time.sleep(1)
        self.driver.find_element_by_accessibility_id('点石商务公园').click()
        time.sleep(1)
        self.driver.find_element_by_accessibility_id('航天云网大厦').click()

    def clockbtn(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.view.View\")').click()

    # def clockoutbtn(self):
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.view.View\")').click()
