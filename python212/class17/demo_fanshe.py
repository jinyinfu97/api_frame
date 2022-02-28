# -*- coding=utf-8 -*-
# @time:2021/11/4
# @phone:15874198829
# @author:码尚教育_星瑶
"""
去实现某个业务，定义类，类里面封装很多方法，提供一个统一的入口能够调用各种方法
业务：登录  退出  注销 注册

"""
class test:
    funclist=["login","loginout","rigister","delete"]

    def login(self):
        print("这是登录")

    def loginout(self):
        print("这是退出")


    def rigister(self):
        print("这是退出")

    def delete(self):
        print("注销")

    def aaa(self):
        pass

    #1 login 2  loginout 3 rigister  4 delete
    def run(self,num):
        getattr(self,self.funclist[num-1])()

# obj=test()
# num=int(input("1 login 2  loginout 3 rigister  4 delete 请输入你操作的数字："))
# obj.run(num)

str1='3*7'
print(eval(str1))



