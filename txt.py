import random

from retrying import retry


@retry(stop_max_attempt_number=11)
class flu():
    def __init__(self):
        self.sum = 0


    def retry_test(self):
        a = random.randint(1,10)
        b = random.randint(1,5)
        self.sum += 1
        assert a == b
        print(self.sum)
flu().retry_test()