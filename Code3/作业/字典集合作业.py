# 1、根据列表[ 1, 6, 3, 5, 3, 4 ]作为新字典的key,对应key的初始值为0，并打印新字典对象
list = [1, 6, 3, 5, 3, 4]
info = dict.fromkeys(list, 0)
print(info)

# 2、循环打印出字典{'name':'aming','age':18,'school':'cema'}中的所有键和值，
dict2 = {'name': 'aming', 'age': 18, 'school': 'cema'}
for key, value in dict2.items():
    print(f"键：{key},值：{value}")

# 3、{‘taobao’,'jingdong','alibaba','baidu','taobao'}对元素去重复
set0 = {'taobao', 'jingdong', 'alibaba', 'baidu', 'taobao'}
print(set0)

# 4、分别有两个集合{1,2,1,3,4,5,6,7}，{1,2,3,8,9,7,10}，求两个集合的差集、并集、交集
set1 = {1, 2, 1, 3, 4, 5, 6, 7}
set2 = {1, 2, 3, 8, 9, 7, 10}
print(f"两个集合的差集：{set1 - set2}")
print(f"两个集合的并集：{set1 | set2}")
print(f"两个集合的交集：{set1 & set2}")

# 5、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复
if set1.intersection(set2) != set():
    print("有重复")
else:
    print("无重复")

# 6、info=['姓名','所在城市','毕业年限','目前薪资','期望薪资','班级']
# 每个学员都基于列表中的字段存储对应的信息数，基于字典来进行存储，如何初始化定义每个学员的信息数据？（基于字典来存储这些数据信息）
info = ['姓名', '所在城市', '毕业年限', '目前薪资', '期望薪资', '班级']
newinfo = dict.fromkeys(info)
# print(newinfo)
# info2=['同学A','上海','2年','15k','20k','MS212']
infoname = ['同学A', '同学B', '同学C', '同学D', '同学E', '同学F']
infocity = ['上海', '北京', '深圳', '广州', '江苏', '浙江']
infoage = ['1', '2', '3', '4', '5', '6']
infosalary = ['10k', '12k', '13k', '14k', '15k', '16k']
info_exp_salary = ['20k', '22k', '23k', '24k', '25k', '26k']
infoclass = ['MS210', 'MS211', 'MS210', 'MS212', 'MS211', 'MS212']
list1 = []
for i in range(0, len(infoname)):
    newinfo = dict.fromkeys(info)
    newinfo['姓名'] = infoname[i]
    newinfo['所在城市'] = infocity[i]
    newinfo['毕业年限'] = infoage[i]
    newinfo['目前薪资'] = infosalary[i]
    newinfo['期望薪资'] = info_exp_salary[i]
    newinfo['班级'] = infoclass[i]
    # print(newinfo)
    list1.append(newinfo)
print(list1)
for newlist in list1:
    print(newlist)

# 7、a={'name':'AA','age':18} 获取a变量的classname的值,如果该key不存在，则添加该key，并设置默认值为'212'
a = {'name': 'AA', 'age': 18}
a.setdefault('classname', '212')
print(a)
