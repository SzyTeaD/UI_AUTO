from utils.mail import send_mail
from utils.report import runner

test = 'test_oa_clockin*'
runner(test)
send_mail()
