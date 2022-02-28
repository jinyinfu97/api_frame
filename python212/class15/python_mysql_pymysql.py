# -*- coding=utf-8 -*-
# @time:2021/10/31
# @phone:15874198829
# @author:码尚教育_星瑶
import pymysql

"""
pymysql对数据库的常用操作：
1、创建数据库的连接对象
2、创建游标对象
3、通过游标对象执行sql语句并获取执行结果
"""


class mysql_operate:
    def __init__(self, host, user, passwd, database):
        self.mycon = pymysql.connect(host=host,
                                     user=user,
                                     passwd=passwd,
                                     database=database)
        self.mycursor = self.mycon.cursor()

    def creat_database(self, name):
        try:
            self.mycursor.execute(f"create database {name}")
            self.mycursor.execute("show databases")
        except Exception as erro:
            print(f'创建数据库失败，失败原因为{erro}')
        return name

    #
    # def conect_mysql(*args, **kwargs):
    #     my_con = pymysql.connect(*args, **kwargs)
    #     return my_con

    def create_tabale(self, sql):
        try:
            self.mycursor.execute(sql)
            print('创建表成功！')
        except Exception as erro:
            print(f'创建表失败，失败原因为{erro}')

    def select_sql(self, sql):
        try:
            self.mycursor.execute(sql)
            all = self.mycursor.fetchall()
            print(f'查询结果为：{all}')
        except Exception as erro:
            print(f'查询语句执行失败，失败原因为{erro}')

    def insert_sql(self, tablename, datatype: tuple, data: list):
        # 避免sql注入
        ssql = f"insert into {tablename} values{datatype}"
        sval = data
        try:
            self.mycursor.execute(ssql, sval)
            # 获取受影响的行数
            print(self.mycursor.rowcount)
            print(f'{self.mycursor.rowcount}记录插入成功')
            # 对数据进行更新（插入、删除、修改），需要进行提交
            self.mycursor.commit()
            # 回滚：取消
            # my_con.rollback()
        except Exception as erro:
            print(f'插入语句执行失败，失败原因为{erro}')
    def update_sql(self, tablename, datatype: tuple, data: list):
        # 避免sql注入
        ssql = f"update {tablename} set  values{datatype}"
        sval = data
        try:
            self.mycursor.execute(ssql, sval)
            # 获取受影响的行数
            print(self.mycursor.rowcount)
            print(f'{self.mycursor.rowcount}记录插入成功')
            # 对数据进行更新（插入、删除、修改），需要进行提交
            self.mycursor.commit()
            # 回滚：取消
            # my_con.rollback()
        except Exception as erro:
            print(f'插入语句执行失败，失败原因为{erro}')
    def execute_sql(self,method,*args,**kwargs):
        if method=='select':
            mysql_operate.select_sql(self,*args,**kwargs)
        elif method=='insert':
            mysql_operate.insert_sql(self,*args,**kwargs)
        if method=='select':
            mysql_operate.select_sql(self,*args,**kwargs)


# class test:
#         def __init__(self,name,age):
#                 self.info = f'我的姓名是{name}，我的年龄是{age}'
#         def info(self):
#                 self.info1 = self.info
#                 return 1
# a = test('jx',24)
# a.info()


# 今日作业：封装python对MySQL的操作：查询、创建表、插入数据、修改数据、删除数据
