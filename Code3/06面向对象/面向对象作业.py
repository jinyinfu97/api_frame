# 一、定义名为MyTime的类，其中应有三个实例变量 时hour 分minute 秒second
# 1）为了给对象初始化赋值，编写构造方法，对时分秒附初始值
# 2）为了保证数据的安全性，这三个成员变量应声明为私有、
# 3）对三个属性分别定义封装get和set方法，定义一个main方法，创建一个MyTime类的对象并调用这六个方法。
class MyTime:
    def __init__(self,h,m,s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def set__hore(self,h):
        self.__hour = h

    def set__minute(self,m):
        self.__minute = m

    def set__second(self,s):
        self.__second = s

    def get__hore(self):
        return self.__hour

    def get__minute(self):
        return self.__minute

    def get__second(self):
        return self.__second


if __name__ == '__main__':
    mt = MyTime(9,51,30);
    print(mt._MyTime__hour,mt._MyTime__minute,mt._MyTime__second);
    mt.set__hore(10)
    print(mt.get__hore())
    mt.set__minute(30)
    print(mt.get__minute())
    mt.set__second(59)
    print(mt.get__second())



# 二、为"无名的粉"写一个类WuMingFen，有三个属性 面码:String theMa  粉的分量(两) int quantity  是否带汤 boolean likeSoup
# 要求：
# 1）写一个构造方法 分别给三个属性赋值。构造出一个WuMingFen类的对象(酸辣面码、2两、带汤)，
# 2）写一个普通方法check()打印对象的三个属性。通过对象调用此方法。
class WuMingFen:
    def __init__(self,t,q,l):
        self.theMa = t
        self.quantity = q
        self.likeSoup = l

    def check(self):
        print(self.theMa,self.quantity,self.likeSoup);

wmf=WuMingFen("酸辣面码","2两","带汤")
wmf.check()
