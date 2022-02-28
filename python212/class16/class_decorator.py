# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/15
# @Email:2155896749@qq.com
# @File: class_decorator.py

# 需求：统计每个函数的耗时多久
import time

"""
"""
# 装饰器函数

# 其他函数只要被装饰器函数装饰即可

def runTime(func):
    """
    装饰函数
    原来功能+扩展的功能：统计每个函数的耗时多久
    :return:
    """
    def wrapper(*args,**kwargs):
        start = time.time()
        # 原来功能
        func(*args,**kwargs)     # 原来功能
        end = time.time()
        cost = end - start
        print(f"统计函数[{func.__name__}]总共耗时{cost}秒")
    return  wrapper

@runTime
def welcome_vip():
    """被装饰器函数"""
    print("欢迎来到码尚学院VIP课堂")
    time.sleep(1)

@runTime
def sum(*args):
    sum=0
    for num in args:
        sum+=num
    print(f"求和：{sum}")
    return sum


welcome_vip()    #实质：执行装饰函数的内置方法
sum(1,2,3,4,5,6,7,8,9,10)


