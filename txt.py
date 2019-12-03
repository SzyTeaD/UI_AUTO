import os
import sys
import time

from config.pathes import REPORT_PATH, NOW, URLINFO
from utils.BasicPage import Basic, browser

# driver = browser()
# dr = Basic(driver)
from utils.FileReader import YamlReader

lists = os.listdir(REPORT_PATH)

print(lists)
