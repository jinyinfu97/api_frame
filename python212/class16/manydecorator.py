# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/15
# @Email:2155896749@qq.com
# @File: manydecorator.py

"""
函数可以有多个装饰器函数
注意：
多个装饰器函数执行顺序是：
    从里到外（就近原则）

"""
def a(func):
    def wrapper(*args,**kwargs):
        func(*args, **kwargs)
        print("aaaaaa")
    return wrapper

def b(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print("bbbbbb")
    return wrapper

def c(func):
    def wrapper(*args,**kwargs):
        func(*args, **kwargs)
        print("ccccccc")
    return wrapper

@c
@b
@a
def welcome_vip():
    """被装饰器函数"""
    print("欢迎来到码尚学院VIP课堂")

welcome_vip()