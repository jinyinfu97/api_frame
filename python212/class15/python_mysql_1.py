# -*- coding=utf-8 -*-
# @time:2021/10/31
# @phone:15874198829
# @author:码尚教育_星瑶
"""
一、Python操作mysql数据库
前期准备：
1、安装mysql数据库
2、安装客户端连接工具 navicat
3、启动mysql数据库服务
    通过管理员身份启动dos窗口：net start mysql
常用的第三库实现Python操作mysql数据库进行对应操作：
1、mysql-connector  是mysql官方提供给的驱动器
2、pymysql
二、mysql-connector基本应用
    安装：pip install mysql-connector
    1)创建数据库的连接
三、pymysql应用
    安装：pip install pymysql


"""

import mysql.connector
"""
python代码实现对数据库的查询操作
1、创建数据库的连接对象
2、创建游标对象
3、通过游标对象执行sql语句并获取执行结果
"""

def select():
    mycon=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="admin",
        database='test'
    )
    print(mycon)
    # 创建游标对象
    my_cursor=mycon.cursor()
    # 对数据库进行对应的操作
    my_cursor.execute("select * from student")
    # 打印执行sql语句的操作的结果
    # for x in my_cursor:
    #     print(x)
    #取返回结果所有的行数据
    # all=my_cursor.fetchall()
    # print(all)

    # 取返回结果第一行行数据
    one=my_cursor.fetchone()
    print(one)

    #  取返回结果n行数据
    two=my_cursor.fetchmany(2)
    print(two)

    #  取返回结果n行数据
    two=my_cursor.fetchmany(2)
    print(two)

"""
python代码实现对数据库其他操作：
创建数据库、创建表、插入数据、数据更新：
"""
def creat_database(name):
    mycon = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="admin"
    )
    my_cursor=mycon.cursor()
    my_cursor.execute(f"create database {name}")
    my_cursor.execute("show databases")
    for x in my_cursor:
        print(x)
def conect_mysql(*args, **kwargs):
    my_con=mysql.connector.connect(*args,**kwargs)
    return my_con

def create_tabale():
    my_con=conect_mysql( host="localhost",user="root",passwd="admin",database='test_212')
    my_cursor=my_con.cursor()
    my_cursor.execute("create table  userinfo(id int auto_increment primary key ,name  varchar(50),classname varchar(50)) ")

def insert():
    my_con = conect_mysql(host="localhost", user="root", passwd="admin", database='test_212')
    my_cursor = my_con.cursor()
    #避免sql注入
    ssql="insert into userinfo(username,classname) values(%s,%s)"
    sval=('N','212')
    my_cursor.execute(ssql,sval)
    # 获取受影响的行数
    print(my_cursor.rowcount)
    print(f'{my_cursor.rowcount}记录插入成功')
    #对数据进行更新（插入、删除、修改），需要进行提交
    my_con.commit()
    # 回滚：取消
    # my_con.rollback()
    my_cursor.execute("select * from userinfo ")
    all=my_cursor.fetchall()
    print(all)

"""批量插入多条记录"""
def insert_many():
    my_con = conect_mysql(host="localhost", user="root", passwd="admin", database='test_212')
    my_cursor = my_con.cursor()
    #避免sql注入
    ssql="insert into userinfo(username,classname) values(%s,%s)"
    sval=[('N1','212'),('N2','212'),('N3','212')]
    # 同时插入多条记录
    my_cursor.executemany(ssql,sval)

    #对数据进行更新（插入、删除、修改），需要进行提交
    my_con.commit()
    # 回滚：取消
    # my_con.rollback()
    # 获取受影响的行数
    print(my_cursor.rowcount)
    print(f'{my_cursor.rowcount}记录插入成功')
    my_cursor.execute("select * from userinfo ")
    all=my_cursor.fetchall()
    print(all)

if __name__ == '__main__':
    # creat_database('test_212')
    #创建表
    # create_tabale()
    #插入数据到表
    # insert()
    #插入多条数据
    insert_many()