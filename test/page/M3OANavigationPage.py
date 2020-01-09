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
        """点击工作台"""
        self.nacigations()[2].click()

    def mybtn(self):
        """点击我的"""
        self.nacigations()[4].click()

    def clockbtn(self):
        """签到"""
        WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='签到']"))).click()

    def reclockbtn(self):
        """重新打卡"""
        WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='重新打卡']"))).click()
