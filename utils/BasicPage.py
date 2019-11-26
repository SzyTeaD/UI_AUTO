from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class Browser():
    def get(browser):
        if browser == 'ie':
            driver = webdriver.Edge()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'opera':
            driver = webdriver.Opera()
        else:
            driver = webdriver.Chrome()
        return driver


class Basic(Browser):
    def __init__(self):
        self.driver = Browser().get()

    def open(self, url, time=15):
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

    def select_by_index(self, type, value, index):
        """通过所有index，0开始,定位元素"""
        try:
            element = self.element(type, value, timeout=10)
            Select(element).select_by_index(index)
        except BaseException:
            print("%s 页面未找到元素 %s" % (self, value))

    def select_by_value(self, type, value, value1):
        """通过value定位元素"""
        try:
            element = self.element(type, value, timeout=10)
            Select(element).select_by_value(value1)
        except BaseException:
            print("%s 页面未找到元素 %s" % (self, value))

    def select_by_text(self, type, value, text):
        """通过text定位元素"""
        try:
            element = self.element(type, value, timeout=10)
            Select(element).select_by_visible_text(text)
        except BaseException:
            print("%s 页面未找到元素 %s" % (self, value))

    def text_perform(self, value1, value2):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        return element1.text

    def clear(self, type, value):
        """清除文本框"""
        element = self.element(type, value)
        element.clear()

    def text(self, type, value):
        """获取文本内容"""
        element = self.element(type, value)
        return element.text

    def get_attribute(self, type, value, name):
        """获得属性"""
        element = self.element(type, value)
        return element.get_attribute(name)

    def location(self, type, value):
        """获得元素坐标"""
        element = self.element(type, value)
        return element.location

    def size(self, type, value):
        """获取元素尺寸"""
        element = self.element(type, value)
        return element.size

    def save_screenshot(self, filename):
        """截图"""
        self.driver.save_screenshot(filename)

    def current_url(self):
        """获取当前URL"""
        return self.driver.current_url

    def cookies(self):
        """获取当前COOKIES"""
        return self.driver.get_cookies()

    def title(self):
        """获取当前title"""
        return self.driver.title

    def quit(self):
        """关闭浏览器"""
        return self.driver.quit()

    def close(self):
        """关闭窗口"""
        return self.driver.close()

    def forward(self):
        """前进"""
        return self.driver.forward()

    def back(self):
        """后退"""
        return self.driver.back()

    def refresh(self):
        """刷新"""
        return self.driver.refresh()

    def click(self, type, value):
        """单击"""
        element = self.element(type, value)
        element.click()

    def click_perform(self,value1,value2):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        element1.click()

    def move_to(self, type, value):
        """鼠标悬疑"""
        element = self.element(type, value)
        ActionChains(self.driver).move_to_element(element).perform()

    def context_click(self, type, value):
        """鼠标右键"""
        element = self.element(type, value)
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, type, value1, value2):
        """拖拽"""
        element = self.element(type, value1)
        target = self.element(type, value2)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def input(self, type, value, text):
        """清除输入框内容并发送文本"""
        element = self.element(type, value)
        # element.clear()
        element.send_keys(text)

    def input_perform(self, value1, value2, inputvalue):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        element1.input(inputvalue)

    def space(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.SPACE)

    def tab(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.TAB)

    def esc(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.ESCAPE)

    def enter(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.ENTER)

    def ctrla(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.CONTROL, 'a')

    def ctrlv(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.CONTROL, 'v')

    def ctrlc(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.CONTROL, 'c')

    def ctrlx(self, type, value):
        element = self.element(type, value)
        element.send_keys(Keys.CONTROL, 'x')

    def jump_off(self):
        """页面跳转后关闭窗口"""
        old_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != old_handle:
                self.driver.switch_to.window(handle)
            else:
                self.driver.close()

    def jump(self):
        """页面跳转"""
        old_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != old_handle:
                self.driver.switch_to.window(handle)

    def frame(self, value):
        self.driver.switch_to.frame(value)

    def frame_back(self):
        self.driver.switch_to.default_content()

    def alert(self):
        self.driver.switch_to.alert.accept()

    def js_script(self, js):
        """运行JS脚本"""
        self.driver.execute_script(js)

    def js_fours_element(self, locator):
        """聚焦元素"""
        element = self.element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_scroll_top(self):
        """滑动到页面顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滑动到页面底部"""
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)