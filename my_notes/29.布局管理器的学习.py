#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  29.布局管理器的学习
@description: 布局管理器的学习
"""

import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('布局管理器的学习')
        self.resize(500, 500)
        self.setup_ui()
        pass

    def setup_ui(self):
        lb1 = QLabel('Label1')
        lb2 = QLabel('Label2')
        lb3 = QLabel('Label3')
        lb1.setStyleSheet('background-color:cyan')
        lb2.setStyleSheet('background-color:green')
        lb3.setStyleSheet('background-color:red')
        lb4 = QLabel('Label4')
        lb4.setStyleSheet('background-color:yellow')
        # 1.创建布局管理器对象
        layout = QBoxLayout(QBoxLayout.BottomToTop)
        # 2.添加子控件
        layout.addWidget(lb1)
        layout.addWidget(lb2)
        layout.addWidget(lb3)

        layout.setSpacing(20)
        layout.replaceWidget(lb2, lb4)

        # ---------------------------------------------------------------------------
        # hide一个对象并不会删除它，正确的做法是setParent(None)
        # ---------------------------------------------------------------------------

        lb2.setParent(None)
        lb2.destroyed.connect(lambda obj:print(obj, 'lb2 is deleted'))
        # layout.setContentsMargins(20, 20, 20, 20)
        # 3.把布局管理器设置给需要布局的父控件
        self.setLayout(layout)

        # ---------------------------------------------------------------------------
        # 布局的嵌套
        # ---------------------------------------------------------------------------
        lb5 = QLabel('Label5')
        lb6 = QLabel('Label6')
        lb7 = QLabel('Label7')
        lb5.setStyleSheet('background-color:pink')
        lb6.setStyleSheet('background-color:blue')
        lb7.setStyleSheet('background-color:gold')

        sub_layout = QBoxLayout(QBoxLayout.LeftToRight)
        sub_layout.addWidget(lb5)
        sub_layout.addWidget(lb6)
        sub_layout.addWidget(lb7)

        layout.addLayout(sub_layout)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
