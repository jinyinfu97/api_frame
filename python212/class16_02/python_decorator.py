# -*- coding=utf-8 -*-
# @time:2021/11/2
# @phone:15874198829
# @author:码尚教育_星瑶
"""
一、什么是python装饰器
    python装饰器（函数）：装饰函数或者类，对函数或类进行功能的扩展
    标记符号：@函数名称
    python装饰器：函数装饰器和类装饰器
    装饰器的使用场景：
    鉴权
    日志
    pytest
    unittest

二、什么是函数装饰器及定义
    需求：统计每个函数的运行时间

三、类装饰器+反射   加一节课
"""
import time

#装饰器函数的应用场景
def runTime(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        #执行原来函数的功能
        try:
            func(*args,**kwargs)
            info="无异常"
        except Exception as error:
            errorinfo="有异常，异常信息"+str(error)
        #执行扩展功能
        time.sleep(1)
        end_time = time.time()
        const = end_time - start_time
        print(f"统计{func.__name__}函数运行耗时{const}秒")
    return wrapper

@runTime
def  welcome_vip():
    print("欢迎来到码尚教育VIP课堂")


def function2():
    print("执行函数2代码")


def function3():
    print("执行函数3代码")


def function4(a,b):
    sum=0
    sum=a+b
    print(f"执行函数4代码,a+b={sum}")


def function5(a,b,c):
    try:
        sum=0
        sum=a+b+c
        print(f"执行函数5代码,a+b+c={sum}")
        #写日志 info基本日志   function5  成功执行
    except:
        pass
        # 写日志 error基本日志   function5  执行失败，异常信息****


#不加装饰器
welcome_vip=runTime(welcome_vip)     #等同@runTime
welcome_vip()


#加装饰器
welcome_vip()
print("---------------------------------------------")
""""装饰器带参数:实质外面再包裹一个函数"""
def demo(name):

    def runTime(func):
        def wrapper(*args,**kwargs):
            start_time = time.time()
            #执行原来函数的功能
            try:
                func(*args,**kwargs)
                info="无异常"
            except Exception as error:
                errorinfo="有异常，异常信息"+str(error)
            #执行扩展功能
            time.sleep(1)
            end_time = time.time()
            const = end_time - start_time
            print(f"统计{func.__name__}函数运行耗时{const}秒")
            print(name)

        return wrapper
    return runTime

@demo('xingyao')
def test():
    print("执行test函数")


test()