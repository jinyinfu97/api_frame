# -*- coding=utf-8 -*-
# @time:2021/10/10
# @phone:15874198829
# @author:码尚教育_星瑶
"""
calendar Python内置模块 ，返回年/月历
"""
import calendar
import datetime


""""打印年历"""
print(calendar.calendar(2021))

"""打印月历"""
print(calendar.month(2021, 10))

"""是否为闰年"""
print(calendar.isleap(2021))

"""
返回日期是周几
周一  0
周二  1
....
周日  6
"""
print(calendar.weekday(2021, 10, 11))
print(datetime.datetime(2021, 10, 10).weekday())

