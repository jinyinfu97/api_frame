# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/21
# @Email:2155896749@qq.com
# @File: 异常处理.py
"""
常见的异常及错误
IndentationError：缩进错误
ValueError:值错误
TypeError:类型错误
NameError: name 'value' is not defined  python变量创建时一定记得赋值
"""
# if 1==1:
#     print("right")
# # value=int("134")
# value=0
# print(value)
# value2=123
# for year in range(1900,2021):
#     print(year[0])

# 自动化测试脚本---》捕获异常  ---》记录日志  bug截图  提高脚本容错性---->定位问题
# ATM取款---》地铁卡  读卡？---》用户异常数据输入  我能够猜想  还有其他输入---》错误提示
# IndentationError
#

"""
异常处理：可以使用try except语句来捕获所有异常
语法：
 try:
	执行代码
 except:
	发生异常执行的代码
 else：
	没有异常执行的代码

"""
# atm机取款
# try:
#     uername=input("请你输入你的账号!")
#     passwd=input("请你输入你的密码!")
#     if uername=="admin" and passwd=="123456":
#         print("登录成功")
#     else:
#         print("登录失败")
#     money=int(input("请输入取款金额"))
#     print("其他步骤代码继续执行")
# except:
#     print("有异常")
# else:
#     print("请执行下一步")
#
# try:
#     uername=input("请你输入你的账号!")
#     passwd=input("请你输入你的密码!")
#     if uername=="admin" and passwd=="123456":
#         print("登录成功")
#     else:
#         print("登录失败")
#     money=int(input("请输入取款金额"))
# except Exception as error:
#     print("类型。。。。",str(error))
# else:
#     print("无异常继续执行取款的下一步操作......")

"""
try-finally 语句无论是否发生异常都将执行最后的代码。
语法格式：
 try:
	执行代码
 except:
	发生异常执行的代码
 else：
	没有异常执行的代码
 finally:
	不管有没有异常都会执行的代码

格式3：
try-finally 语句无论是否发生异常都将执行最后的代码。
语法格式：
try:    
    file1=open('2.txt')
    s=file1.readline()  
    i=int(s)
except ValueError as err2:   
    print('ValueError:{0}'.format(err2))
except OSError as err:   
    print('OSError:'.format(err))
except:   
    print('unexcept error', sys.exc_info())
finally:    
    print('这句话，无论是否异常都要执行的噢')

"""

x=10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
print("其他业务代码执行")

# python六大数据类型+控制语句if  while  for +03函数+常用模块os  time  datatime +异常处理+常见异常处理能力
# pyhthon 思维---》面向对象+自动化测试相关第三方模块使用

