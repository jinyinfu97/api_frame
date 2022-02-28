# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/17
# @Email:2155896749@qq.com
# @File: 嵌套循环.py

# *
# **
# ***
# ****
# *****
print("打印三角形")
for i  in range(1,6):
    #循环体里面----》重复做某件事情：1 * 2 * *   ----》n n**
    for x in range(1,i+1):
        print('*',end="")
    print()
print("打印完成")