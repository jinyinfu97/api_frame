# -*- coding=utf-8 -*-
# @time:2021/9/30
# @phone:15874198829
# @author:码尚教育_星瑶
"""
时间戳：是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数。
时间元组：
	t = (2018,6,24,16,56,45,0,0,0)  #(年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时<1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1>)
"""

import time

# 时间戳
print("时间戳:",time.time())

print("时间元组：",time.localtime())

# 时间戳转为时间元组time.localtime(时间戳)
time_tuple=time.localtime(1633009202)
print(time)

# 把时间元祖转换成时间戳time.mktime(t)
times=time.mktime(time_tuple)
print("时间戳:",times)

"""
字符串与时间元组相互转化
"""
time_tuple=time.strptime("2000-08-06 22:29:35",'%Y-%m-%d %H:%M:%S')
print(time_tuple)

# 时间转化为字符串
str_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(str_time)


print("年：",time.localtime()[0],time.localtime().tm_year)

