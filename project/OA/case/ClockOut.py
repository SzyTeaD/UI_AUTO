import random
import time
import unittest

from config.pathes import URLINFO, USERINFO
from project.OA.page.loginpage import login
from utils.BasicPage import Basic
from utils.FileReader import YamlReader


class ClockIn(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dr = Basic()
        url = YamlReader(URLINFO).get('OAHomeUrl')
        self.dr.open(url)

    def test1_login(self):
        username = YamlReader(USERINFO).get('YX')
        password = YamlReader(USERINFO).get('YXPSWD')
        login(self.dr, username, password)

    def test2_clock(self):
        time.sleep(2)
        self.dr.click('css','[class="vportal vp-onlineRecord"]')
        time.sleep(random.randint(1,300))
        c = self.dr.text('class','card-punch-start-inner')
        print(c)

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()