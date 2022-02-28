# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/26
# @Email:2155896749@qq.com
# @File: 面向对象特征1封装.py
"""
需求：小明爱跑步
	1.小明体重75.0公斤  属性  -->
	2.每次跑步会减肥0.5公斤  行为
	3.每次吃东西体重会增加1公斤  行为
	4.小美的体重是45.0公斤  属性
"""
# 定义一个类来进行表示      小明  小美
class julebu:

    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def eat(self):
        self.weight +=1
        print(f"每次吃东西体重会增加1公斤，你现在的体重{self.weight}")
        pass

    def pao(self):
        self.weight-=0.5
        print("每次跑步会减肥0.5公斤,现在体重",self.weight)


xming=julebu("小明",75)
xming.pao()
xming.eat()
print(xming.weight)
xmei=julebu("小美",45)
xmei.pao()
xmei.pao()
xmei.eat()
print(xmei.weight)
c=julebu("cc",120)
c.pao()
c.eat()
c.eat()
print(c.weight)




