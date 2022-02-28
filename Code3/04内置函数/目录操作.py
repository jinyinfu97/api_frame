# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/19
# @Email:2155896749@qq.com
# @File: 目录操作.py

import os

# 创建文件夹 mkdir(path)
os.mkdir(os.getcwd()+"\B")
# os.mkdir(r"E:\VIP\M211\Code\04内置函数\A")
print("目录B创建成功")
# 创建多级目录os.makedirs(path)
# os.makedirs(r"E:\VIP\M211\Code\04内置函数\B\C)
 # 删除空目录
import shutil
os.rmdir(r"E:\VIP\M211\Code\04内置函数\B\C")
# 删除非空目录shutil.rmtree(path)
shutil.rmtree(r"E:\VIP\M211\Code\04内置函数\B\C")

# 重命名os.rename(oldname,newname)
old=r"E:\VIP\M211\Code\04内置函数\B"
new=r"E:\VIP\M211\Code\04内置函数\new"
os.rename(old,new)
# 获取当前路径
print(os.getcwd())



