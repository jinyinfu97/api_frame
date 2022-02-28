# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/10
# @Email:2155896749@qq.com
# @File: string类型.py

# 定义string
str1="hello world"
str1_hello='hello world'
str2_hello='''hello world'''
print(type(str1))
print(type(str1_hello))
print(type(str2_hello))

# 截图字符串中的某个字符或者部分字符---切片
"""
string类型  不可变数据
语法格式：变量[start：end：step]     特别注意规则：  含头不含尾 左闭右开
start:开始索引值 索引值从左到右 从0开始  索引值从右到左，从-1开始
end：结束索引值
step：步长  默认是1
"""
str_num="123456789"
# 取单字符   字符串中第二个字符
print(str_num[1])
# 取单字符   字符串中倒数第二个字符
print("字符串中倒数第二个字符:",str_num[-2])
# 取多个字符   从开始位置截图长度为3对应的字符串   h e l  0:3
print(" 从开始位置截图长度为3对应的字符串:",str_num[0:3])
# 取从第三个字符开始，截取后面所有字符
print("取从第三个字符开始，截取后面所有字符:",str_num[2:])
# 截取前六个字符
print("截取前六个字符:",str_num[0:6])
print("截取前六个字符:",str_num[:6])
# 步长为1
print(str_num[::2])
# 字符串反转  从右到左
print("字符串反转:",str_num[::-1])

# 字符串更新  + 拼接
name="Baby"
print("name物理位置",id(name))
name=name+"01"
print(name)

# \n  " ' \ \t  特殊符号
print("1111\n2222")
# 原符号输出   前面\(转义) 特殊符号
print("1111\\n\"\'2222\\")
print(r"1111\n'\"2222")
print(R"1111\n'\"2222")
print(r"E:\VIP\PPT\Python基础")
print(R"E:\VIP\PPT\Python基础")
print("E:/VIP/PPT/Python基础")
# 特殊符号 进行特定场景输出
# print("1111\n2222")

"""
字符串格式化
"""
# 字符串格式表示方式一
print("%s[%s期，工作年限：%d],欢迎来到码尚学院VIP课堂"%("大雨","M211",3))

# 字符串格式表示方式二
print("{1}[{0}期，工作年限：{2}],欢迎来到码尚学院VIP课堂".format("大雨","M211",3))
# 字符串格式表示方式三  f  字面量格式化
name="大雨"
q="M211"
year="2"
print(f"{name}[{q}期，工作年限：{year}],欢迎来到码尚学院VIP课堂")

"""
字符串常见函数
"""
str8="123456789"
print(str8.strip(),str8.capitalize())
# strip() / lstrip() / rstrip()
# 去空格
# format()
# 字符串格式化
# capitalize() / upper() / ower()
# 大小写转换
# max() / min()

# join(seq)
# 以指定的分隔符把seq中的元素合并成一个新字符串  join  加入---某个规则符号+合并
join_str="helloworld"
new_str="-".join(join_str)
print(new_str)

# split()
# 通过分隔符截取字符串  通过分隔符，返回列表数据
names="hefan;大雨;志大叔"
namel=names.split(";")
print(namel,type(namel))

# replace(原字符, 新字符)
# 替换字符串
str_old="1234567"
new_str=str_old.replace("123","000")
print(new_str)

# find(查找字符, 开始索引，结束索引值)查找字符串，找到返回开始索引值，没有找到返回-1
ss_str="12345678"
print(ss_str.find("8"))
# index  -->find区别在于，index如果没有找到则报错
ss_str="12345678888"
print(ss_str.index("8"))

# count(查询字符, 开始索引，结束索引值) 返回某个字符在指定范围出现次数
print(ss_str.count("0"))
# startswith(匹配字符, 开始索引，结束索引值)  判断是否以某个字符开头
print(ss_str.startswith("123"))
# endswith(匹配字符, 开始索引，结束索引值)  判断是否以某个字符结尾
print(ss_str.endswith("123"))

