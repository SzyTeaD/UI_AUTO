class Clock():
    def __init__(self,driver):
        self.driver = driver
    def mainiframe(self):
        self.driver.iframe('id','mainIframe')

    def tabiframe(self):
        self.driver.iframe('id', 'tab_iframe')

    def clockin(self):
        self.driver.click('xpath','/html/body/div/div[2]/div/div[1]/div/div')

    def clockin_info(self):
         self.driver.text('css','body > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(1) > span:nth-child(4) > span')

    def clockout(self):
        self.driver.click('xpath','/html/body/div/div[3]/div/div[1]/div/div')

    def clockout_info(self):
         self.driver.text('css','body > div > div:nth-child(3) > div > div:nth-child(2) > div:nth-child(1) > span.punch-dialog > span')

    def switch_to_statistics(self):
        '''切换到信息统计'''
        self.driver.click('xpath','//*[@id="statics"]/a')