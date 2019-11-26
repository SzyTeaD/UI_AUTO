import unittest


def dependon(depend=None):
    '''
    可以适用于依赖的测试用例失败
    或错误时都跳过测试用例，
    有dependon装饰器标记的用例必须在
    用例depend（test_login）之后执行
    '''
    import functools
    def wraper_func(test_func):
        @functools.wraps(test_func)
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            print("self._resultForDoCleanups", self._resultForDoCleanups.__dict__)
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            test = unittest.skipIf(flag, '{} failed  or  error or skipped'.format(depend))(test_func)
            return test(self)

        return inner_func
