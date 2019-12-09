import random
import time
import unittest

from appium import webdriver

from config.pathes import  USERINFO
from test.page.M3OAClockPage import Clock
from test.page.M3OALoginPage import M3OALogin
from test.page.M3OANavigationPage import Navigation
from utils.FileReader import YamlReader


class ClockIn(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '7XBNW18C10005211'
        desired_caps['appPackage'] = 'com.seeyon.cmp'
        desired_caps['appActivity'] = '.ui.LoadActivity'
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test1_login(self):
        time.sleep(3)
        username = YamlReader(USERINFO).get('OAUSER')
        password = YamlReader(USERINFO).get('OAPSWD')
        try:
            M3OALogin(self.dr).loginflow(username, password)
        # time.sleep(random.randint(1,120))
        except Exception :
            pass


    def test2_intoclockcenter(self):
        Navigation(self.dr).Workbenchbtn()
        time.sleep(2)
        Navigation(self.dr).clockbtn()
        time.sleep(2)

    def test3_seleadress(self):
        Clock(self.dr).select_address('航天云网大厦')
        time.sleep(1)

    def test4_clockin(self):
        Clock(self.dr).clockbtn()



    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()