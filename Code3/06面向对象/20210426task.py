# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/28
# @Email:2155896749@qq.com
# @File: 20210426task.py

# 一、
# # 1、摆放家具
# # 需求：
# # 1）房子有户型，总面积和家具名称列表     房子---》户型 属性  面积和家具名称列表
# # ?? ?新房子没有任何的家具    初始化时候特征
# # 2）家具有名字和占地面积，其中   家具对象     ----》属性：名字和占地面积
# # ?? ?床：占4平米     -  床   属性：面积
# # ?? ?衣柜：占2平面     衣柜     属性：面积
# # ?? ?餐桌：占1.5平米
# # 3）将以上三件家具添加到房子中    行为
# # 4）打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表  ---》 获取属性

# 分析对象相同属性及行为  及这些对象存在逻辑关系

class jiaju:

    def __init__(self,name,use_area):
        self.name=name
        self.use_area=use_area

    def __str__(self):
        return f"名称：{self.name}, 占比面积：{self.use_area}平米"

class House:
    #属性  面积和家具名称列表  名称
    #方法
    # 初始化数据
    jiaju_list=[]
    def __init__(self,house_type,area):
        self.house_type=house_type
        # 总面积
        self.area=area
        # 剩余面积
        self.free_area=area

    # 添加家具的方法---》house类
    def addJiaju(self,object:jiaju):
        # 添加家具对象---># jiaju_list增加元素
        if self.free_area>object.use_area:
            self.jiaju_list.append(object.name)
            self.free_area-=object.use_area
        else:
            print(f"{object.name}家具的面积太大了，无法添加，空闲面积有限")

    def __str__(self):
        return f"户型{self.house_type}总面积:{self.area} 剩余面积：{self.free_area} 家具列表：{self.jiaju_list}"



house1=House("三室两厅",128)

# 家具类的对象---》床 衣柜  餐桌  沙发
chuang1=jiaju("房间01_床",4)
print(chuang1)
yigui1=jiaju("房间01_衣柜",2)
print(yigui1)
canzhuo=jiaju("房间01_餐桌",1.5)
print(canzhuo)
shafa1=jiaju("房间01_沙发",6)

# 将以上三件家具添加到房子中   ---》行为 ---》方法  房子类  与   家具类有关联
house1.addJiaju(chuang1)
house1.addJiaju(canzhuo)
house1.addJiaju(yigui1)
house1.addJiaju(shafa1)
print(house1)


# 二、2、需求：
#      1）士兵瑞恩有一把AK47
#      2）士兵可以开火(士兵开火扣动的是扳机)
#      3）枪 能够 发射子弹(把子弹发射出去)
#      4）枪 能够 装填子弹 --增加子弹的数量

# class shibin:
#
#     def __init__(self,name,qiang):
#
#         pass
#
#     def kaihuo(self):
#         pass
#
# class qiang:
#
#     def fashe(self):
#         pass
#
#     def zhuangzidan(self):
#         pass
