# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/19
# @Email:2155896749@qq.com
# @File: 函数嵌套.py

# 调用嵌套
def a():
    print("hello a")
def b():
    print("hello b")
    a()
b()

# 定义嵌套
def A():
    print("hello A")
    def B():
        print("hello B")
    B()
A()
def login():
    pass
def f2():
    login()
    # @实现功能1

def f3():
    login()
    # @实现功能2


# 放入购物车：先登录-实现功能1
# 立即购买：先登录-实现功能2