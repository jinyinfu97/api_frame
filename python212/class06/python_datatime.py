# -*- coding=utf-8 -*-
# @time:2021/9/30
# @phone:15874198829
# @author:码尚教育_星瑶

import  datetime

# 获取某日期时间
dt=datetime.datetime(2018,6,24,16,56,45,13) #(年、月、日、时、分、秒、微秒) #以时间元祖创建
# 获取现在日期时间
dt2=datetime.datetime.today()  #获得当前时间datetime
dt3=datetime.datetime.now()    #获得当前时间datetime
print(dt,type(dt))
print(dt2,type(dt2))
print(dt3,type(dt3))

"""
时间日期与时间戳的相互转化
"""
# 日期转化为时间戳
times=dt.timestamp()
print("时间戳：",times)

#时间戳转日期
data1=datetime.datetime.fromtimestamp(1529830605.000013)
print(f"时间戳{data1}转日期",data1)

"""
字符串与日期的相互转化
"""
# 日期转字符串
dt=datetime.datetime(2018,6,24,16,56,45,13)
str_time=dt.strftime('%Y-%m-%d %H:%M:%S')
print(" 日期转字符串:",str_time)

# 字符串转日期
dt=datetime.datetime.strptime('2015-6-1 18:19:59.10', '%Y-%m-%d %H:%M:%S.%f')
print("字符串转日期:",dt)
