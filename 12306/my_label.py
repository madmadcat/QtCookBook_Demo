#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/4
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  my_label
@description: $描述$
"""

from PyQt5.Qt import *


class MyLabel(QLabel):

    def mousePressEvent(self, ev):
        # 重写鼠标点击事件，对标签范围点击动作进行强化
        print(ev.pos())
        if ev.x() < 0 or ev.y() <= 30:
            return None

        point = QPushButton(self)
        point.resize(20, 20)
        point.move(ev.pos() - QPoint(10, 10))
        point.setStyleSheet('background-color: green; border-radius: 10px')
        point.show()

        # 点击已存在按钮，就删除他,第一个bool参数不需要使用
        point.clicked.connect(lambda _, btn=point: btn.deleteLater())

    def get_points(self):
        # 修正坐标便宜，拼接字符串
        result = ['{},{}'.format(child.x() + 10, child.y() - 20) for child in self.children() if child.inherits('QPushButton')]
        result = ','.join(result)
        print(result)
        return result

        # for child in self.children():
        #     if child.inherits('QPushButton'):
        #         print(child.pos())

    def clear_all_points(self):

        # 可以写成列表推到式
        for child in self.children():
            if child.inherits('QPushButton'):
                child.deleteLater()