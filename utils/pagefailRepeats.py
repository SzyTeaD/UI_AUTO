import unittest

from config.pathes import SCREENSHOT_PATH


class PageFailRepeat(unittest.TestCase):

    def __init__(self,driver,page):
        self.driver = driver
        self.page = page

    def estimate(self):
        self.driver.refresh()
        while True:
            state = 0
            self.page(self.driver)
            state += 1
            if self.assertTrue(self.page):
                break
            if state > 3:
                self.driver.save_screenshot(SCREENSHOT_PATH)
                break
