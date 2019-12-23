import random
import time
import unittest

from appium import webdriver
from retrying import retry
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config.pathes import  USERINFO
from test.page.M3OAClockPage import Clock
from test.page.M3OALoginPage import M3OALogin
from test.page.M3OANavigationPage import Navigation
from utils.FileReader import YamlReader
from utils.log import Logger


class ClockIn(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.logger = Logger('OA').get_logger()
        time.sleep(random.randint(1, 90))
        zhang = YamlReader(USERINFO).get('OA')[1]
        for i,v in zhang.items():
            self.username=i
            self.password=v
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.1'
        desired_caps['deviceName'] = '7XBNW18C10005211'
        desired_caps['appPackage'] = 'com.seeyon.cmp'
        desired_caps['appActivity'] = '.ui.LoadActivity'
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    @retry(stop_max_attempt_number=3)
    def test1_login(self):
        time.sleep(3)
        try:
            self.dr.find_element_by_xpath("//android.widget.Button[@text='跳过']")
            self.dr.find_element_by_xpath("//android.widget.Button[@text='跳过']").click()
            print('跳过势密码设置')
        except Exception:
            print('无手势密码设置')
        try:
            self.dr.find_element_by_name("提示")
            self.dr.find_element_by_name("我知道了").click()
            time.sleep(1)
            self.dr.keyevent(4)
            print('跳过弱密码修改')
        except Exception:
            print('无弱密码修改')
        try:
            Navigation(self.dr).mybtn()
            WebDriverWait(self.dr, 15, 1).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//android.view.View[@resource-id='setting']"))).click()
            WebDriverWait(self.dr, 15, 1).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='退出登录']"))).click()
            WebDriverWait(self.dr, 15, 1).until(
                expected_conditions.presence_of_element_located((By.ID,"com.seeyon.cmp:id/buttonDefaultPositive"))).click()
        except Exception:
            self.logger.info('%s已退出登录' % self.username)
        M3OALogin(self.dr).uesernametext(self.username)
        M3OALogin(self.dr).pswdtext(self.password)
        M3OALogin(self.dr).surebtn()
        try:
            self.dr.find_element_by_xpath("//android.widget.Button[@text='跳过']")
            self.dr.find_element_by_xpath("//android.widget.Button[@text='跳过']").click()
            print('跳过势密码设置')
        except Exception:
            print('无手势密码设置')
        try:
            self.dr.find_element_by_name("提示")
            self.dr.find_element_by_name("我知道了").click()
            time.sleep(1)
            self.dr.keyevent(4)
            print('跳过弱密码修改')
        except Exception:
            self.logger.info('无弱密码修改')
        self.logger.info('%s已成功登录' % self.username)

    @retry(stop_max_attempt_number=3)
    def test2_seleadress(self):
        Navigation(self.dr).workbenchbtn()
        time.sleep(1)
        Navigation(self.dr).clockbtn()
        time.sleep(1)
        try:
            self.dr.find_element_by_accessibility_id('航天云网大厦')
        except Exception:
            Clock(self.dr).select_address()
        time.sleep(1)
        self.logger.info('%s已成功定位' % self.username)

    @retry(stop_max_attempt_number=3)
    def test3_clockin(self):
        Clock(self.dr).clockbtn()
        Clock(self.dr).clockinbtn()
        Clock(self.dr).attendancebtn()
        self.logger.info('%s已成功打卡' % self.username)


    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()