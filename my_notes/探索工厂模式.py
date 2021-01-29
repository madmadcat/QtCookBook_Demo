# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     探索简单工厂模式
   Description :
   Author :       xdong
   date：          2021/1/27
-------------------------------------------------
   Change Activity:
                   2021/1/27:
-------------------------------------------------
"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # 抽象产品
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    # 具体产品
    def pay(self, money):
        print(f'支付宝支付{money}元')


class Huabei(Payment):
    # 具体产品
    def pay(self, money):
        print(f'花呗支付{money}元')

class WxPay(Payment):
    # 具体产品
    def pay(self, money):
        print(f'微信支付{money}元')

# 工厂方法模式
# 定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类
# 角色：
#       抽象工厂
#       具体工厂
#       抽象产品
#       具体产品
class PaymentFactory(metaclass=ABCMeta):
    # 抽象工厂
    @abstractmethod
    def create_payment(self):
        pass

class  AlipayFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        obj = AliPay()
        return obj

class HuabeiFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        return Huabei()

class  WxpayFactory(PaymentFactory):
    # 具体工厂
    def create_payment(self):
        obj = WxPay()
        return obj

# client
pf1 = AlipayFactory()
pf2 = HuabeiFactory()
pf3 = WxpayFactory()

p1 = pf1.create_payment()
p3 = pf2.create_payment()
p2 = pf3.create_payment()


# class PaymentFactory():
#     """简单工厂模式
#     根据方法返回不同payment对象，对client透明封装创建对象的复杂度
#     """
#     def create_payment(self, method):
#         if method == 'alipay':
#             return AliPay()
#         elif method == 'huabei':
#             return AliPay(use_huabei=True)
#         elif method == 'wxpay':
#             return WxPay()
#         else:
#             raise TypeError('No such payment named {}'.format(method))



p1.pay(100)
p2.pay(80)
p3.pay(99.2)