from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Navigation():
    '''导航中心'''
    def __init__(self,driver):
        self.driver = driver

    def nacigations(self):
        elements = WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_all_elements_located((By.ID, 'com.seeyon.cmp:id/main_tab_img_icon')))
        return elements

    def workbenchbtn(self):
        '''点击工作台'''
        self.nacigations()[2].click()

    def mybtn(self):
        '''点击工作台'''
        self.nacigations()[4].click()

    def clockbtn(self):
        '''签到'''
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ListView[1]/android.view.View[8]/android.view.View[1]').click()

