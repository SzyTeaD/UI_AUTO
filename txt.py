import os
import time

import psutil
from appium import webdriver

from test.page.M3OAClockPage import Clock
from test.page.M3OANavigationPage import Navigation

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.1'
desired_caps['deviceName'] = '7XBNW18C10005211'
desired_caps['appPackage'] = 'com.seeyon.cmp'
desired_caps['appActivity'] = '.ui.LoadActivity'
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
Navigation(dr).workbenchbtn()
time.sleep(1)
Navigation(dr).clockbtn()
time.sleep(1)
if dr.find_element_by_accessibility_id('航天云网大厦'):
    print(1)
# Clock(dr).select_address()
time.sleep(1)