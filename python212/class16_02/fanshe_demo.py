# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/15
# @Email:2155896749@qq.com
# @File: fanshe_demo.py

#实现反射实现登录、退出、注销-----》关键字驱动
# excel ---> open_brower   close  click  input

class mashang:

    def login(self):
        print("正在登录.....")

    def loginout(self):
        print("正在退出.....")

    def register(self):
        print("正在注册.....")


    def run(self):
        """
        1 login
        2、loginout
        3、register
        :return:
        """
        fucslist=["login","loginout","register"]
        num=int(input("请你输入操作数字:"))
        methods=fucslist[num-1]
        action=getattr(self,methods)
        action()

if __name__ == '__main__':
    mashang().run()