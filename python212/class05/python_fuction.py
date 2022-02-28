# -*- coding=utf-8 -*-
# @time:2021/9/23
# @phone:15874198829
# @author:码尚教育_星瑶
"""
1、函数定义及作用：
定义：函数就是组织好的，可以重复使用的，用来实现单一或者相关联功能的代码段
作用：提高代码的复用性
比如：print()/input()  ---- Python内置函数
2、如何定义函数？
def 标识符(参数1,参数2,参数3...,参数n):
    函数体（用来实现单一或者相关联功能的代码段）
    return [表达式]

函数是否需要带上return?
默认情况，可以不要return或者return返回None
什么情况下，需要带返回值(return [表达式])
需要调用这个函数的调用方是否需要或许函数体中的某个值
3、函数调用
    函数名(参数1值,参数2值,参数2值....参数n值)
    默认情况下，参数值和参数名称是按照函数定义顺序匹配的
    实际情况，项目中存在多个参数的函数，不一定需要用默认情况下这种调用函数，可以采用其他调用函数参数类型
4、调用函数事可使用的正式参数类型：
    1）必需参数
        必须以正确的顺序传入函数，调用时的数量必须和定义时一样的
        必需参数(参数顺序、参数个数、参数类型都必须跟函数定义一致)
    2）关键字参数（顺序不匹配）
        允许函数调用时参数的顺序与定义不一致
        使用关键字来确定传入的参数值
    3）默认参数（个数不匹配）
        调用函数时，可以对默认参数不传值，则取默认值，否则取传递的值
    4）不定长参数
        函数调用方无法确定参数的个数及类型在这情况下，可以定义为不定长参数
        比如：定义注册函数？
        A注册账号： A调用注册函数，提供姓名+手机号码（必填项）
        B注册账号   B调用注册函数，提供姓名+手机号码（必填项）+工作城市+工作年限+其他信息
        1)第一类 ：加*参数名
        函数内部把可变参数组装到元组中
        调用（加*参数名）不定长参数：
        函数名（参数值1,参数值2,参数值3....）
        2)第二种：加**参数名
        函数内部把可变参数组装到字典中
         调用（加**参数名）不定长参数：
         可以只传必需参数，也可以传入任意个数的关键字参数
         函数名（参数1名=参数值1,参数2名=参数值2,参数3名=参数值3）
         关键字参数的名称不受限制，可以任意关键字参数名称
        3)第三类：*单独出现  命名关键字参数
         命名关键字参数：作用：限制关键字参数的名字
         关键字参数的名称受限制，关键字参数的名称跟定义的形参的名称一致
    # 定义函数时候，参数顺序
    必需参数、默认参数、可变参数（*参数名称/或者*）、命名关键字参数、**参数名（不限定参数名称关键字参数）
5、函数嵌套
    函数体中调用其他函数（当然可以自己本身）
    递归函数：函数体中调用自己本身函数
"""
#不带参数函数
def welcome():
    return "欢迎进入码尚教育的VIP课堂"


def goodbye():
    print("谢谢对码尚教育的VIP课堂关注")

# 调用没有参数函数
value=welcome()
print(value)
value2=goodbye()
print(value2)

"""
需求：求最大值
"""
# 带参数的函数  name形参
def welcome(name):
    print(f"{name}，欢迎进入码尚教育的VIP课堂")
    return

name='MS200'
# name 实参
welcome(name)

def max(a,b):
    """
    求最大值
    :param a:其中一个数
    :param b: 其中一个数
    :return:
    """
    if a>b:
        max=a
    else:
        max=b
    return max
value=max(10,5)
print("求5,10的最大值：",value)

#就业榜单输出学员详细信息： 姓名  工作年限  城市  学前薪资  学后薪资
def offerinfo(name,work_age,work_city,pre_gz,bf_gz):
    print(f"调用函数：offerinfo 姓名 :{name} ,工作年限:{work_age} , 所在城市:{work_city}， 学前薪资: {pre_gz}k ，"
          f"学后薪资:{bf_gz}k ，涨薪{bf_gz-pre_gz}k")

# 必需参数(参数顺序、参数个数、参数类型都必须跟函数定义一致)
offerinfo('alone',2,'深圳',15,20)
# 关键字参数
offerinfo(work_age=2,name='alone',work_city='深圳',bf_gz=20,pre_gz=15)


def offerinfo2(name,work_age,pre_gz,bf_gz,work_city='深圳'):
    print(f"调用函数：offerinfo2 姓名 :{name} ,工作年限:{work_age} , 所在城市:{work_city}， 学前薪资: {pre_gz}k ，"
          f"学后薪资:{bf_gz}k ，涨薪{bf_gz-pre_gz}k")
# 默认参数
offerinfo2(work_age=2,name='alone',bf_gz=20,pre_gz=15,work_city='北京')


"""不定长参数"""

# 不定长参数函数（加*参数名）
def register(name,phone,*args):
    # 把不确定的参数都存储在元组里args
    print(args,type(args))
    info=[name,phone]
    for value in args:
        info.append(value)
    print(f"{name}注册成功")
    print(f"打印{name}注册的个人信息：",info)
#调用不定长参数(加*参数名)
extra=("深圳","3",15000,25000,"深圳宝安洪浪北***")
register("B",'12345678912',*extra)
register("A",'15874198829')

# 不定长参数函数（加**参数名）
def register_yh(name,phone,**kwargs):
    # 把不确定的参数都存储在字典里kwargs
    print(kwargs, type(kwargs))
    info = {"name":name,"phone":phone}
    for key,value in kwargs.items():
        info[key]=value
    print(f"通过调用rigister_yh函数，完成{name}注册信息的填写")
    print(f"打印{name}注册的个人信息：", info)

#调用不定长参数(加**参数名)
extra={'city': '深圳', 'workage': '3', 'xz': 15000, 'after_xz': 20000}
register_yh("B",'12345678912',city1=extra['city'],workage3=extra['workage'],xz=extra['xz'],after_xz=extra['after_xz'])
#更简洁的方式
register_yh("B",'12345678912',**extra)

# 不定长参数函数（*单独出现）  * 作为命名关键字参数的分隔符，后面属于命名关键字参数（参数名称限定的了）
def register_3(name,phone,*,city,work_age):
    print(name,phone,city,work_age)


#调用 不定长参数函数（*单独出现）
register_3("MS219",'1111111111',city="深圳",work_age="3年")

def register_4(name,phone,*args,city,work_age):
    print(name,phone,args,city,work_age)

register_4("register_4",'1111111111',city="深圳",work_age="3年")


# 定义一个函数实现计算多个数字之和
def sum(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
value1=sum(1,2)
value2=sum(22,44)
value3=sum(1,2,3,4,5,6,7,8,9,10)
print(value1,value2,value3)


# 封装函数涨薪情况,获取涨薪幅度多少，并展示学员的信息
def xz_up(name,phone,*,xz,xqxz,**kwargs):
    """涨薪=学后薪资-学前薪资"""
    info={"name":name,"phone":phone}
    for key,vale in kwargs.items():
        info[key]=vale
    print(f"vip学习涨薪：{xz-xqxz}元,学员信息：{info}")

extra={'city': '深圳', 'workage': '3年'}
xz_up('MS201',"1111111111",xz=20000,xqxz=15000,**extra)
xz_up('MS230',"1111111111",xz=20000,xqxz=15000)



"""
函数嵌套
"""

def a():
    print("执行a函数代码段")

def b():
    a()
    print("执行b函数代码段")

def c():
    #函数体中定义函数
    def d():
        print("执行d函数代码段")
    return  d

def f():
    print("执行f函数代码")

def aa(a):
    # 调用参数a函数
    a()
    print("aa函数扩展当前函数的功能代码")

value=c()
print(type(value))
# 调用d函数
value()

print("函数也是可以作为参数使用-----")
aa(f)


"""
递归函数：自己调用自己本身函数
注意：1、结束条件
     2、递推的条件
1、计算阶乘 1*2*3*....*n
2、1,1,2,3,5,8,13....(斐波纳契数列)
"""

def count(n):
    result=1
    for num in range(1,n+1):
        result*=num
    return result
value=count(5)
print(value)

# 基于递归函数实现
def count_2(n):
    if n==1:
        return 1
    return n*count_2(n-1)
value=count_2(5)
print(value)

"""
1,1,2,3,5,8,13....(斐波纳契数列)
"""
def fbnx_num(n):
    if n==1 or n==2:
        return 1
    return  fbnx_num(n-1)+fbnx_num(n-2)

nums=[]
for n in range(1,10):
    nums.append(fbnx_num(n))
print(nums)


"""
-----------------------欢迎进入T666班学生管理系统-----------------------------
请选择系统功能：
0:显示所有学员信息
1:添加一个学员信息
2:删除一个学员信息
3:修改一个学员信息
4:查询一个学员信息
exit:退出学生管理系统

"""
caozuo_info="""-----------------------欢迎进入T666班学生管理系统-----------------------------
请选择系统功能：
0:显示所有学员信息
1:添加一个学员信息
2:删除一个学员信息
3:修改一个学员信息
4:查询一个学员信息
exit:退出学生管理系统"""

def all_info():
    pass

def add():
    pass

def delete():
    pass

def update():
    pass

def select():
    pass

def exit():
    print("退出学生管理系统")


def caozuo(caozuo_value):
    if caozuo_value=="0":
        all_info()
    elif caozuo_value=="1":
        add()
    elif caozuo_value=="2":
        delete()
    elif caozuo_value=="3":
        pass
    elif caozuo_value=="4":
        pass
    elif caozuo_value=="exit":
        exit()
        return
    else:
        pass
    caozuo(input(caozuo_info))

caozuo_value=input(caozuo_info)
caozuo(caozuo_value)
