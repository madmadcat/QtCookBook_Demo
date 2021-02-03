#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/1
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  20.Toolbutton工具按钮
@description: 探索工具按钮的使用
"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

# 控件操作
# 创建控件
window = QWidget()
# 设置控件
window.setWindowTitle('ToolButton')
window.resize(500, 500)

btn = QToolButton(window)
btn.setText('Tool')

# # 工具按钮设置图标后默认不会显示text
# btn.setText('setting')
# btn.setIcon(QIcon('close.png'))
# btn.setIconSize(QSize(60, 60))
# btn.setToolTip('setting')
#
# # 设置工具按钮风格，5个枚举类型
btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# 工具按钮的箭头风格实验
# Qt.NoArrow
# 	无箭头
# Qt.UpArrow
# 	向上箭头
# Qt.DownArrow
# 	向下箭头
# Qt.LeftArrow
# 	向左箭头
# Qt.RightArrow
# 	向右箭头
btn.setArrowType(Qt.RightArrow)
btn.setAutoRaise(True)
print(btn.autoRaise())
menu = QMenu(btn)
sub_menu = QMenu(menu)
sub_menu.setTitle('new')

action = QAction('open', menu)
action.setData((1, 2, 3))
action.triggered.connect(lambda :print('lalala'))
menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action)

btn.setMenu(menu)
# 更改弹出方式
btn.setPopupMode(QToolButton.MenuButtonPopup)
# 工具菜单会触发action，利用其特性可以获得菜单中的action数据
# action.setData()
# action.data()
def do_action(action):
    print(action.data())
    print('tool button is clicked')
btn.triggered.connect(do_action)

# btn2 = QPushButton('一般按钮', window)
# btn2.move(0, 200)
# btn2.setFlat(True)
#
# menu = QMenu(btn2)
# sub_menu = QMenu(menu)
# sub_menu.setTitle('new')
#
# action = QAction('open', menu)
# action.triggered.connect(lambda :print('lalala'))
# menu.addMenu(sub_menu)
# menu.addSeparator()
# menu.addAction(action)
#
# btn2.setMenu(menu)
# 展示控件
window.show()
# 执行应用程序，进入消息循环
sys.exit(app.exec())