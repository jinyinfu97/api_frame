# 1、定义一个列表[1, 2, 3]，并将列表中的头尾两个元素对调。对调后为[3, 2, 1]
list = [1,2,3]
list.sort(reverse=True)
print("对调后为：", list)

# 2、定义一个列表，并将列表中的指定位置的两个元素对调。对调第一个和第三个元素
# 列表如下：[23, 65, 19, 90]
# 对调后结果：[19, 65, 23, 90]
list1 = [23, 65, 19, 90]
temp=list1[0]
list1[0]=list1[2]
list1[2]=temp
print("对调后为：", list1)

# 3、对列表[10, 11, 12, 13, 14, 15]
# 翻转，调整后为[15, 14, 13, 12, 11, 10]
list2 = [10, 11, 12, 13, 14, 15]
list2.reverse()
print("翻转后为：", list2)

# 4、判定6是否包含列表[1, 6, 3, 5, 3, 4]
list3 = [1, 6, 3, 5, 3, 4]
if 6 in list3:
    print("6在列表里")
else:
    print("6不在列表里")

# 5、[1, 6, 3, 5, 3, 4]转换为元组
list4 = [1, 6, 3, 5, 3, 4]
list4 = tuple(list4)
print("转换后：", list4)

# 6、根据列表[ 1, 6, 3, 5, 3, 4 ]作为新字典的key,对应key的初始值为0，并打印新字典对象（不做）
# 创建一个字典，key确定，值不太确定，设置value-->默认值null
keys=[ 1, 6, 3, 5, 3, 4 ]
info=dict.fromkeys(keys,0)
print(info)

# 7、循环打印出字典{'name':'aming','age':18,'school':'cema'}中的所有键和值， （不做）
info1 = {'name':'aming','age':18,'school':'cema'}
for x,y in info1.items():
    print(x,y)

# 8、{‘taobao’,'jingdong','alibaba','baidu','taobao'}对元素去重复  （不做）
set = {'taobao','jingdong','alibaba','baidu','taobao'}
print(set,type(set))

# 9、分别有两个集合{1,2,1,3,4,5,6,7}，{1,2,3,8,9,7,10}，求两个集合的差集、并集、交集（不做）
set1 = {1,2,1,3,4,5,6,7}
set2 = {1,2,3,8,9,7,10}
print("求两个集合的差集: ", set1-set2)
print("并集",set1.union(set2))
print("交集：",set1.intersection(set2))

# 10、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复（不做）
if set1.intersection(set2)!={}:
    print("有重复")
else:
    print("无重复")

# 11、list7=[1,2,3,4,5]根据列表中的元素作为字典中的key,及初始值为0，打印这个新的字典，不用fromkey方法实现（不做）


