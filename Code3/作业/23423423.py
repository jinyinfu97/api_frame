# 冒泡排序
# list = [2,44,521,123,33,34,576,11,70]
# temp = 0
# for i in range(0,len(list)):
#     for n in range(0,len(list)-1):
#         if list[n]>list[n+1]:
#             temp = list[n]
#             list[n] = list[n+1]
#             list[n+1] = temp
# print(list)

# for cs in range(len(lis)):
#     for index in range(len(lis)-1):
#         if lis[index]>lis[index+1]:
#             temp=lis[index]
#             lis[index]=lis[index + 1]
#             lis[index + 1]=temp
# print(lis)

#列表去重
list1 = [1,1,2,3,4,4,5]
set1 = set(list1)
newlist = list(set1)
print(newlist)
