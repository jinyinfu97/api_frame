# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/21
# @Email:2155896749@qq.com
# @File: os模块应用.py

import os
import stat

"""
os模块----》对文件目录进行操作  -----》实现对文件目录操作与管理
1、创建删除修改重命名文件目录
2、获取文件目录路径
3、获取文件目录属性
4、修改查询文件权限  
"""

# os.getcwd()  获取当前.py文件所在的项目路径---》os.getcwd()

file_path = os.getcwd()
# 获取file_path上一级路径  ----》os.path.dirname(path)
dirname = os.path.dirname(file_path)
print("目录路径：", dirname)
print("获取当前项目路径", file_path)
# 05时间模块异常处理-->创建文件A  路径拼接 os.path.join(path1,path2)
path_A = os.path.join(file_path, "A")
print(path_A)
# os.mkdir(path_A)
# 路径拆分 目录+文件   ---》os.path.split(path1)
path1 = "C:/Users/Administrator/PycharmProjects/pythonProject4/Code3/05时间模块异常处理/os模块应用.py"
new = os.path.split(path1)
print(new)

# 获取目录或者文件的访问权限
# Mode:os. F_OK(是否存在)、os.R_OK（可读 ）、os.W_OK（可写）、os.X_OK（可执行）
value = os.access(path_A, os.F_OK)
isread = os.access(path_A, os.R_OK)
iswrite = os.access(path_A, os.W_OK)
print(value, isread, iswrite)
# OTH  其他用户  GRP 用户组  USR拥有者  R 可读  X 可执行   W 可写
os.chmod(path_A, stat.S_IROTH)
