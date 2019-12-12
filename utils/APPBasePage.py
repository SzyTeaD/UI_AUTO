from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class APPBase():
    def __init__(self,deviceName,appPackage,appActivity):
        self.deviceName = deviceName
        self.appPackage = appPackage
        self.appActivity = appActivity
        self.driver = self.get_driver()

    def get_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.1'
        desired_caps['deviceName'] = self.deviceName
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver

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

    def click(self, type, value):
        """单击"""
        element = self.element(type, value)
        element.click()

    def click_perform(self, value1, value2):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        element1.click()

    def input(self, type, value, text):
        """清除输入框内容并发送文本"""
        element = self.element(type, value)
        # element.clear()
        element.send_keys(text)

    def input_perform(self, value1, value2, inputvalue):
        element1 = self.driver.find_element_by_css_selector(
            value1).find_element_by_css_selector(value2)
        element1.input(inputvalue)

    def lock(self,time=5):
        """锁定屏幕时间"""
        self.driver.lock(time)

    def background(self,time=5):
        """将APP放置后台"""
        self.driver.background_app(time)

    def hide_keyboard(self):
        """收起键盘"""
        self.driver.hide_keyboard()

    def activity(self,pagename,activityname):
        """启动Activity"""
        self.driver.start_activity(pagename, activityname)

    def open_notifications(self):
        """打开通知栏"""
        self.driver.open_notifications()

    def is_installed(self,pagename):
        """检查应用是否已经安装 参数包名"""
        self.driver.is_app_installed(pagename)

    def parameter_app(self,path):
        """安装应用 参数 路径"""
        self.driver.install_app(path)

    def remove_app(self, pagename):
        """删除"""
        self.driver.remove_app(pagename)

    def shake(self):
        """检查应用是否已经安装 参数包名"""
        self.driver.shake()

    def close_app(self):
        """关闭应用"""
        self.driver.close_app()

    def reset(self):
        """重置（等于卸载后重装）"""
        self.driver.reset()

    # def get_text(self):
    #     """获得字符串"""
    #     return self.driver.app_strings

    def current_activity(self):
        """获取当前Activity"""
        return self.driver.current_activity

    def touch(self,element):
        """触摸动作(TouchAction) / 多点触摸动作(MultiTouchAction)"""
        action = TouchAction(self.driver)
        action.press(el=element, x=10, y=10).release().perform()

    def swipe(self,start=75, starty=500, endx=75, endy=0, duration=800):
        """参数 开始x,y坐标   滑动到的X,y坐标， 持续时间ms"""
        self.driver.swipe(start, starty, endx, endy,duration)

    def zoom(self,coordinate,time):
        """坐标点击"""
        self.driver.tap(coordinate,time)

    def scroll(self,ele1,ele2):
        """滚动"""
        self.driver.scroll(ele1, ele2)

    def drag_and_drop(self, ele1, ele2):
        """按住element并拖动到另外一个element上"""
        self.driver.drag_and_drop(ele1,ele2)

    def keyevent(self,keycod):
        """
        电话键
        KEYCODE_CALL 拨号键 5  KEYCODE_ENDCALL 挂机键 6   KEYCODE_HOME 按键Home 3
        KEYCODE_MENU 菜单键 82 KEYCODE_BACK 返回键 4  KEYCODE_SEARCH 搜索键 84
        KEYCODE_CAMERA 拍照键 27   KEYCODE_FOCUS 拍照对焦键 80  KEYCODE_POWER 电源键 26
        KEYCODE_NOTIFICATION 通知键 83 KEYCODE_MUTE 话筒静音键 91   KEYCODE_VOLUME_MUTE 扬声器静音键 164
        KEYCODE_VOLUME_UP 音量增加键 24  KEYCODE_VOLUME_DOWN 音量减小键 25
        控制键
        KEYCODE_ENTER 回车键 66    KEYCODE_ESCAPE ESC键 111 KEYCODE_DPAD_CENTER 导航键 确定键 23
        KEYCODE_DPAD_UP 导航键 向上 19   KEYCODE_DPAD_DOWN 导航键 向下 20 KEYCODE_DPAD_LEFT 导航键 向左 21
        KEYCODE_DPAD_RIGHT 导航键 向右 22    KEYCODE_MOVE_HOME 光标移动到开始键 122
        KEYCODE_MOVE_END 光标移动到末尾键 123   KEYCODE_PAGE_UP 向上翻页键 92
        KEYCODE_PAGE_DOWN 向下翻页键 93  KEYCODE_DEL 退格键 67
        KEYCODE_FORWARD_DEL 删除键 112 KEYCODE_INSERT 插入键 124
        KEYCODE_TAB Tab键 61 KEYCODE_NUM_LOCK 小键盘锁 143   KEYCODE_CAPS_LOCK 大写锁定键 115
        KEYCODE_BREAK Break/Pause键 121  KEYCODE_SCROLL_LOCK 滚动锁定键 116   KEYCODE_ZOOM_IN 放大键 168 KEYCODE_ZOOM_OUT 缩小键 169
        组合键
        KEYCODE_ALT_LEFT Alt+Left   KEYCODE_ALT_RIGHT Alt+Right
        KEYCODE_CTRL_LEFT Control+Left  KEYCODE_CTRL_RIGHT Control+Right
        KEYCODE_SHIFT_LEFT Shift+Left   KEYCODE_SHIFT_RIGHT Shift+Right
        """
        if keycod == 'back':   #后退
            self.driver.press_keycode (4)
        elif keycod == 'menu':  #菜单
            self.driver.press_keycode (82)
        elif keycod == 'home':   #Home
            self.driver.press_keycode (3)
        elif keycod == 'search':   #搜索键
            self.driver.press_keycode (84)
        elif keycod == 'power':   #电源键
            self.driver.press_keycode (26)
        elif keycod == 'notification':   #通知键
            self.driver.press_keycode (83)
        elif keycod == 'call':   #拨号键
            self.driver.press_keycode (5)
        elif keycod == 'endcall':   #挂机键
            self.driver.press_keycode (6)
        elif keycod == 'camera':   #拍照键
            self.driver.press_keycode (27)

if __name__ == '__main__':
    app = APPBase('7XBNW18C10005211','com.seeyon.cmp','.ui.LoadActivity')