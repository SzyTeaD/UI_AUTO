import os
import sys
import time

from config.pathes import REPORT_PATH, NOW, URLINFO
from utils.BasicPage import Basic, browser

# driver = browser()
# dr = Basic(driver)
from utils.FileReader import YamlReader


def txt(*args):
    return str(*args)
ele = ('id', 'VerifyCodeImg')
print(os.path.join(REPORT_PATH, NOW + ' report.html'))


print(YamlReader(URLINFO).data)
