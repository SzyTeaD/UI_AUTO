import os

import psutil

def appstop():
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        # print('pid-%s,pname-%s' % (pid, p.name()))
        if 'Appium.exe' in p.name():
            cmd = 'taskkill /F /IM Appium.exe'
            os.system(cmd)
            print('stop appium')

def appstart(devices = '7XBNW18C10005211'):
    cmd = 'start /b appium -a 127.0.0.1 -p 4723 -bp 4728 --chromedriver-port 9519 -U %s --session-override --no-reset' %devices
    os.system(cmd)
    print('start appium')

if __name__ == '__main__':
    appstart()