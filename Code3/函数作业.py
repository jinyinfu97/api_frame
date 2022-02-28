# （完成1,2,3,4题，后面的题目暂时不做）
# 1.写函数，接收两个数字参数，返回最大值
# 例如：
# 传入：10,20
# 返回：20
def getmax(a,b):
    mmax=a
    if b>a:
        mmax=b
    return mmax
print(getmax(10,20))
# 2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
# 例如：
# 传入：[34,23,52,352,352,3523,5]
# 返回：[23,352,3523]
def getnewlist(mylist):
    list1=[]
    for i in range(0,len(mylist)):
        if i%2!=0:
            list1.append(mylist[i])
    return list1
print(getnewlist([34,23,52,352,352,3523,5]))
# 3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
# 传入2：[34,23,52]     				返回2：[34,23,52]
def get5len(mylist):
    list1 =[]
    if len(mylist)>5:
        for x in range(0,5):
            list1.append(mylist[x])
    else:
        list1=mylist
    return  list1
print(get5len([34,23,52,352,666,3523,5]))
print(get5len([34,23,52]))
# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# 例如：
# 传入："hello world"
# 返回：True
def isnull(str1):
    a=False
    for x in str1:
        if x==' ':
            a=True
            break
    return a

print(isnull("hello world"))