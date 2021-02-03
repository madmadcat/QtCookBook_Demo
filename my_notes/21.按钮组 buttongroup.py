#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/1
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  21.按钮组 buttongroup
@description: $描述$
"""
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

# 控件操作
# 创建控件
window = QWidget()
# 设置控件
window.setWindowTitle('按钮组的使用')
window.resize(500, 500)

# 创建四个单选按钮 ，男/女/是/否
r_male = QRadioButton('男', window)
r_female = QRadioButton('女', window)
r_male.move(100, 100)
r_female.move(100, 150)

# 创建按钮组
sex_group = QButtonGroup(window)
sex_group.addButton(r_male)
sex_group.addButton(r_female)
sex_group.setId(r_male, 5)

def test(val):
    print(val)
#buttonClicked 支持两种参数， button对象 或者 buttonID，在连接信号时可以通过下面的例子进行选择
sex_group.buttonClicked[int].connect(test)

r_yes = QRadioButton('yes', window)
r_no = QRadioButton('no', window)
r_yes.move(300, 100)
r_no.move(300, 150)

answer_group = QButtonGroup(window)
answer_group.addButton(r_yes)
answer_group.addButton(r_no)
# 按钮组是抽象概念，无法实时layout

r_a = QRadioButton('aaa', window)
r_b = QRadioButton('bbb', window)
r_a.move(400, 100)
r_b.move(400, 150)
layout_ab = QVBoxLayout()
layout_ab.addWidget(r_a)
layout_ab.addWidget(r_b)
ab_groupbox = QGroupBox('GroupBox', window)
ab_groupbox.setLayout(layout_ab)
# 父组件会被设定为layout
print(r_a.parent())

layout_sex = QHBoxLayout()
# layout_sex.addWidget(sex_group)
# layout_sex.addWidget(answer_group)


# 展示控件
window.show()
# 执行应用程序，进入消息循环
sys.exit(app.exec())