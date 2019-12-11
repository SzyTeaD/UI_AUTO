import os

import psutil

pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    print('pid-%s,pname-%s' % (pid, p.name()))
    if 'Appium.exe' in p.name():
        cmd = 'taskkill /F /IM Appium.exe'
        os.system(cmd)
        print('关闭appium')