import random
import time
import unittest

from config.pathes import URLINFO, USERINFO
from test.page.ClockPage import Clock
from test.page.HomePage import Home
from test.page.LoginPage import login
from utils.Assertion import assert_after_time
from utils.BasicPage import Basic, browser
from utils.FileReader import YamlReader


class ClockIn(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.dr = Basic(self.driver)
        url = YamlReader(URLINFO).get('OAHomeUrl')
        self.dr.open(url)

    def test1_login(self):
        username = YamlReader(USERINFO).get('OAUSER')
        password = YamlReader(USERINFO).get('OAPSWD')
        login(self.dr, username, password)

    def test2_clock(self):
        time.sleep(2)
        Home(self.dr).center_of_clock()
        time.sleep(random.randint(1,120))
        Clock(self.dr).mainiframe()
        Clock(self.dr).tabiframe()
        Clock(self.dr).clockout()

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()