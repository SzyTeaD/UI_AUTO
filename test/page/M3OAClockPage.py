import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Clock():
    '''签到中心'''
    def __init__(self,driver):
        self.driver = driver

    def select_address(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='航天云网大厦']").click()

    def clockbtn(self):
        WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_element_located((By.XPATH,"//android.view.View[@content-desc='打卡']"))).click()


    def clockoutbtn(self):
        WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_element_located((By.XPATH,"//android.view.View[@content-desc='签退']"))).click()

    def clockinbtn(self):
        WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_element_located((By.XPATH,"//android.view.View[@content-desc='签到']"))).click()

    def attendancebtn(self):
        WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.Button[@resource-id='attendance-right']"))).click()
