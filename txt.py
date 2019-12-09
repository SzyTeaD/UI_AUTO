import time

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '7XBNW18C10005211'
desired_caps['appPackage'] = 'com.seeyon.cmp'
desired_caps['appActivity'] = '.ui.LoadActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
# driver.find_element_by_class_xpath("//android.widget.EditText[@text='用户名']").send_keys('yangxin')
# driver.find_element_by_class_xpath("//android.widget.EditText[@text='密 码']").send_keys('yangxin')
# driver.find_element_by_class_xpath("//android.widget.Button[@resource-id='com.seeyon.cmp:id/btn_login']]").click()
driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.EditText\").textContains(\"用户名\")').send_keys('yangxin')

time.sleep(3)
driver.quit()