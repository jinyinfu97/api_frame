# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/8
# @Email:2155896749@qq.com
# @File: yaml_action.py
import yaml

with open("yaml_5.yml","r+") as file:
    data= yaml.load(stream=file, Loader=yaml.FullLoader)
print(data)
username=data[0]["sucesslogin"]["username"]
print(username)

"""
序列化：python对象转换为数据文件进行存储及传输
"""
modules=["中文","pytest","unittest","requests","requests"]
with open("modules.yaml","w+") as file:
    yaml.dump(data=modules,stream=file,allow_unicode=True,encoding="utf-8")




