# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/7
# @Email:2155896749@qq.com
# @File: python基本数据类型.py

# 导入python模块  快捷导包: ctrl+alt+空格   或者 alt+回车
import math
# 随机生成数值类型
import random

# 定义number类型
num1=1
num2=2.1
num3=False
print(num1)
# 打印数据类型
print(type(num1),type(num2),type(num3))

print(num1**2)
print(9/2)
# //获取得到与除数类型是一致，不会进行四舍五入，/返回值类型为float
print(9//2.0)
print(abs(num1))
print(" floor(x)返回数字的下舍整数:",math.floor(4.0))
print(" ceil(x)返回数字的上入整数",math.ceil(5.1))
print(" random.random()返回随机生成的一个实数，它在[0,1)范围内:", random.random())
 # random.randint(a,b)返回随机生成一个整数，在a~b之间的整数")
print("random.randint(a,b)返回随机生成一个整数，在a~b之间的整数:", random.randint(100, 200))
# 进行四舍五入
print(round(4.7),round(4.78,1))
# 去掉整数部分 math.trunc
print(math.trunc(4.7))

num5=80.22
# 判断数据类型的第二种方式
print(isinstance(num5,float))   #返回True/False

print(round(4.7),round(4.70,2))
print(round(2.5,1))


