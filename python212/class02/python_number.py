# -*- coding=utf-8 -*-
# @time:2021/9/9
# @phone:15874198829
# @author:码尚教育_星瑶
import math

num_212class=180

# 查看变量类型
print(type(num_212class))
print(num_212class)
zx=9.3
print(type(zx))
print(zx)
# 判断变量是否为某个数据类型，如果是指定某个类型则返回True,否则返回False
print(isinstance(num_212class,int))

"""
//  商不一定取整数，它与除数的类型有关系
/
a**b  a的b次幂  
"""
num3=3**4
print(num3)
num1=8/3
print(num1)
num2=8//3
print(num2)
num4=8//3.00
print(num4)
ys=8%3
print("余数：",ys)

value1=math.floor(5.6)
value2=math.ceil(4.01)
print(value1,value2)

num5=45.89
value3=round(num5)
print(value3)





