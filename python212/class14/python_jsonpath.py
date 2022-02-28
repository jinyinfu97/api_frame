# -*- coding=utf-8 -*-
# @time:2021/10/28
# @phone:15874198829
# @author:码尚教育_星瑶
"""
常用模块：jsonpath
1、作用：对json文本/字典数据进行信息提取
2、什么是json？
    json类似字典，不是字典
    json是结构类似于字典的字符串
3、jsonpath常见的特殊符号
    $  根节点
    .. 选择所有符号条件（模糊匹配）
    * 匹配所有的元素节点
    @  当前节点
    ?()  过滤表达式

"""
import json
import jsonpath

d={
    "error_code":0,
    "stu_info":
    [
        {"id":223,
      "name":"null",
      "sex":"女",
      "classname":"212期"
      },
     {"id": 224,
      "name": "景龙",
      "sex": "男",
      "classname": "212期"
      },
{"id": 225,
      "name": "MS226",
      "classname": "212期"
      }
    ]
}
print(type(d))
name=d["stu_info"][0]["name"]
print(name)


# 模糊匹配  匹配所有学员name
data1=jsonpath.jsonpath(d,"$..name")
print("匹配所有学员name：",data1)


# 精确匹配
# 获取null的值  匹配第一个学员name
data3=jsonpath.jsonpath(d,"$.stu_info[0].name")
print("匹配第一个学员name:",data3)

#  匹配第一个学员name
data4=jsonpath.jsonpath(d,"$.stu_info[0]..name")
print("匹配第一个学员name:",data4)

#匹配前两个学员的信息
data=jsonpath.jsonpath(d,"$.stu_info[:2]")
print("匹配前两个学员的信息：",data)

data5=jsonpath.jsonpath(d,"$.stu_info[?(@.sex=='女')]")
print("匹配性别为女的学生信息:",data5)

data6=jsonpath.jsonpath(d,"$.stu_info[?(@.sex)]")
print("匹配包含性别列的学生信息:",data6)

"""
jsonpath模块处理json数据
"""
json_data='{"name":"冷水","id":"242"}'
print(type(json_data))
# json数据进行转化，转化字典 反序列化
d2=json.loads(json_data)
print(type(d2))
print(jsonpath.jsonpath(d2, '$.id'))
