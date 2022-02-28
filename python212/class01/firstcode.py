# -*- coding=utf-8 -*-
# @time:2021/9/7
# @phone:15874198829
# @author:码尚教育_星瑶

"""
1、同一行显示多条语句，则每条语句后面用；隔开
2、print函数：自动化换行输出 等同于 print(字符2,字符2,字符3,....,end='\n')
print可以有多个参数
如何不换行输出？
print(字符1,字符2,字符3,....,end='')
"""
print("欢迎大家加入码尚教育Python自动化测试",end='\n')

print("欢迎刘荣安",",野马","加入码尚教育Python自动化测试")

isOver=True
if isOver:
    print("开始跳槽涨薪了")
    print("涨薪9.3k")
else:
    print("继续学习，加油~~~")

# 导入
# import module2
# print("212期班级人数：",module2.class212_num)
# module2.learn_01()

"""导入某个模块具体某个函数及数据"""
# from module2 import class212_num,learn_01
# print(class212_num)
# learn_01()

"""导入某个模块具体所有函数及数据"""
# from module2 import *
#
# print(class212_num)
# learn_01()
# learn_02()

# from module2 import learn_01 as d1learn1
# d1learn1()

# from class02.module3 import learn_01
# learn_01()

# import class02.module3
# class02.module3.learn_01()

from class02 import module3
module3.learn_01()










