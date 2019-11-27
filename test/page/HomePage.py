class Home():
    def __init__(self,driver):
        self.driver = driver

    def center_of_clock(self):
        self.driver.click('css', '[class="vportal vp-onlineRecord"]')