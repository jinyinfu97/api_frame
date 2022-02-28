# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/14
# @Email:2155896749@qq.com
# @File: if语句.py
"""

# 当某某成绩大于等于60，及格 否则显示不及格-----》条件控制语句
# 单一条件语句格式：
if 条件1:
    代码块1---->显示及格
else:
    代码2----》显示不及格
运行逻辑：
条件1为真，执行代码块1
条件1为假，执行代码块2

多个条件情况下：
if 条件1:
    代码块1
elif 条件2:
	代码块2
…
else:
	代码块N

如果条件1为True将执行代码块1语句
如果条件1为False将判断条件2
如果条件2为True将执行代码块2语句
如果条件2为False将判断下一个条件，直到什么条件都不符合就执行代码N

"""


score=float(input("请输入你的成绩："))
if score>=60:
    print("恭喜你")
else:
    print("继续加油！")


# 成绩  -----》多重if
# 《60  不及格   第一大类
# 第二大类：成绩大于60  ----》多重if
#    75>x》60 一般
# 75>=x<=85   中等
# 85以上   优秀生

# score=float(input("请输入你的成绩："))
# if score>=60:
#    if score>=85:
#        print("优秀生")
#    elif score>=75:
#        print("中等")
#    else:
#        print("一般")
# else:
#     print("不及格")
score=float(input("请输入你的成绩："))
if score<60:
    print("不及格")
elif score>=85:    #优秀生  A B  C
    if score>95:
        print("A")
    elif score>90:
        print("B")
    else:
        print("C")
elif score>=75:
    print("中等生")
else:
    print("一般")

