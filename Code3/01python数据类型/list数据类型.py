# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/12
# @Email:2155896749@qq.com
# @File: list数据类型.py

"""
不可变数据
string:"" '' "
number：
元组：()
---可变数据----
列表：通过[],也可以存储多个数据，数据类型可以不一样，并且可以支持多种类型，
元素与元素之间也是通过，隔开

"""
list1=[1,2,3,4,"baby",[1,2,3],(1,2,3)]
print(list1)
print(type(list1))
# 获取列表中最后一个元素   某个位置元素  或者部分元素  -----》切片 变量名[开始索引:结束索引：步长]
print(list1[-1])
print(list1[:4])
del list1[0]
print(list1)
# 列表也是可以支持运算   + * in/not in
list1=list1+["hefan","dingdong"]
print(list1)
print(list1*3)

"""
list常见内置函数
操作：添加/删除/查找、修改 元素

"""
# 操作：添加元素append()
list2=[1,2,3,4,5]
list2.append(6)  #做增加操作
print(list2)
# 增加0，最前面    insert(index,object)指定位置插入值
list2.insert(0,"大雨")
print(list2)
# 需要批量添加多个值到列表中 6,7,8,9,10
list2.extend([6,7,8,9,10])
print(list2)
# 删除
# list2.pop()   #不传入索引值，则删除最后一个，否则删除指定索引值的元素  pop()返回删除的值
print(list2)
del_value=list2.pop(0)
print(del_value)
print(list2)
list2.clear()  #清空列表
print(list2)
list3=[20,9,1,2,3,4,5,6]
copy_list=list3.copy()
print(copy_list)
list3.remove(6)   #remove与pop区别？   remove--根据值进行删除 pop---》根据索引删除
print(list3)
# 查找
print(list3.index(2) )  #查找到返回值的索引值，否则抛出异常
# 查找某个元素在列表中出现的次数
print(list3.count(1))
# 列表进行排序
list3.sort()
print(list3)
# 列表反转
list3.reverse()
print(list3)









