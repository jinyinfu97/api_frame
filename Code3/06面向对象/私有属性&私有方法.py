# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/26
# @Email:2155896749@qq.com
# @File: 私有属性&私有方法.py

class people:
    """描述一个中国人类"""
    fuse="yellow"    #类属性1
    language = "chain"  # 类属性2
    __weight=90

    # 构造方法---》名字特殊 __init__  调用特殊：实例化时调用
    # 什么时候会重构构造方法---》初始化数据
    def __init__(self,name,classname):
        print(f"实例化了一个对象，她的名称{name}，班级{classname}")
        self.name=name   #实例属性：实例对象自己私有。---》self.name   self.classname
        self.classname=classname

    def __speakmimi(self):
        print("这是一个私有方法")


    # 定义行为？ 说话 睡觉
    def speak(self):
        print(self,type(self))
        print("我说就是中国话")
        print("告诉一个秘密，我的体重是:", self.__weight)
        self.__speakmimi()

xingji=people("xingji","M211")
# print(xingji.__weight)
xingji.speak()
# print(xingji.__weight)
# xingji.__speakmimi

print("私有属性及私有方法只能类内部使用，实例对象或类不可以在外部使用，"
      "但是可以通过此种格式调用：对象._类名+私有属性/私有方法")

print("1外部获取私有属性",xingji._people__weight)
print("2外部获取私有方法：")
xingji._people__speakmimi()
