# -*- coding=utf-8 -*-
# @time:2021/10/10
# @phone:15874198829
# @author:码尚教育_星瑶
import traceback
"""
1、异常处理,可以使用try except语句来捕获所有异常

    语法结构：
     try:
        执行代码
     except:
        发生异常执行的代码
     else：
        没有异常执行的代码
    
    try:
        执行代码
     except:
        发生异常执行的代码
    
     try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass

2、raise 抛出异常
    场景使用：根据程序需要，需要主动抛出异常，中断代码的执行
    
3、import traceback 常看异常

"""

"""
根据用户的输入，求和
"""

def sum(*args):
    try:
        sum=0
        for num in args:
            sum+=num
    except:
        print("输入的不是数字")
    else:
        print(f"求和：{sum},计算完成")
    finally:

        print("sum函数执行完成")

sum(2,3,1)
sum('a','b',1)

"""
使用8/用户输入的整数，并且输出结果
"""

def func2():
    try:
        num=int(input("请输入一个整数的除数:"))
        value=8/num
        print(f"8/{num}={value}")
    except ZeroDivisionError:
        print("除数不能为0")
    except ValueError:
        print("请输入正确的格式，除数必须是一个整数")
    except Exception as result:
        print(f"未知错误：{result}")


# func2()

"""
用户密码长度小于8，抛出异常
"""

def input_passwd():
    pwd=input("请输入密码：")
    if len(pwd)>8:
        return pwd
    ex=Exception("密码长度不对，密码长度不能小于8")
    raise ex

# num=2/2
# raise  Exception("我想休息了")


"""
traceback 常看异常
print_exc()  打印异常信息
format_exc()  返回异常信息
"""
"""打印异常"""
try:
    1/0
except:
    traceback.print_exc(file=open('error.txt',"w+"))
    # 返回异常信息
    error=traceback.format_exc()
    print("代码异常信息：\n",error)

