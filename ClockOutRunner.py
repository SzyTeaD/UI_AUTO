from utils.mail import Mail
from utils.report import runner

test = 'test_oa_clockout*'
runner(test)
eml = Mail()
eml.send_mail()
