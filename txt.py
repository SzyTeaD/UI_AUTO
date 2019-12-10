import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.1'
desired_caps['deviceName'] = '7XBNW18C10005211'
desired_caps['appPackage'] = 'com.seeyon.cmp'
desired_caps['appActivity'] = '.ui.LoadActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)



a = WebDriverWait(driver, 15, 1).until(
    expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))
elements = WebDriverWait(driver, 15, 1).until(
    expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))

print(a[1],a[0],a)
elements[0].send_keys('saf')

