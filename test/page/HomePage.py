class Home():
    def __init__(self,driver):
        self.driver = driver

    def center_of_clock(self):
        '''考勤中心'''
        self.driver.click('css', '[class="vportal vp-onlineRecord"]')