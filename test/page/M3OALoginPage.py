from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class M3OALogin():
    def __init__(self,driver):
        self.driver = driver

    def textelements(self):
        elements = WebDriverWait(self.driver, 15, 1).until(
            expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'android.widget.EditText')))
        return elements

    def uesernametext(self,username):
        self.textelements()[0].send_keys(username)

    def pswdtext(self,pswd):
        self.textelements()[1].send_keys(pswd)

    def surebtn(self):
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.seeyon.cmp:id/btn_login']").click()

    def returnlogpage(self):
        self.driver.find_element_by_id('com.seeyon.cmp:id/buttonDefaultPositive').click()