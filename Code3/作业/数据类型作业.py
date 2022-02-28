# 1、用print函数打印多个值
# print("你好")
# print("hello!")

# 2、用print函数不换行打印
# print("你好",end=" ")
# print("hello!")

# 3、导入模块的方式有哪些
# 答：被导入的模块与调用模块属于同/非 同一目录/
#    导入格式统一：from 上上级模块.上一级模块  import 当前模块
# 导入方式：
# 1、import 模块名
# 2、from 模块名 import  函数名1,函数名2   导入某个模块下指定数据或者函数
# 导入时，可以对被导入的模块名及函数名或者变量名都可以取别名    as 别名

# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
# 答：number,string,list,tuple,dist,set
# 可变：list,dict,set
# 不可：number,string,tuple

# 5、python3中可以支持哪些数值类型？
# 答：int,float,bool,complex

# 6、判断变量类型有哪些方式，分别可以用哪些函数？
# obj = 123
# 方法一
# print(isinstance(obj,int))
# 方法二
# print(type(obj))

# 7、分别对49.698作如下打印
# 1）四舍五入，保留两位小数
a=49.698
# round函数不保留0
print(round(a,2))
# 用float函数可以取到0
print('%.2f'%a)
# 2）向上入取整
import math
print(math.ceil(a))
# 3）向下舍取整
print(math.floor(a))
# 4）计算8除以5返回整型
print(8//5)
# 5）求4的2次幂
print(4**2)
# 6）返回一个（1, 100）随机整数
import random
print(random.randint(1,100))

# 8、依次对变量a, b, c赋值为1, 2, 3
(a,b,c)=(1,2,3)
print(a,type(a))
print(b, type(b))
print(c,type(c))

# 9、截取某字符串中从2索引位置到最后的字符子串
str = "abcdefg"
print(f"截取{str}中从2索引位置到最后的字符子串为：", str[2:])

# 10、对字符串“testcode”做如下处理：
# 1）翻转字符串
str1="testcode"
print("翻转字符串为:", str1[-1::-1])
# 2）首字母大写
print("首字母大写为", str1.capitalize())
# 3）查找是否包含code子串，并返回索引值
if "code" in str1:
    print("包含code子串")
    print("返回索引值为：", str1.index('code'))
# 4）判断字符串的长度
print("判断字符串的长度", len(str1))
# 5）从头部截取4个长度字符串
print("从头部截取4个长度字符串", str1[0:4])
# 6）把code替换为123
str1 = str1.replace("code","123")
print("code替换为123并打印替换后的字符串为：", str1)
# 7）把“testcode”字符串中的两个单词转换为列表中的元素，并打印处理
str1 = "testcode"
str2 = str1[0:4]
str3 = str1[4::]
list = []
list.append(str2)
list.append(str3)
print("“testcode”字符串中的两个单词转换为列表中的元素为：", list)
# 8）把['test', 'code']
# 把list变量中的元素连接起来
# list = ['test', 'code']
# for i in list:
#     print(i,end="")

# 11、如何打印出字符串“test\ncode”
print (r"打印出字符串test\ncode为:" r"test\ncode")

# 12、如何创建一个空元组
tuple = ()
print(tuple)
print(type(tuple))

# 13、创建一个只包含元素1的元组，并打印出该变量的类型
tuple1 = (1,)
print(type(tuple1))

# 14、元组中元素可以修改？如何更新元组中的元素？
# 答：元祖是不可变的数据类型，所以元组中的元素是不可更改的，但是如果元祖中的元素是列表、集合或者字典，那可以对其进行修改
tuple3 = (1,2,[3,4,5])
tuple3[2][0] =6
print(tuple3)

# 15、对元组（1, 2, 3, 4, 5)做如下操作：
# 1）取倒数第二个元素
tuple1 = (1,2,3,4,5)
a = tuple1[-2]
print(a)
# 2）截取前三个元组元素
print(tuple1[0:3])
# 3）依次打印出元组中所有元素
for i in tuple1:
    print(f"元祖中的第{i}个元素为：",i)

# 16、把元组(1, 2, 3, 4, 5, 6)元素格式化成字符串
seq = ('1','2','3','4','5')
print(','.join(seq))
print(type(','.join(seq)))
