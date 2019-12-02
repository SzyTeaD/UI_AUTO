import os
import sys
import time

from config.pathes import REPORT_PATH, NOW
from utils.BasicPage import Basic, browser

# driver = browser()
# dr = Basic(driver)

def txt(*args):
    return str(*args)
ele = ('id', 'VerifyCodeImg')
print(os.path.join(REPORT_PATH, NOW + ' report.html'))


terminal = sys.stdout.write
print(terminal)
for line in sys.stdin:
    print(line)