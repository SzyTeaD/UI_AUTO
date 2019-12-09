class Navigation():
    '''导航中心'''
    def __init__(self,driver):
        self.driver = driver

    def Workbenchbtn(self):
        '''点击工作台'''
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                                      '/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
                                      '/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]'
                                      '/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]'
                                      '/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
                                      '/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]'
                                      '/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    def clockbtn(self):
        '''签到'''
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.seeyon.cmp.lib_swipeclose.TranslucentSlidingPaneLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ListView[1]/android.view.View[8]/android.view.View[1]').click()

