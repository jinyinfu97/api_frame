# 给一个列表，要求分组输出列表中连续数组的首位和末位
# 如[1,2,3,4,6,7,8,10,11,13]
# 输出[1,4][6,8][10,11][13]
list = []
# newlist = [1, 3, 2, 4, 6, 7, 8, 10, 11, 13, 222, 223, 224, 278, 277]
newlist = [1,3,5,6,7,99]
a = 0

# 方法二：
for i in range(0,len(newlist)):
    list.append(newlist[i])
    if i+1<len(newlist):
        if newlist[i]+1 != newlist[i+1]:
            print(list)

        elif len(list)>1:
            print(list[0:len(list):len(list)-1])

        # elif len(list)==1:
        #     print(list)
    elif i+1 == len(newlist):
        print(list)
    list = []
















# 方法一：
# for i in newlist:
#
#     list.append(i)
#     if i + 1 not in newlist:
#         if len(list) > 1:
#             print(list[0:len(list):len(list) - 1])
#         elif len(list) == 1:
#             print(list)
#         list = []
#     elif a + 1 < len(newlist):
#         if i != newlist[a + 1] - 1:
#             print(list)
#             list = []
#     elif a + 1 == len(newlist):
#         print(list)
#     a = a + 1
