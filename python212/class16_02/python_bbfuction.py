# -*- coding=utf-8 -*-
# @time:2021/11/2
# @phone:15874198829
# @author:码尚教育_星瑶
"""
1、什么是闭包函数
 一个函数的返回值是另外一个函数，返回的函数调用父函数内部的其他变量，
 如果返回的函数在外部被执行，就产生了闭包
2、闭包函数的意义及作用
    作用：使函数外部能够调用函数内部定义的变量
3、闭包函数优缺点：
    优点：内部函数和局部变量都可以在外部使用
    缺点：闭包操作导致整个函数的内部环境，被长久保存，占用大量的内存

装饰器实质就是一个闭包函数
"""
"""闭包函数表示形式1   内部函数的局部变量可以在外部访问"""
name1="python2"
def fun1():
    name2='python3'
    def inner():
        print(name2)
    return inner
print(name1)
result=fun1()
print(type(result))
# 执行返回函数
result()

"""闭包函数表示形式2  内部函数可以通过外部访问"""
def fun2():
    name2='python3'
    def inner():
        print("执行内置函数inner")
    def all():
        return inner
    return all

result=fun2()
fuc=result()
print("内部函数可以通过外部访问",type(fuc))
fuc()


