import time

from django.test import TestCase

# Create your tests here.
# import random
#
# num = random.randint(0, 9)
# lowalf = chr(random.randint(97, 122))
# upalf = chr(random.randint(65, 90))

# 装饰器 闭包函数
# def foo():
#     x = 123
#     print(x)
# print(foo.__name__)

# 闭包函数的规则：内层函数应用了外层函数的环境变量，这样的函数称之为闭包函数
#
# def foo():
#     x = 10
#     def inner():
#         print(x)
#     return inner
#
# func = foo()
# func()


##########################################################

def times(fn):
    def inner():
        start = time.time()
        fn()
        elapsed = (time.time() - start)
        print(elapsed)
    return inner

@times
def t():
    ret = 1
    for i in range(100000000):
        ret += i

t()


