# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/19
# @Email:2155896749@qq.com
# @File: 递归函数.py

# 7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
# 要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，
# exit代表退出学生管理系统。每一个功能定义一个自定义函数。界面如下：
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
    delname = input("请输入需要修改人的姓名")
    if mylist.count(delname) > 0:
        mylist.remove(delname)
    else:
        print("T666班没有这个学员没有此学员")
    print(mylist)


def change():
    pass


def select():
    pass


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

# 1、封装函数   业务切割多个函数   函数与函数进行独立
# 2、实现循环不同操作，----》实现不同操作封装函数 ----》递归函数
