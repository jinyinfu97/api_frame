# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/14
# @Email:2155896749@qq.com
# @File: python运算符.py
"""
# python常见运算符
算术运算符：+、-、*、/、//、%、**
比较（关系）运算符：==、！=、>、>=、<=

"""

# =   赋值
# ==  比较运算符  结果：True False
if 1==2 or 1==3 :
    print("对")
else:
    print("错")
sum=0
# sum=sum+1
sum+=1
sum-=1
print(sum)

print(0 and 1)
print(0 or 1)
print(not 1)
num1=1
num2=1
print(id(num1))
print(id(num2))
a=1
print(id(a))

score=input("请输入你的成绩:")
print("我的成绩:",score)
print(type(score))


