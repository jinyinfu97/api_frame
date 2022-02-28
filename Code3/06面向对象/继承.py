# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/28
# @Email:2155896749@qq.com
# @File: 继承.py
"""
面向对象的四大特征：封装  继承 重载  多态
继承：子类可以共用父类的属性及方法（子承父业  女儿像爸爸）
子类（派生类）：猫类
父类(基类): 动物类
继承应用场景：两个或者多个类之间存在有相同的属性及方法
继承：实现代码的重用，相同的代码不需要重复的写
子类继承父类及父类的父类的属性和方法---》私有属性及私有方法除外
继承：
单继承：子类只有一个父类
多继承：子类有多个父类  子类A(B,C,D)
就近原则   先找自己类，如果没有对应的属性及方法，从左到右依次往上调用

"""
# 父类
class  Anmail:

    color="yellow"
    __weight=5

    def __private(self):
        print("这是一个私有方法")

    def eat(self):
        print("体重:",self.__weight)
        print("*****.....我饿了！！！！")

    def speak(self):
        pass

class tiger:
    def eat(self):
        print("老虎在吃东西!!!!")

# 子类 Cat(父类)
class Cat(Anmail,tiger):
    pass

    def huangzhuang(self):
        print(self.color)  #调用父类的属性  yellow
        # print(self.__weight)   #子类不能调用父类的私有属性及私有方法
        # self.__private()
        self.eat()

    # 对父类的eat()方法的重构
    # def eat(self):
    #     print("喵喵喵喵.....我饿了！！！！")

jiafeim=Cat()
jiafeim.eat()
print(jiafeim.color)
# jiafeim.__private()
print("子类都是可以调用父类的属性及方法")
jiafeim.huangzhuang()

"""
重载：重构  实现功能的扩展
"""
