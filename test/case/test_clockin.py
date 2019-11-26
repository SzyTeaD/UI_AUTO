import random
import time
import unittest

from config.pathes import URLINFO, USERINFO
from test.page.HomePage import Button
from test.page.LoginPage import login
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
        Button(self.dr).clock()
        time.sleep(random.randint(1,300))
        self.dr.click('class','card-punch-end-inner')

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()