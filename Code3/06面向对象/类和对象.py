# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/24
# @Email:2155896749@qq.com
# @File: 类和对象.py
"""
# 定义类  中国人
class 类名:
    # 属性
    # 方法
"""
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

# DD    类的实例化---》对象
# 初始化数据  名称：DD  班级：211
DD=people("DD","211")
DD.speak()
print("获取DD同学的特征",DD.language,DD.fuse)

# hefan  对象
hefan=people("hefan","210")
# 初始化数据  名称：hefan  班级：210
hefan.speak()
print("获取hefan同学的特征",hefan.language,hefan.fuse)
# 类属性： fuse="yellow"    #类属性1
#     language = "chain"  # 类属性2
print("类属性可以通过对象或类来获取：",people.fuse,DD.fuse)
print("类属性可以通过对象或类来获取：",people.language,hefan.fuse)
# 实例属性
print("实例属性只能通过对象来调用:",hefan.name)
# print("实例属性不同通过类去获取：",people.name)
# 内置属性 底层每个类都有的这些数据，不同的内置属性存储不同的数据
print(people.__doc__)
print(people.__name__)
print(people.__module__)

