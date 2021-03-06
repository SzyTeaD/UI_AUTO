import random
import time
import unittest

from config.pathes import URLINFO, USERINFO
from test.page.ClockPage import Clock
from test.page.HomePage import Home
from test.page.WebOALoginPage import login
from utils.Assertion import assert_before_time
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
        time.sleep(random.randint(1,120))


    def test2_clock(self):
        Home(self.dr).center_of_clock()
        Clock(self.dr).mainiframe()
        Clock(self.dr).tabiframe()
        time.sleep(0.5)
        Clock(self.dr).clockin()

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()