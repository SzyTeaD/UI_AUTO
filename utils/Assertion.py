import time


def assert_before_time(hours,minutes):
    H = int(time.strftime('%H', time.localtime(time.time())))
    M = int(time.strftime('%M', time.localtime(time.time())))
    if H < int(hours) and M < int(minutes):
            print('在规定时间内操作')
    else:
        raise AssertionError('已经超出时间！')

def assert_after_time(hours,minutes):
    H = int(time.strftime('%H', time.localtime(time.time())))
    M = int(time.strftime('%M', time.localtime(time.time())))
    if H > int(hours) and M > int(minutes):
            print('在规定时间内操作')
    else:
        raise AssertionError('未到工作时间！')

if __name__ == '__main__':
    assert_after_time(10,30)