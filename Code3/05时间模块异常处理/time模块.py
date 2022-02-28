# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/21
# @Email:2155896749@qq.com
# @File: time模块.py

import time



"""
总结：time ----》处理时间 
时间戳  获取总秒数
时间元组---》9个元组  年月日...
常用函数：
获取时间元组   time.localtime()
获取时间戳 time.time()
把时间元组转化成时间戳：time.mktime(时间元组)
把时间戳转化时间元组：time.localtime(时间戳)
字符串与时间元组相互转化
时间元组-》字符串：time.strftime()  
字符串--》时间元组：time.strptime()

# Python编程中经常会用到time和datatime来处理日期和时间
# 时间戳：是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数。
#时间戳:1970年01月01日00时00分00秒到现在的总秒数

t = (2018,6,24,16,56,45,0,0,0)  
#(年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时<1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1>)

"""
# 获取获取现在的时间戳
zs=time.time()
print(zs)


# 1619010965.6694999
# 1619010991.0435
# 获取现在的时间元组
time_tuple=time.localtime()
print("获取现在的时间元组:",time_tuple)
'''
# 获取当前月份  多少号  星期几   ？
month=time_tuple.tm_mon
day=time_tuple.tm_mday
weekday=time_tuple.tm_wday
print(month,day,weekday)
#  周日 6 周六 5 周五 4 周四 3 周三 2 周二 1 周一 0
# Wed Apr 21 21:23:08 2021
print(time.asctime())
# 1619010965 转时间元组
ttup1=time.localtime(1587546210)
print(ttup1)
# 时间元组转化时间戳
secs=time.mktime(ttup1)
print("时间元组转化为时间戳time.mktime：",secs)
#字符串与时间元组相互转化
# 时间元组----》字符串
timestr=time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
print(timestr,type(timestr))
# 输出日志 报告   文件名称后面时间
filepath=f'log_{time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())}'
with open(filepath,"w+",encoding="utf-8") as file:
    file.write("笑褒 九头蛇")
# 时间格式字符串  2021/04/21 21:36:41 -----》时间？
ttup2=time.strptime(timestr,"%Y/%m/%d %H:%M:%S")
print("字符串转化时间元组time.strptime(string,format):",ttup2)
'''



