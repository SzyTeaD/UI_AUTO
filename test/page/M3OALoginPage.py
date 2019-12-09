class M3OALogin():
    def __init__(self,driver):
        self.driver = driver

    def uesernametext(self,username):
        self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.EditText\").textContains(\"用户名\")').send_keys(username)

    def pswdtext(self,pswd):
        self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.EditText\").textContains(\"密 码\")').send_keys(pswd)

    def surebtn(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.Button\").textContains(\"登录\").resourceId(\"com.seeyon.cmp:id/btn_login\")').click()

    def loginflow(self,username,pswd):
        self.uesernametext(username)
        self.pswdtext(pswd)
        self.surebtn()