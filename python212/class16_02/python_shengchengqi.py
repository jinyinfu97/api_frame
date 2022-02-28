# -*- coding=utf-8 -*-
# @time:2021/11/2
# @phone:15874198829
# @author:码尚教育_星瑶
"""
一、什么是生成器
    函数中包含yield，这样的函数叫做生成器
    普通函数和包含yield函数（生成器）的区别：
    生成器返回迭代器的函数，生成器就是迭代器
执行规则：
生成器运行时，每次遇到yield时函数会暂停并保存当前所有运行信息，
返回yeild值，并在下一次迭代（next()）的时候从当前位置继续执行


二、什么是迭代器？
迭代器访问结合元素的一种方式，迭代器只能往前不能往后退
字符串、列表、元组都是可以创造成迭代器
[1,2,3,4,5]
迭代器有两个基本的方法：iter()  next()

"""
list1=[1,2,3,4,5]
try:
    it=iter(list1)  #创建迭代对象
    print(next(it))   #1
    print(next(it))    #2
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("已经遍历完成")
# for num in it:
#     print(num)


import sys

def fibonacci(n):
    """生成器"""
    a=0
    b=1
    counter =0
    while True:
        if (counter > n):
            return
        yield a

        a,b=b,a+b   #a=0  b=1

        a=b
        b=a+b
        # temp=a
        # a=b
        # b=temp+b
        counter += 1

f = fibonacci(10)    #f是迭代器对象
# 第一遇到yeild  a=0  返回a的值

while True:
    try:
        print(next(f), end=" ")
        #第一遍历执行  next(f)   返回值 a=0 a=1  a=1 a=2  a=3  a=5  a=8
    except StopIteration:
        sys.exit()

