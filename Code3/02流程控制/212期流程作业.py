import random

# 1、打印如下结果：
# 1*5=5
# 2*10=20
# 3*15=45
# ...
# 10*50=500
# for i in range(1,11):
#     print(str(i)+"*"+str(5*i)+"="+str(i*5*i))

# 2、本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
# sum = 0
# num = 10000
# for i in range(1,6):
#     sum = num*(1+3/1000)**i
#     print(f"第{i}年：{sum}")
# print("5年后：", sum)

# 3、计算1900年1月1日到今天(如：2019年12月20日)相距多少天。

# 4、打印如下图案：
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     print("*"*i)

# 5、打印如下图案：
# *
# ***
# *****
# *******
# *********
# for i in range(1,6):
#     print("*"*(2*i-1))

# 6、打印如下图案：
# #####*
# ####***
# ###*****
# ##*******
# #*********
# for i in range(1,6):
#     print("#"*(6-i),end='')
#     print("*"*i)

# 7、打印如下图案：
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *

#
# for i in range(0, 5):
#     print(" " * (4 - i) + "*" * (2 * i + 1) + " " * (4 - i))
# for n in range(0, 4)[::-1]:
#     print(" " * (4 - n) + "*" * (2 * n + 1) + " " * (4 - n))

# 8、打印99乘法表
# for i in range(1, 10):
#     for n in range(1, i + 1):
#         print(f"{n}*{i}={n * i}", end=' ')
#     print()


# 9、定义一个List，任意输入10个数字保存到List，然后按从小到大排序。（冒泡排序）
def sortlist(newlist):
    for i in range(len(newlist)):
        for j in range(len(newlist) - i - 1):
            if newlist[j] > newlist[j + 1]:
                newlist[j], newlist[j + 1] = newlist[j + 1], newlist[j]
    print(newlist)


list1 = []
for randomnum in range(0, 10):
    list1.append(random.randint(1, 1200))
sortlist(list1)
del list1
