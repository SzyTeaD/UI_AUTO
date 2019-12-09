import time

from config.pathes import USERINFO, URLINFO
from utils.BasicPage import Basic, browser
from utils.FileReader import YamlReader
from utils.verifyCode import verifyCode

def login(driver,username,password):
    '''在登录页循环提交登录信息，知道登录成功'''
    old_url = driver.current_url()
    while True:
        driver.clear('id','login_username')
        driver.input('id','login_username',username)
        driver.clear('id','login_password')
        driver.input('id','login_password',password)
        code = verifyCode(driver,'id', 'VerifyCodeImg')
        driver.input('id', 'VerifyCode', code)
        time.sleep(2)
        driver.click('id','login_button')
        new_url =  driver.current_url()
        if new_url != old_url:
            break
        else:
            driver.refresh()

if __name__ == '__main__':
    driver = browser()
    dr = Basic(driver)
    url = YamlReader(URLINFO).get('OAHomeUrl')
    dr.open(url)
    username = YamlReader(USERINFO).get('OAUSER')
    password = YamlReader(USERINFO).get('OAPSWD')
    login(dr,username,password)