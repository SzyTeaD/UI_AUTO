import random
import time

from utils.report import runner

time.sleep(random.randint(1, 90))
test = 'test_oa_clockout*'
runner(test)

