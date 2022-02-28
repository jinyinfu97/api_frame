# _*_ coding:utf-8 _*-
# 1、任意的输入10个数字，按从大到小排序
# list1 =[]
# for i in range(1,11):
#     str1 = int((input("请输入第"+str(i)+"个数字:")))
#     list1.append(str1)
# list1.sort(reverse=True)
# print(list1)


# 2、"在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?”，通过键盘输入小男孩回答的鲜花的束数，数量不一样小女生的反应也不一样。
# 如果鲜花数大于等于9999，打印："小女生直接晕了过去",如果在1000(包含)-9999(不包含)，打印："明天就结婚",如果在100(包含)-1000(不包含)，打印："拉拉手意思意思，有空再约！",否则：打印："你是个好人"
# print("这花多少束？")
# num = int(input("请输入鲜花数量："))
# if num >= 9999:
#     print("小女生直接晕了过去")
# elif 1000 <= num < 9999:
#     print("明天就结婚")
# elif 100 <= num < 1000:
#     print("拉拉手意思意思，有空再约！")
# else:
#     print("你是个好人")

# 3、输入三角形的三条边长，判断三角形的类型。根据实际情况分别打印：不能构成三角形，一般三角形，等腰三角形，等边三角形，只要能构成三角形，则还需要计算出：周长。
# a = float(input("请输入第1条边："))
# b = float(input("请输入第2条边："))
# c = float(input("请输入第3条边："))
# print(bool(a == b == c))
# if a + b > c and b + c > a and a + c > b:
#     if (a == b or b == c or a == c) and bool(a == b == c) is False:
#         print("是等腰三角形")
#         print("周长为" + str(a + b + c))
#     elif a == b == c:
#         print("是等边三角形")
#         print("周长为" + str(a + b + c))
#     print("是一般三角形")
# else:
#     print("不是三角形")

# 4、如果输入三个不同的数，要求比较大小并按从小到大排序输出呢？如输出：a<b<c）
# a = input("第一个数：")
# b = input("第二个数：")
# c = input("第三个数：")
# list = [a,b,c]
# list.sort()
# print(list[0]+"<",list[1]+"<",list[2])

# 5、判断输入的用户名为admin及密码为admin则打印登录成功，否则打印用户名或密码错误，登录失败
# 6、判断输入的数是奇数还是偶数
# 7、用户输入的年份是否为闰年
# 8、输入两个整型变量，分别使用if结构两个中的最小值
# 9、打印如下结果：
# 1*5=5
# 2*10=20
# 3*15=45
# ...
# 10*50=500

# for i in range(1,11):
#     a = 5*int(i)
#     b = a*int(i)
#     print(str(i)+"*"+str(a)+"="+str(a*b))

# 10、本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
# 11、计算1900年1月1日到今天(如：2019年12月20日)相距多少天。
# 12、打印如下图案：
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     print("*"*i)
# print()

# for i in range(1,6):
#     for a in range(1,i+1):
#         print("*",end="")
#     print()

# 13、打印如下图案：
# *
# ***
# *****
# *******
# *********
# for i in range(0,5):
#     print("*"*(2*i+1))
# print()

# 14、打印如下图案：
# #####*
# ####***
# ###*****
# ##*******
# #*********
# for a in range(1,6):
#     print("#"*(6-a)+"*"*(2*a-1))
# print()

# 15、打印如下图案：
#      *
#     ***
#    *****
#   *******
#  *********
#   6*******7
#    7*****5
#     8***3
#      9*1
for i in range(0,9):
    if i<=4:
        print(" "*(4-i)+"*"*(2*i+1))
    else:
        for a in range(1,i-3):
            print(" ",end="")
        for b in range(1,-2*(i-4)+10):
            print("*",end="")
        print()

# 16、打印99乘法表
# 17、定义一个List，任意输入10个数字保存到List，然后按从小到大排序。（冒泡排序）
# lis = []
# for a in range(1,11):
#     number=int(input("请输入一个数字："));
#     lis.append(number);
# for cs in range(len(lis)):
#     for index in range(len(lis)-1):
#         if lis[index]>lis[index+1]:
#             lis[index],lis[index+1]=lis[index+1],lis[index];
# print(lis);
