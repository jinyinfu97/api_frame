# -*- coding=utf-8 -*-
# @time:2021/9/28
# @phone:15874198829
# @author:码尚教育_星瑶
"""
文件处理：open()
read(n) 读取指定字节长度n 默认读取文件所有内容
readline() 默认读取当前行的所有内容，可以限制读n长度的内容
绝对路径
相对路径
"""
# 1 打开文件  with  as语句默认关闭文件对象
def file_operator():
    with open('info.txt',"r+",encoding="utf-8") as file:
        print(type(file))
        # 2 操作文件（读、写数据）
        content=file.readline()
        content2 = file.readline(2)
        content3= file.readline()
        print(content)
        print(content2)
        print(content3)
        print(file.mode,file.name)
        file.write("都是大佬！")
        print("获取文件的指针位置：",file.tell())
file_operator()

# # 改变指针的位置
# def change_tell():
#     with open('info.txt', "rb+") as file:
#         content1=file.read(2)
#         print(content1)
#         print(file.tell())
#         # 指针偏移1
#         file.seek(1,1)
#         content2 = file.read(2)
#         print(content2)
#
# # change_tell()
#
# def read_next():
#     with open('info.txt', "r+") as file:
#         for index in range(3):
#             line=next(file)
#             print(f"第{index}行:{line}")
# read_next()
#
# def read_lines(n):
#     with open('info.txt', "r+") as file:
#         lines=file.readlines()
#         print(lines,type(lines))
#         print(lines[n-1])
#
# def write_lines(str):
#     with open('info.txt', "a+") as file:
#         file.writelines(str)
#
#
# str="""
# MS299
# MS300
# MS301
# """
# str2=["MS299\n","MS300\n","MS301"]
# write_lines(str2)





