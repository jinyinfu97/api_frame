import os
# 1、文件操作
# 	1、创建python.txt文件
# 	2、写入内容
# 	3、读取文件内容
# 	4、读取第一行内容
# 	5、获取当前文件指针位置
# 	6、从文件开头部分位移2，进行行读取
# 	7、获取文件的编码格式及文件名称
# file_path=os.getcwd()
# dirname=os.path.dirname(file_path)
# print(dirname)
str='''
金音符
hmj
伟哥
'''
# os.m (os.getcwd()+'\python.txt')
with open("python.txt","w+",encoding="utf-8") as f:
    f.writelines(str)
    print(f.tell())
    f.seek(2,0)
    print(f.tell())
    print(f.readline())

# 2、获取当前文件路径
# 3、获取当前文件的绝对路径、当前文件路径、获取当前文件名
# 4、目录与文件如何实现拼接
# 5、获取系统时间戳，时间元组
# 6、时间戳：1606915064  格式成字符串
# 7、获取时间戳1606915064的年、月、日、星期
# 8、返回系统时间（通过时间元组表示）
# 9、判断用户输入，非数字，则捕获异常。无异常则打印下一步
# 10、进行登录操作，当输入的用户名密码错误，则抛出异常，提示用户名密码错误
#    正确用户名及密码分别为：admin,admin
def yanzheng(user,password):
    if user == 'admin' and password == 'admin':
        print('输入正确，请继续下一步')
    else:
        raise Exception('提示用户名密码错误')
yanzheng('admin','admin')
print(12312)