import ctypes
import random
import unittest

from config.pathes import USERINFO, PROJECTINFO
from utils.FileReader import YamlReader
from utils.log import logger


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


class Out_color:
    FOREGROUND_WHITE = 0x0007
    FOREGROUND_BLUE = 0x01 | 0x08  # text color contains blue.
    FOREGROUND_GREEN = 0x02 | 0x08  # text color contains green.
    FOREGROUND_RED = 0x04 | 0x08  # text color contains red.
    FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
    STD_OUTPUT_HANDLE = -11
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def __init__(self):
        pass

    # @ set color in computer terminal.
    def set_color(self, color, handle=std_out_handle):
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool

    # Failed or Error messge is text color contains red.
    def messge_error(self, str):
        self.set_color(Out_color.FOREGROUND_RED)
        logger.info(str)
        self.set_color(Out_color.FOREGROUND_WHITE)

    # Passed messge is text color contains green.
    def messge_pass(self, str):
        self.set_color(Out_color.FOREGROUND_GREEN)
        logger.info(str)
        self.set_color(Out_color.FOREGROUND_WHITE)

    # Title messge is text color contains blue.
    def title(self, str):
        self.set_color(Out_color.FOREGROUND_BLUE)
        logger.info(str)
        self.set_color(Out_color.FOREGROUND_WHITE)



if __name__ == '__main__':
    c = YamlReader(PROJECTINFO).get('OA').get('log')
    output = Out_color()
    output.messge_pass("Passed")
