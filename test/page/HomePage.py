class Button():
    def __init__(self,driver):
        self.driver = driver

    def clock(self):
        self.driver.click('css', '[class="vportal vp-onlineRecord"]')