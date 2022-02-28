# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/14
# @Email:2155896749@qq.com
# @File: for循环语句.py

"""
 for 变量  in 序列：
 	执行语句1
 else:
 	执行语句2

运行逻辑：
遍历序列（元组，列表，字典，字符串）中所有元素，每次遍历都会执行语句1

"""
# 求和:1+2+3+4+4+...+100  ---》for    1+2+3...+10
# range(n,m)  返回n~m整数列表，含头不含尾返回列表中包含n,不会包含m
sum=0
for x in range(1,101):
    # sum=sum+x
    sum+=x
print("1+2+3+....+100=",sum)

list1=[1,2,3]
list2=["a","b","c"]

# 跳出循环体  break
# 跳出本次循环 continune
# pass  空语句  占位语句 作用确保程序结构的完整性

for  x in range(1,11):
    if x<=5:
        continue  #跳出本次循环
    print(x)
        # break   #跳出整个循环






