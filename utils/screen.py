from config.pathes import SCREENSHOT_PATH


class Screen(object):

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        def inner (*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                import time
                self.driver.get_screenshot_as_file(SCREENSHOT_PATH)
                raise
