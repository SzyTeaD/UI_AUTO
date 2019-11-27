import os

from config.pathes import REPORT_PATH, NOW
from utils.BasicPage import Basic


reportpath = os.path.join(REPORT_PATH, NOW + ' report.html')
print(reportpath)