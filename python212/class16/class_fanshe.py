# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/15
# @Email:2155896749@qq.com
# @File: class_fanshe.py
class M211Vip:

    def __init__(self,name,wkage):
        self.name=name
        self.wkage=wkage

    def welcome(self):
        print("恭喜加入组织")

    def learning(self):
        print("正在跟其他人拉开差距......")

def mylearning():
    print("正在自学中....")

if __name__ == '__main__':
    bo=M211Vip("波","3")
    print(bo.name,bo.wkage)  #实例属性
    name=getattr(bo,"name")   #把字符串映射到实例的变量
    wkage=getattr(bo,"wkage")
    method=getattr(bo,"learning") #映射到实例的方法
    print(name,type(name))
    print(wkage, type(wkage))
    print(method,type(method))
    # 执行方法
    method()
    if hasattr(bo,"learning"):
        print("正在学习中....")
    else:
        print("正在加班中....")
    # 2、hasattr判断对象是否有对应的属性
    if hasattr(bo,"name"):
        print("有name属性....")
    else:
        print("没name属性....")

    #setattr 设置对象的内容（属性/方法）
    setattr(bo,"name","波波")   #修改对象的属性
    name=getattr(bo,"name")
    print(f"被修改的对象属性:{name}")
    # 类的外部的函数映射到类里面的方法
    setattr(bo,"mylearning",mylearning)
    bo.mylearning()
    getattr(bo,"mylearning")()
    # 4、delattr删除指定属性
    delattr(bo,"wkage")
    print(bo.wkage)




