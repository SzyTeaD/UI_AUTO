import os
import time

from config.pathes import REPORT_PATH, NOW
from utils.BasicPage import Basic, browser

driver = browser()
dr = Basic(driver)
dr.open('https://wx.qq.com/')
time.sleep(2)
driver.refresh()