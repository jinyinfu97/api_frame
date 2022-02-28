# 1.编写装饰器，为多个函数加上认证的功能，
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

# FALG = False
# def login(user,passwprd):
#     with open('admin',mode='r',encoding='utf-8') as f:
#         if f.readline().strip()== user and f.readline().strip() == passwprd:
#             return True
#         return False
# def wrapper(func):
#     def inner(*args,**kwargs):
#         global FALG
#         if FALG:
#             ret = func(*args,**kwargs)
#         else:
#             user = input("输入用户名")
#             password = input("输入密码")
#             if login(user,password):
#                 print('登录成功')
#                 func(*args, **kwargs)
#                 FALG =True
#                 return
#             else :
#                 print('登录失败')
#                 return
#         return ret
#     return inner
# @wrapper
# def shop_add():
#     print('增加一个商品')
# @wrapper
# def shop_del():
#     print('删除一件商品')
# shop_add()
# shop_del()
# shop_del()
# shop_del()


# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用都将被调用的函数名写入文件

# def warpper(func):
#     def inner(*args,**kwargs):
#         with open('log',mode='a',encoding='utf-8') as f:
#             f.write(func.__name__+'\n')
#         ret  = func(*args,**kwargs)
#         return ret
#     return inner
#
# @warpper
# def shop_add():
#     print('增加一个商品')
# @warpper
# def shop_del():
#     print('删除一件商品')
# shop_add()
# shop_del()
# shop_del()
# shop_del()

# ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))
import random
import string

print(''.join("123"))
print (''.join(random.choice(string.ascii_letters + string.digits) for i in range(2)))
print(type(random.choice("123") for n in range(2)))
print(''.join("123" for m in range(2)))