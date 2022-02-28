# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/25
# @Email:2155896749@qq.com
# @File: demo.py


class people:
    """描述一个中国人类"""
    fuse="yellow"    #类属性1
    language = "chain"  # 类属性2

    # 构造方法---》名字特殊 __init__  调用特殊：实例化时调用
    # 什么时候会重构构造方法---》初始化数据
    def __init__(self,name,classname):
        print(f"实例化了一个对象，她的名称{name}，班级{classname}")
        self.name=name   #实例属性：实例对象自己私有。---》self.name   self.classname
        self.classname=classname


    # 定义行为？ 说话 睡觉
    def speak(self):
        print(self,type(self))
        print("我说就是中国话")

    def __str__(self):
        return "实例化一个对象"



    def __getattribute__(self, item):
        print("执行内置函数__getattribute__")
        if item=="name":
            return self.name

DD=people("dd","M211")
print(DD.fuse)
