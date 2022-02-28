# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/17
# @Email:2155896749@qq.com
# @File: 函数参数类型.py

# 必需参数

def info1(name,age):
    print(f"欢迎{name}来到码尚学院VIP课堂，姓名：{name}，年龄：{age}")

# 调用函数
name="Dong"
age=18
info1(name,age)   #必需参数

def info2(name:str,age:int,classname,adress,score):
    print(f"欢迎{name}来到码尚学院VIP课堂，姓名：{name}，"
          f"年龄：{age},其他信息({classname},{adress}{score})")
classname="M211"
adress="深圳"
score="100"
info2(name,age,classname,adress,score)   #必需参数  按照定义顺序定义参数个数
# 关键字参数    不按顺序传参
# 允许函数调用时参数顺序与声明不一致
info2(adress="北京",age=19,classname="M210",name="九头蛇",score="60")
# 默认参数   定义+调用函数
# 定义函数时进行默认值赋值

def info3(name:str,age:int,adress,score,classname="M211"):
    print(f"欢迎{name}来到码尚学院VIP课堂，姓名：{name}，"
          f"年龄：{age},其他信息({classname},{adress}{score})")
# 调用
# 设置默认值函数  是否可以通过关键字参数进行调用或者必需参数调用   可以
#默认参数函数  默认参数可以不赋值   则取默认值
info3(name,age,adress,score)
# 默认参数能否赋值  可以     调用方式  基于必需参数  关键字参数
info2(adress="北京",age=19,classname="M21O",name="笑褒",score="100")

# 不定长参数：你可能需要一个函数能处理比当初生命是更多的参数，
# 这些参数叫做不定长参数
# 有这么几种形式
# *参数----》把多个参数基于元组方式进行存储
# **参数----》把多个参数基于字典方式进行存储
# *单独出现   后面的参数通过关键字传参
# 实现求几个数的和   几个数？  ---没法确定
def sum(a,b):
    return  a+b

# 求和方法  2/3,4,5,6...个数之和
def sum(*num):
    print(num)   #num元素就是每个参数值
    print(type(num))   #元组
    # 求和操作
    sum=0
    for x in num:
        sum+=x
    print(sum)
    return sum
    # pass  #空语句
sum(2,3)
sum(2,3,4,5,7,65,90)

def sum2(**num):
    print(num)
    print(type(num))

sum2(a=1,b=2,c=3,d=4,e=5)

def sum3(num1,num2,*,num3):
    return num2+num1+num3
print(sum3(1,2,num3=3))












