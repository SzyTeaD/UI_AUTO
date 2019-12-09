class M3OALogin():
    def __init__(self,driver):
        self.driver = driver

    def uesernametext(self,username):
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]").send_keys(username)

    def pswdtext(self,pswd):
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='密 码']").send_keys(pswd)

    def surebtn(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.Button\").textContains(\"登录\").resourceId(\"com.seeyon.cmp:id/btn_login\")').click()

    def loginflow(self,username,pswd):
        self.uesernametext(username)
        self.pswdtext(pswd)
        self.surebtn()