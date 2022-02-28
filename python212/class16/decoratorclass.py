# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/15
# @Email:2155896749@qq.com
# @File: decoratorclass.py

"""
装饰器类

"""
import time

# # 定义装饰类-----》本质类   作用：原来功能+扩展功能
# class A:
#     #原来功能   self._func()
#     def __init__(self,func):
#         self._func=func
#
#     #扩展功能
#     def __call__(self,*args,**kwargs):
#         """
#         __call__函数：实例化对象()
#         :return:
#         """
#         start = time.time()
#         # 原来功能
#         self._func()  # 原来功能
#         end = time.time()
#         cost = end - start
#         print(f"统计函数总共耗时{cost}秒1")
#
#
# @A
# def welcome_vip():
#     """被装饰器函数"""
#     print("欢迎来到码尚学院VIP课堂")
#
# welcome_vip()


# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用都将被调用的函数名写入文件

def write_log(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        with open('log.txt',mode='a+',encoding='utf-8') as f:
            f.write(func.__name__+'\n')
    return wrapper
@write_log
def fun1(a, b):
    print(f'{a}+{b}={a + b}')
    return a+b

@write_log
def fun2(a, b):
    print(f'{a}*{b}={a * b}')
    return a * b

    # raise Exception('自己加的报错！！')

fun1(1,2)
fun2(3,4)


