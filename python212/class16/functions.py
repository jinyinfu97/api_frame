# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/15
# @Email:2155896749@qq.com
# @File: functions.py


# 需求：统计每个函数的耗时多久
import time

"""
"""
# 装饰器函数

# 其他函数只要被装饰器函数装饰即可
def runTime(func):
    """
    原来功能+扩展的功能：统计每个函数的耗时多久
    :return:
    """
    def wrapper():
        start = time.time()
        # 原来功能
        func()     # 原来功能
        end = time.time()
        cost = end - start
        print(f"统计函数总共耗时{cost}秒1")
    return  wrapper


def welcome_vip():

    print("欢迎来到码尚学院VIP课堂")
    time.sleep(1)


# 代表wrapper函数
welcome_vip=runTime(welcome_vip)   # 没有用装饰器与用了装饰器的区别-----》装饰器执行的原理
print(welcome_vip)
# 执行wrapper函数()
welcome_vip()

