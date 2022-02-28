# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/4/28
# @Email:2155896749@qq.com
# @File: 多态.py

"""
多态：不同的子类对象调用相同的方法，产生不同的执行结果（呈现多种形态）
"""
# 支付方式 ：微信支付  支付宝  银联支付 ....
# 不同的类---》功能业务相同： 收款 付款   ---》相同的方法  收款 和付款方法
# 不同的类  微信支付  支付宝  银联支付  相同的方法  收款 和付款方法 实现业务不同
class wx:
    def pay(self):
        print("微信支付")

class zhifubao:
    def pay(self):
        print("支付宝支付")

class yl:
    def pay(self):
        print("银联支付")

def start_pay(object):
    object.pay()

#点了外卖--支付方式
wx_hefan=wx()
start_pay(wx_hefan)



