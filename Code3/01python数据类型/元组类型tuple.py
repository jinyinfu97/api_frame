# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/10
# @Email:2155896749@qq.com
# @File: 元组类型tuple.py



# 定义元组,元组可以存储多个数据
tup1=(1,2,"abc",2.0)
print(type(tup1))
print(tup1)
# 创建空元组
tup2=()
print(type(tup2))
print(tup2)
# 只有一个元素的元组   1
tup3=(1,)
print(type(tup3))
# 获取元组中某个数据的值或者多个数据的值  ----->切片
print(tup1[0],tup1[:-1])
print(tup1[::-1])

new_tup=tup1+tup3
print(new_tup)
del new_tup
# 元组运算符  +  * 重复  in   存在     not in  不存在
new_tup=tup3*3
print(new_tup)

tup4=(1,2,3,4,5,6)
if 1 in tup3:
    print("存在")
else:
    print("不存在")

good="棒！"
print(good*10)
