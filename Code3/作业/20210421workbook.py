# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/21
# @Email:2155896749@qq.com
# @File: 20210421workbook.py
"""
11、计算1900年1月1日到今天(如：2021年4月21日)相距多少天。
"""
days=0
# 1900年~2021年 总共多少  闰年+366天  非闰年+365   ----》for while
#
for year in range(1900,2021):
    print(year,type(year))
    #判断year是否是闰年还是非闰年 ---》判断闰年规则？
    #闰年--->能被4整除 不能被100整除 或者能把被400整除
    if (year%4==0 and year%100!=0)  or year%400==0:
        print(year,"闰年")
        days+=366
    else:
        print(year,"平年")
        days += 365
print(days)
# 到2021年今日   4月21号  +求每个月的添加  30  29  28  31
for month in range(1,4):
    if month in [1,3,5,7,8,10,12]:
        days+=31
    elif month==2:
        year=2021
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(year, "闰年")
            days += 29
        else:
            print(year, "平年")
            days += 28
    else:
        days+=30

days=days+21
print(f"计算1900年1月1日到今天(如：2021年4月21日)相距{days}天")



"""
4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，
不包含返回False
例如：
传入："hello world"
返回：True
"""
# 什么情况下需要返回值 什么不需要返回值
def isNullStr(zf):
    for s in zf:
        if s==" ":
            return True
    return False

zf="helloworld"
value=isNullStr(zf)
print(value)


"""

需要讲解：
15、打印如下图案： 
     *   5空格+1个*     i=0    ---》(5-i)空格+(1+2*i)个*   
    ***    4空格+3个*   i=1
   *****   3空格+5个*
  *******  2空格+7个*
 *********  1空格+9个*
 
  *******
   *****
    ***
     *
"""
for i in range(0,5):
    #输出内容规律---->(5-i)空格+(1+2*i)个*
    content=(20-i)*" "+(1+2*i)*"*"
    print(content)