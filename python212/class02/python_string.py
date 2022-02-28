# -*- coding=utf-8 -*-
# @time:2021/9/9
# @phone:15874198829
# @author:码尚教育_星瑶
"""
string类型
"""


str1='欢迎大家加入码尚教育VIP课堂'
str2="哈哈"
str3="""MS221_NN"""
str4='''MS221_NN'''
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))


"""根据索引区间取值"""
print("学号：",str3[0:5])
# 字符串最后的一个字符
print(str3[-1])
# 倒数第二
print(str1[-2])
print(str1[-3])
# 从某个位置开始取到末尾
print(str3[1:])
# 隔一个字符从左往右取值
print(str3[0::2])

str4="""MS221_NN"""
print(str4[-1::-2])
print(str4[::-2])

print(str4[::])

"""
特殊字符原字符输出
方式一：通过转义字符 \
方式二：字符前加r/R
"""
str5=R'\n'
str6=r'\n'
print(str5,str6)
print("1111")


"""
Python常用的运算符
+  字符串的拼接
* 复制   复制2   *2
in     成员判断
not in 
"""
str7="abc"
str8="edfg"
print(str7*3)
print('a' not  in str7)

"""
字符串格式化
格式化方式一：
%s 字符串占位符
%d  整数占位符
%u  无符号整型
%f  浮点数字
方式二：
"""
name="就这"
age=18
print("欢迎"+name+",工作年限："+str(age))

print("格式化方式一：欢迎 %s,工作年限：%d"%(name,age))

# 格式化第二种方式
str9="格式化方式二：欢迎{1},工作年限：{0}".format(age,name)
print(str9)

# 格式化第三方式
str10=f"格式化方式三：欢迎{name},工作年限：{age}"
print(str10)





