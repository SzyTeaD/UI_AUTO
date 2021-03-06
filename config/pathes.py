"""
文件路径
"""
import os
import time

DAY = time.strftime('%Y-%m-%d',time.localtime(time.time()))
TIME = time.strftime(' %H-%M-%S',time.localtime(time.time()))
NOW = DAY + TIME
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
HOME_PATH = os.path.split(os.path.split(BASE_PATH)[0])[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
USERINFO = os.path.join(CONFIG_PATH, 'UserInfo.yml')
PROJECTINFO = os.path.join(CONFIG_PATH, 'ProjectInfo.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
PICTURE_PATH = os.path.join(BASE_PATH, 'picture')
DRIVER_PATH = os.path.join(BASE_PATH, 'driver')
CHROME_PATH = os.path.join(DRIVER_PATH,'chromedriver.exe')
EDGE_PATH = os.path.join(DRIVER_PATH,'MicrosoftWebDriver.exe')
FIRFOX_PATH = os.path.join(DRIVER_PATH,'geckodriver.exe')
OPERA_PATH = os.path.join(DRIVER_PATH,'operadriver.exe')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
CASE_PATH = os.path.join(os.path.join(BASE_PATH,'test'), 'case')
IMAGE_PATH = os.path.join(os.path.join(PICTURE_PATH,'verifycode') , 'picture.png')
FRAME_PATH = os.path.join(os.path.join(PICTURE_PATH,'verifycode'), 'frame4.png')
SCREENSHOT_PATH = os.path.join(os.path.join(PICTURE_PATH,'screenshot'), NOW+'wrong.png')

if __name__ == '__main__':
    print(LOG_PATH)