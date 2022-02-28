# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/8
# @Email:2155896749@qq.com
# @File: ini_action.py

"""
一、后缀名.ini  用于存储项目全局配置变量
比如：接口地址  项目地址....输出文件路径

"""
import configparser

config=configparser.ConfigParser()
config.read("config.ini",encoding="utf-8")
# 获取ini文件中所有的节点
sections=config.sections()
# 获取ini文件中某个节点下所有选项
options=config.options(section="database")
# 获取某个节点下某个选项的选项值
value=config.get(section="database",option="username")
# 获取某个节点下的所有选项及选项值  ---》元组列表
values=config.items(section="database")
print(sections)
print(options)
print(values)
print(value)

"""
ini文件编辑：
1、写入一个节点
2、写入选项及选项值
3、删除节点
4、删除选项及选项值
"""
# 写入一个节点
new_section="userinfo1"
if new_section not in sections:
    config.add_section("userinfo1")
# 给某个节点添加选项及选项值
    config.set(section="userinfo1",option="username",value="hefan")
    config.set(section="userinfo1",option="passwd",value="hefan")
    # file=open("config.ini","w+")
    # config.write(file)
    # file.close()
    with open("config.ini","w+") as file:
        config.write(file)

# 删除节点
del_section="userinfo1"
print(sections)
if del_section in sections:
    config.remove_section(section=del_section)
    with open("config.ini","w+") as file:
        config.write(file)
# 删除选项及选项值
config.remove_option(section="userinfo",option="passwd")
with open("config.ini","w+") as file:
    config.write(file)

