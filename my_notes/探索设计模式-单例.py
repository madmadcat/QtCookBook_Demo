#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021 01 27
# Author: xDong@wandtec


class ControlPanel(object):
    """
    使用new方法实现一个简单的单例模式
    """
    __singleton = None

    def __init__(self, pos):
        self.pos = pos
        print('用户从', pos, '打开了控制面板')

    def __new__(cls, *args, **kwargs):
        if cls.__singleton is None:
            obj = object.__new__(cls) #__new__方法的参数是类 这个对象。
            cls.__singleton = obj
            
            print(cls.__singleton)
        return cls.__singleton

    def network_setting(self, name):
        print('用户设置了新的网卡', name)


c1 = ControlPanel('北京')
c2 = ControlPanel('上海')
c3 = ControlPanel('深圳')             
print(c1, c2, c3)
c1.network_setting('虚拟网卡')
c2.network_setting('无线网卡')
c3.network_setting('USB网卡')
