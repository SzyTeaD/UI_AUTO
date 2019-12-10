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
        desired_caps['platformVersion'] = '9.1'
        desired_caps['deviceName'] = '7XBNW18C10005211'
        desired_caps['appPackage'] = 'com.seeyon.cmp'
        desired_caps['appActivity'] = '.ui.LoadActivity'
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test1_login(self):
        time.sleep(3)
        try:
            self.dr.find_element_by_name("跳过")
            self.dr.find_element_by_name("跳过").click()
        except Exception:
            print('无手势密码设置')
        try:
            self.dr.find_element_by_name("提示")
            self.dr.find_element_by_name("我知道了").click()
            time.sleep(1)
            self.dr.keyevent(4)
        except Exception:
            print('无弱密码修改')

        self.dr.find_elements_by_id("com.seeyon.cmp:id/main_tab_img_icon")[4].click()

            # username = YamlReader(USERINFO).get('OAUSER')
            # password = YamlReader(USERINFO).get('OAPSWD')
            # M3OALogin(self.dr).uesernametext(username)
            # M3OALogin(self.dr).pswdtext(password)
            # M3OALogin(self.dr).surebtn()



    # def test2_intoclockcenter(self):
    #     time.sleep(random.randint(1, 120))
    #     Navigation(self.dr).Workbenchbtn()
    #     time.sleep(2)
    #     Navigation(self.dr).clockbtn()
    #     time.sleep(2)
    #
    # def test3_seleadress(self):
    #     Clock(self.dr).select_address('航天云网大厦')
    #     time.sleep(1)
    #
    # def test4_clockin(self):
    #     Clock(self.dr).clockbtn()
    #     Clock(self.dr).clockoutbtn()
    #     Clock(self.dr).attendancebtn()


    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()