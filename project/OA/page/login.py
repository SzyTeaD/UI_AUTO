from config.pathes import USERINFO, URLINFO
from utils.BasicPage import browser, Basic
from utils.FileReader import YamlReader
from utils.verifyCode import verifyCode

def login(driver,username,password):
    old_url = driver.current_url()
    while True:
        driver.clear('id','login_username')
        driver.input('id','login_username',username)
        driver.clear('id','login_password')
        driver.input('id','login_password',password)
        code = verifyCode(driver)
        driver.input('id', 'VerifyCode', code)
        driver.click('id','login_button')
        new_url =  driver.current_url()
        if new_url != old_url:
            break
        else:
            driver.refresh()

if __name__ == '__main__':
    # driver = browser()
    # dr = Basic(driver)
    url = YamlReader(URLINFO).get('OAHomeUrl')
    print(url)
    # dr.open(url)
    # username = YamlReader(USERINFO).get('YX')
    # password = YamlReader(USERINFO).get('YXPSWD')
    # login(dr,username,password)