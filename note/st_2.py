# coding=utf-8
"""
    面试题python
    装饰器的学习--函数装饰器、类装饰器
"""

import time
from unittest import skip

""" 函数装饰器 """


def runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print("运行时长：%.4f 秒" % (end - start))
        return f

    return wrapper


@runtime
def func_a(a):
    print("hello" + a)
    time.sleep(0.5)


@runtime
def func_b(b, c='xx'):
    print("world" + b + c)
    time.sleep(0.8)


if __name__ == '__main__':
    func_a(" john")
    func_b(" b", c="xxx")

"""
类装饰器
__name__获取方法名
__doc__获取方法中的函数注释

"""
from functools import wraps

@skip
class runtime(object):
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''自定义装饰器方法'''
            print("当前运行方法：%s" % func.__name__)
            print("当前运行方法注释内容：%s" % func.__doc__)
            f = func(*args, **kwargs)
            start = time.time()
            time.sleep(1)
            end = time.time()
            print("运行时长：%.4f 秒" % (end - start))
            return f

        return wrapper


@runtime()
def func_a(a):
    """用例1"""
    print("hello" + a)
    time.sleep(0.5)


@runtime()
def func_b(b, c='xx'):
    """用例2"""
    print("world" + b + c)
    time.sleep(0.8)


if __name__ == '__main__':
    func_a(" 类装饰")
    func_b(" fuck", c="类装饰器学习")
    print(func_a.__name__)
    print(func_a.__doc__)

