# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/19
# @Email:2155896749@qq.com
# @File: 文件操作.py
str1="""
python全栈自动化测试
Python基础
接口自动化
web自动化
app自动化
.....
"""
file=open("20210419_02.txt","a+",encoding="utf-8")
#  业务代码  可能也会异常，后面代码不会执行，file.close()不会执行，
print(file.readline())
# file.writelines(str1)
file.close()

# with  open("20210419_01.txt","w+",encoding="utf-8") as file:
# #     # 一旦有任何异常，自动关闭文件对象
#     file.writelines(str1)  #写入多行内容

'''
# 读取文件中内容
with open("20210419_01.txt","r",encoding="utf-8") as file2:
    # print(file2.tell())
    # # 改变指针位置，读取中间部分内容
    # file2.seek(2,0)
    # print(file2.tell())
    print(file2.readline())
    # print(file2.read(10))

    # print(file2.tell())
    # print(file2.readline())
    # print(file2.tell())
    # print(file2.readline())
    # print(file2.readline())

print(file2.encoding,file2.mode,file2.closed)

'''