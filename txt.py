from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class browser():
    def browser(browser=None):
        if browser == 'ie':
            driver = webdriver.Edge()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'opera':
            driver = webdriver.Opera()
        else:
            driver = webdriver.Chrome()
        return driver

class Basic(browser):
    def __init__(self):
        self.driver = browser().browser()
    def get_url(self, url, time=15):
        """最大化打开网页"""
        self.driver.implicitly_wait(time)
        self.driver.maximize_window()
        self.driver.get(url)

    def element(self, type, value, timeout=10):
        """定位元素"""
        try:
            if type == 'xpath':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.XPATH, value)))
                return element
            elif type == 'id':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.ID, value)))
                return element
            elif type == 'name':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.NAME, value)))
                return element
            elif type == 'class':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, value)))
                return element
            elif type == 'link':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.LINK_TEXT, value)))
                return element
            elif type == 'css':
                element = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, value)))
                return element
        except BaseException:
            print("%s 页面未找到元素 %s" % (self, value))

    def elements(self, type, value, timeout=10):
        """定位一组元素"""
        try:
            if type == 'xpath':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, value)))
                return elements
            elif type == 'id':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.ID, value)))
                return elements
            elif type == 'name':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.NAME, value)))
                return elements
            elif type == 'class':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, value)))
                return elements
            elif type == 'link':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.LINK_TEXT, value)))
                return elements
            elif type == 'css':
                elements = WebDriverWait(
                    self.driver, timeout, 1).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, value)))
                return elements
        except BaseException:
            print("%s 页面未找到元素 %s" % (self, value))
class MouseEvent(Basic):
    def input(self, type, value, text):
        """清除输入框内容并发送文本"""
        element = self.element(type, value)
        element.send_keys(text)

if __name__ == '__main__':
    driver = browser()
    dr = Basic()
    dr.get_url('https://www.hao123.com/')
    dr.driver.find_element_by_name('word').send_keys('124124')
