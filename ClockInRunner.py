import random
import time

from config.pathes import PROJECTINFO
from utils.FileReader import YamlReader
from utils.mail import Mail
from utils.report import runner

Y = []
# time.sleep(random.randint(1, 90))
test = 'test_oa_clockin_Y*'
runner(test)
receusers = YamlReader(PROJECTINFO).get('OA').get('mail')['receusers'][0]
Y.append(receusers)
eml = Mail('OA', Y)
eml.send_mail()
# ZH = []
# time.sleep(random.randint(1, 90))
# test = 'test_oa_clockin_ZH*'
# runner(test)
# eml = Mail('OA')
# eml.send_mail()
