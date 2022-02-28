# 知某次聚会敏感词有N个人参加，这N个人来自26个地区，现在将26个地区使用数字0-25表示，
# 使用整数数组Locations存储这N个人的地区, 请返回一个bool值, True代表所有人的地区全都不同，False代表存在相同地区。要求：不能使用额外的存储结构。
# area = []
# for i in range(0,26):
#     area.append(i)
# # print(area)
# Locations = [1,1,2,3,4,5]
# set1 = set(Locations)
# bool = len(set1)==len(Locations)
# print(len(set1)==len(Locations))
# if bool == True:
#     print('所有人的地区全都不同')
# else:
#     print('存在相同地区')

# a = input("第一个数：")
# b = input("第二个数：")
# c = input("第三个数：")
# list = [a,b,c]
# list.sort()
# print(list)


# 求列表重复最多的数字
list0=[1,1,2,2,2,3,3,3,3,4,4,4,4,9,9]
new = []
num=0
name =0
eqkey =[]
eqvalue = []
for i in list0:
    if num < list0.count(i):
        num = list0.count(i)
        name = i
    elif num == list0.count(i):
        num = list0.count(i)
        name = i
        eqkey.append(name)
        eqvalue.append(num)
print(eqkey,eqvalue)


print(f'出现次数最多的是{name},次数是{num}')









abc = max(list0,key=lambda a:list0.count(a))
print(abc)


for n in list0:
    new.append(list0.count(n))

info1=dict.fromkeys(list0)

for a in range(len(list0)):
    info1[list0[a]] = new[a]
print(info1)
# result_max = max(info1,key=lambda x:info1[x])
result_max = max(info1,key=info1.get)
print(f'max:{result_max}')

str1 = "AAAaaa8888899sssss"
print(max(str1, key=str1.count))
list1 = ['11', 'zzz', '22', 'eee']
print(max(list1))
result_max1 = max(info1.values())
print(info1.values(),type(info1.values()))







