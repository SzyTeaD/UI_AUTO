import os
import unittest

from config.pathes import REPORT_PATH, NOW, CASE_PATH
from utils import HTMLTestRunnerCN

def runner(test):
    discover = unittest.defaultTestLoader.discover(start_dir=CASE_PATH,
                                                   pattern=test)
    if not os.path.exists(REPORT_PATH):
        os.makedirs(REPORT_PATH)
    reportpath = os.path.join(REPORT_PATH, NOW + ' report.html')
    fp = open(reportpath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(fp)
    runner.run(discover)



if __name__ == '__main__':
    runner('test_clockout*')
