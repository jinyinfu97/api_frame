# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/26
# @Email:2155896749@qq.com
# @File: modelA.py

class people:

    def speak(self):
        # self  类的实例
        print("这是实例方法")

    @staticmethod
    def static_method():
        print("这是一个静态方法")

    @classmethod
    def  class_method(cls):
        # 参数  cls  ---》类本身
        print("这是一个类方法")



"""
假设我有一个学生类和一个班级类，想要实现的功能为：
    执行班级人数增加的操作、获得班级的总人数；
    学生类继承自班级类，每实例化一个学生，班级人数都能增加；
    最后，我想定义一些学生，获得班级中的总人数。

"""
# 人员增加 ---》方法   实例方法    类方法   静态方法   否定：内置方法  私有方法
#
# class  TestClass:
#
#     # 属性班级人数
#     num=0
#
#     # 人员增加
#     @classmethod
#     def addNum(cls):
#         cls.num+=1
#
#     def __init__(self):
#         TestClass.addNum()
#
#     @classmethod
#     def getNum(cls):
#         return cls.num
#
#     @staticmethod
#     def getNum1():
#         return  TestClass.num
#
#
# class Student(TestClass):
#     pass
# # 实例化对象  人数增加一 ---》什么时候调用这个方法addNum
# a=Student()
# b=Student()
# c=Student()
# d=Student()
# num=TestClass.getNum1()
# print("班级人数：",num)

# main()方法
if __name__ == '__main__':
    a = people()
    a.speak()
    print("调试当前模块的代码....  执行main方法代码")
