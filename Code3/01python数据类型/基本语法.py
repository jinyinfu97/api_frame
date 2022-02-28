# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/7
# @Email:2155896749@qq.com
# @File: 基本语法.py
import keyword

print("欢迎来到码尚学院VIP课堂")
'''
标识符规则：

'''
# 查看Python关键字
print(keyword.kwlist)
# False=1
# .py文件----》模块   模块名遵守标识符命名规则，同时尽量不要跟第三方模块名同名
'''
注释作用：提高代码可读性和可维护性
python注释有哪些？
1、单行注释  #  快捷键 ctrl+/
2、多行注释    选择多行+快捷键 ctrl+/    或者   """""" 或者  ''''''

行与缩进 
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数

多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句

同一行显示多条语句   分号(;)分割
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割。
比如：print("hello world"); print("hello cema")

print函数默认会换行，并且可以输出多个内容
不换行输出怎么办？


'''
score=80
print("恭喜获取本期奖学金")
print("受到惩罚")
print("assssssssssssssssssss")
item_one=10
item_two=20
item_three=30
item_4=30
item_5=30
item_6=30
total = item_one +\
        item_two +\
        item_three+\
        item_4+\
        item_5+\
        item_6
print(total);print("hello world");print("hello world");print("hello world")
print("hello world")
print("hello world")


'''
print函数默认会换行，并且可以输出多个内容
不换行输出怎么办？  end=" "
print("cn","czj","此行路远....",end=" ")
'''
print("cn","czj","此行路远....",end=" ")
print("欢迎来到码尚学院VIP课堂")

"""
代码组/子句
具有相同缩进的一组语句叫代码组
比如：if/while/for/def/class ,首行以关键字开始，以：结束，那么该行后面的一行或多行为代码组，首行及后面的代码块就是子句
"""

if True:
    print("欢迎来到码尚学院VIP课堂")
else:
    print("欢迎来到码尚学院Vip试听课堂")

hello_str="欢迎来到码尚学院VIP课堂"






