# 1.写函数，接收两个数字参数，返回最大值
# 例如：
# 传入：10,20
# 返回：20
# def getmax(a,b):
#     print(max(a,b))
# getmax(1,4)

# 2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
# 例如：
# 传入：[34,23,52,352,352,3523,5]
# 返回：[23,352,3523]
# d=[]
# def list(a):
#     for index in range(len(a)):
#         b = index*2+1
#         if b<len(a):
#             c=a[b]
#             d.append(c)
#     print(d)
# list([34,23,52,352,352,3523,5,1,2,3,4])

# 3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
# 传入2：[34,23,52]     				返回2：[34,23,52]
# def list(a):
#     newlist = []
#     if len(a)>5:
#         for i in range(0,5):
#             newlist.append(a[i])
#         print(newlist)
#     else:
#         print(a)
# list([34,23,52,352,666,3523,5])
# list([34,23,52])

# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# 例如：
# 传入："hello world"
# 返回：True
# def checkisnull(a):
#     if " " in a:
#         print("True")
#     else:
#         print("False")
# checkisnull("helloworld")

# 5.写函数，接收n个数字，求这些数字的和
# def getsum(num1,*numbern):
#     sum=0
#     sum+=num1
#     for x in numbern:
#         sum+=x
#     return sum
# print(getsum(1,2,2,2,2,2))

# 6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
# 例如：
# 传入：10,*,20
# 返回：200
def cal(a,b,c):
    if b == "+":
        # print(a + b)
        print (str(a) + "+" + str(c) + "=" + str(a + c))
    elif b == "-":
        print(str(a) + "-" + str(c) + "=" + str(a - c))
    elif b == "*":
        print(str(a) + "*" + str(c) + "=" + str(a * c))
    elif b == "/":
        print(str(a) + "/" + str(c) + "=" + str(a / c))
    else:
        print("不是四则运算")
cal(1,"/",3)

# 7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
# 要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。每一个功能定义一个自定义函数。界面如下：
# 系统界面如下：
# -----------------------欢迎进入T666班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统
# (0)输入0后效果如下：
# 	0
# 	["郭易","汤碗珍"..]
# (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：张三
# 	["郭易","汤碗珍",'张三'..]
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：张三
# 	["郭易","汤碗珍"..]
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：张三
# 	请输入需要修改后的姓名：李四
# 	["郭易","汤碗珍",'李四'..]
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	请输入查询人的姓名：张三
# 	郭易在座位号(3<下标>)的位置。
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用T666的学生管理系统，下次再见。
def all_info():
    # 展示所有学员信息
    print(mylist)


def add(mylist):
    '''添加学员信息'''
    mylist.append(input("请输入增加人的姓名"))
    print(mylist)


def delete():
    delname = input("请输入需要删除人的姓名")
    if mylist.count(delname) > 0:
        mylist.remove(delname)
    else:
        print("T666班没有这个学员没有此学员")
    print(mylist)


def change():
    changename = input("请输入需要修改人的姓名")
    if mylist.count(changename) >0:
        mylist.remove(changename)
        mylist.append(input("请输入需要修改后的姓名:"))
    else:
        print("T666班没有这个学员没有此学员")
    print(mylist)
def select():
    selname = input("请输入需要查询人的姓名")
    if mylist.count(selname) > 0:
        print(selname + "在座位号" + str(mylist.index(selname)) + "的位置。")
        # for index in range(len(mylist)):
        #   if mylist[index] == selname:
        #     a = index
        # print(selname + "在座位号" + str(a) + "的位置。")
    else:
        print("T666班没有这个学员没有此学员")
    print(mylist)

def caozuo(nr, mylist):
    if nr == "exit":
        print("欢迎使用T666的学生管理系统，下次再见。")
    else:
        # 执行对应的操作
        if nr == '0':
            all_info()
        elif nr == "1":
            add(mylist)
        elif nr == "2":
            delete()
        elif nr == "3":
            change()
        elif nr == "4":
            select()
        else:
            print("输入有误！！！")
        caozuo(input(message), mylist)


message = """
-----------------------欢迎进入T666班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统
"""
mylist = ["Baby", "Ginkgo"]
caozuo(input(message), mylist)