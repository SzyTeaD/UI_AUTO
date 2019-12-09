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
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='打卡']").click()

    def clockoutbtn(self):
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.widget.ListView[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]").click()

    def clockinbtn(self):
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.widget.ListView[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]").click()

    def attendancebtn(self):
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='attendance-right']").click()