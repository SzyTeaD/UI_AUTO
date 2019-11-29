import os
import time

from config.pathes import REPORT_PATH, NOW
from utils.BasicPage import Basic, browser

# driver = browser()
# dr = Basic(driver)

def txt(*args):
    return str(*args)
ele = ('id', 'VerifyCodeImg')
print(type(txt(ele)))