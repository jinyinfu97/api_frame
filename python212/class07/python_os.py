# -*- coding=utf-8 -*-
# @time:2021/9/30
# @phone:15874198829
# @author:码尚教育_星瑶
"""
os模块：提供了丰富的方法来处理文件及目录
2、os模块常用方法
    1、创建目录
    2、创建多级目录
    3、删除目录
    4、重命名文件及目录
    5、文件权限
        验证文件权限  os.acess(path,mode)  返回验证值是否与mode是否一致，是一致则返回True
        Mode:os. F_OK(是否存在)、os.R_OK（可读 ）、os.W_OK（可写）、os.X_OK（可执行）
    6、文件路径
        os.path模块使用
        获取当前文件的目录 os.getcwd()
        os.path.join(目录,文件) 目录拼接文件



"""
import os
import stat


def make_dir(path):
    """创建目录"""
    os.mkdir(path)
    print(f"创建目录：{path}成功")

def make_many_dirs(path):
    """创建多级目录"""
    os.makedirs(path)
    print(f"创建多级目录成功：{path}")

def delete_empty_dir(path):
    """删除空目录"""
    os.rmdir(path)
    print(f"删除目录成功，目录：{path}")

def delete_not_empty_dir(path):
    """删除非空目录"""
    import shutil
    shutil.rmtree(path)
    print(f"删除目录成功，目录：{path}")

def rename_dir(old,new):
    """重命名文件目录"""
    os.rename(old,new)
    print(f"重命名{old}命名{new}成功")


"""
# 创建目录
path=r"E:\VIP\MS212\python212\class07\MS212"
make_dir(path)

# 创建多级目录
path=r"E:\VIP\MS212\python212\class07\a\b\c"
make_many_dirs(path)

#删除非空目录
path=r"E:\VIP\MS212\python212\class07\a\b"
delete_not_empty_dir(path)

# 重命名
old=r"E:\VIP\MS212\python212\class07\a\info.txt"
new=r"E:\VIP\MS212\python212\class07\a\info.txt"
rename_dir(old,new)

# 验证文件的权限
new=r"E:\VIP\MS212\python212\class07\a\info.txt"
value=os.access(path=new,mode=os.F_OK)
print(value)

# 修改文件权限  权限值：r  w  x  rwx   用户权限：OTH  GRP   USR
path=r"E:\VIP\MS212\python212\class07\a\info.txt"
os.chmod(path=path,mode=stat.S_IRUSR)

"""


"""
6、文件路径   os.path模块使用

"""

path=r"E:\VIP\MS212\python212\class07\a\info.txt"
# 是否为目录
os.path.isdir(path)
# 是否为文件
os.path.isfile(path)

# 获取当前文件的目录 os.getcwd()

def get_path():
    path=os.getcwd()
    return  path

path=get_path()
print(path)

# 获取绝对路径
path=r"E:\VIP\MS212\python212\class07\a\info.txt"
print(os.path.abspath(path))

# 获取路径的目录
path=r"E:\VIP\MS212\python212\class07\a"
print("目录名称：",os.path.dirname(path))

#路径是否存在，存在返回True
print("路径是否存在",os.path.lexists(path))

# 路径进行分割  把目录及文件进行分割，返回一个元组os.path.split(path)
path=r"E:\VIP\MS212\python212\class07\a\info.txt"
value=os.path.split(path)
print(value)
rootpath=value[0]
print(f"获取路径{value}的目录：{rootpath}")

# 获取当前文件的名称
rootpath="E:\VIP\MS212\python212"
filename="1.log"
# 把目录和文件进行拼接os.path.join(目录,文件)
path=os.path.join(rootpath,filename)
print(path)
open(path,"w+")

# 需求：log目录/日志文件
rootpath="E:\VIP\MS212\python212"
log_dir=os.path.join(rootpath,"log")
import time
path=os.path.join(log_dir,f'log_{time.strftime("%Y%m%d%H%M%S",time.localtime())}.txt')
print(path)

# 如何获取根路径
path=__file__
print(path)
dir_path=os.path.dirname(os.path.dirname(path))
print(dir_path)



