#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/3
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  tool
@description:
"""
from PyQt5.Qt import *


class AccountTool:
    """
    验证用户名和密码
    """
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3

    @staticmethod
    def check_login(account, pwd):
        if account != 'dx':
            return AccountTool.ACCOUNT_ERROR
        if pwd != '123':
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS


class AnimationTool:
    """
    基于Qt对象，生成动画效果
    """
    @staticmethod
    def animation_pos_generator(target, start_pos, end_pos, parent, duration=1000):
        """
        生成Qt属性动画对象，动画效果基于pos变化，弹簧效果QEasingCurve.InOutBounce,
        必须绑定父控件以保证动画对象的生命周期
        :param target: QWidget
        :param start_pos: QPoint
        :param end_pos: QPoint
        :param duration: int
        :param QObject or sub-class of QObject
        :return: QAnimation object
        """
        animation = QPropertyAnimation(parent)
        animation.setTargetObject(target)
        animation.setPropertyName(b'pos')
        animation.setStartValue(start_pos)
        animation.setEndValue(end_pos)
        animation.setDuration(duration)
        animation.setEasingCurve(QEasingCurve.InOutBounce)
        return animation



