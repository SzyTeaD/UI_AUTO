import random
import unittest

from config.pathes import USERINFO, URLINFO
from utils.FileReader import YamlReader


class logtest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.sum = 0

    def test1(self):
        if self.sum > 10:
            self.sum+=random.randint(1,6)

        else:
            self.sum+=random.randint(1,20)
        print(1,self.sum)

    def test2(self):
        if self.sum > 20:
            self.sum += random.randint(1, 6)

        else:
            self.sum += random.randint(1, 10)
        print(2,self.sum)

    @classmethod
    def tearDownClass(self):
        print(3,self.sum)

if __name__ == '__main__':
    c = YamlReader(URLINFO).get('OA').get('log')

    print(c)