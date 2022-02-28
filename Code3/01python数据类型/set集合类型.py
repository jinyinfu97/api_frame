# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/12
# @Email:2155896749@qq.com
# @File: set集合类型.py

"""
集合set类型：表示符{}--》字典{}？相同表示怎么区分？
可以存储多个元素，只支持不可变数据类型string,number,tuple
注意：
1、如何区分集合{}---》字典话，表示形式不一样的
2、元素类型  只支持不可变数据类型string,number,tuple,不支持可变数据类型(dict,set,list)

注意：
1、集合是无序列表，因此不支持通过索引取值
2、集合自动去重

各大数据类型之间可以相互转化  集合转化list，通过切片实现取某个元素

"""
set1={1,2,3,4,(1,2,3)}
print(set1)
print(type(set1))
# 创建空集合
null=set()
print(null)
print(type(null))
# # 获取集合某个元素或者多个元素   ？？？？？
# print(set1)
# 运算
# 交集  A & B  取两个集合的相同元素
A={1,2,3,4,5}
B={6,7,8,9,10,5,4}
print(A,B)
new=A&B
print(new)
print("交集：",A.intersection(B))

# 并集  |  合并A、B集合，返回集合既包含A集合所有元素也会包含B集合的所有元素
new1=A|B
print(new1)
print("并集",A.union(B))
# 差集  A-B  返回A集合的所有元素，但是不会包含B中的元素
print(A-B)
print("差集",A.difference(B))
# 异或 ^  A^B  返回两个集合相同元素之外的其他元素的集合
print(A^B)
print("异或",A.symmetric_difference(B))
#
son={6,10}
print(son.issubset(A))


# 8、把元组(1,2,3,4,5,6)元素格式化成字符串
tupl=(1,2,3,4,5,6)
new=f"{tupl}"
new1="{0}".format(tupl)
print(new)
print(type(new))

set2={1,2,3,4,5,4,5,6,7}
print(set2)
print(list(set2)[-1])
# list()
tup2=(1,3,5,7,8)
newlist=list(tup2)
print(newlist)
print(type(newlist))
# tuple()
new_tup=tuple(newlist)
print(new_tup,type(new_tup))
# set()
new_set=set(newlist)
print(new_set,type(new_set))
new_set2=set(new_tup)
print(new_set2,type(new_set2))


# 判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复
set3={1,2,3,4}
set4={7,8,9}
same=set3&set4
if len(same)>0:
    print("重复")
else:
    print("无重复")

#     isdisjoint判断两个集合是否包含相同元素，如果没有则返回True，否则返回false
if  set3.isdisjoint(set4):
    print("无重复")
else:
    print("重复")
set3.add(5)
print(set3)
set3.update({6,7,8,9})
print(set3)
set3.remove(9)
print(set3)










