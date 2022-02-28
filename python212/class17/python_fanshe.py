# -*- coding=utf-8 -*-
# @time:2021/11/4
# @phone:15874198829
# @author:码尚教育_星瑶
"""
一、什么是反射
把字符串映射到实例的变量或实例的方法,然后可以去进行执行调用、修改

反射的本质（核心）：利用字符串的形式去操作对象/模块中成员（方法/属性）
基于字符串的事件驱动

二、反射四个重要的方法
1、getattr 获取对象属性/对象方法
2、hasattr 判断对象是否有对应的属性及方法
3、delattr  删除指定的属性
4、setattr 为对象设置内容

"""
class TestObj:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def test(self):
        print("执行test方法")

def a():
    print("类外部方法")

if __name__ == '__main__':
    """1、getattr 获取对象属性/对象方法"""
    xiaoyu=TestObj('小宇',18)
    # print(xiaoyu.name)
    # xiaoyu.test()
    #获取对象的属性
    print(getattr(xiaoyu,"name"))
    # 执行对象的方法
    result=getattr(xiaoyu, "test")
    print(type(result))
    result()
    """2、hasattr 判断对象是否有对应的属性及方法"""
    if hasattr(xiaoyu,"adress"):
         print(getattr(xiaoyu,"adress"))
    if hasattr(xiaoyu,"test"):
         print(getattr(xiaoyu,"test"))
    """4、setattr 为对象设置内容"""
    #修改属性的值
    setattr(xiaoyu,"name","winnie")
    print(getattr(xiaoyu, "name"))
    #修改方法
    setattr(xiaoyu,"test1",a)
    getattr(xiaoyu,"test1")()

    xiaoyu.test1()

