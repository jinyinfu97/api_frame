# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/17
# @Email:2155896749@qq.com
# @File: 03函数.py

def hello():
    print("hello zhidashu")

# 执行函数体代码---》调用函数
hello()

def hello(name):
    return("hello ",name)
    # return

r=hello("九头蛇")
print(r)

# 不可变数据类型参数  list dict set  通过参数传递，不可以改变参数值
print("开始")
old=2
print(id(old))
def change(old):
    old=10
    print(id(old))
    return old

change(2)
print(old)
print(id(old))
print("结束")


# 可变数据类型参数  list dict set  通过参数传递，可以改变参数值
def change_list(mylist):
    mylist=mylist.append(10)

mylist=[1,2,3,4,5]
change_list(mylist)
print(mylist)





