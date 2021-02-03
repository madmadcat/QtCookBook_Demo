#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/1
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  19.按钮和菜单
@description: $描述$
"""
from PyQt5.Qt import *
import sys

class MyWindow(QWidget):
    """
    实现右键菜单的上下文的一种方法，需要重写上下文菜单事件
    """
    def contextMenuEvent(self, a0) -> None:
        print('上下文事件')

        menu = QMenu(self)

        new_action = QAction()
        new_action.setText('新建')
        new_action.setIcon(QIcon('setting-100.png'))
        new_action.triggered.connect(lambda: print('new file'))

        menu.addAction(new_action)

        open_action = QAction(QIcon('xxx.png'), '打开', menu)
        open_action.triggered.connect(lambda: print('打开文件'))
        open_recent_menu = QMenu('最近打开', menu)

        file_action = QAction('111222--333')

        menu.addAction(open_action)
        menu.addMenu(open_recent_menu)
        open_recent_menu.addAction(file_action)
        menu.addSeparator()

        exit_action = QAction(QIcon('xxx.png'), '退出', menu)
        exit_action.triggered.connect(lambda: print('退出程序'))
        menu.addAction(exit_action)

        # 运行菜单控件，传入桌面的globalPos()
        menu.exec_(a0.globalPos())


app = QApplication(sys.argv)

# 控件操作
# 创建控件
window = MyWindow()
# 设置控件
window.setWindowTitle('button and menu')
window.resize(500, 500)
btn = QPushButton('文件', window)
menu = QMenu()

new_action = QAction()
new_action.setText('新建')
new_action.setIcon(QIcon('setting-100.png'))
new_action.triggered.connect(lambda: print('new file'))

menu.addAction(new_action)

open_action = QAction(QIcon('xxx.png'), '打开', menu)
open_action.triggered.connect(lambda: print('打开文件'))
open_recent_menu = QMenu('最近打开', menu)

file_action = QAction('111222--333')

menu.addAction(open_action)
menu.addMenu(open_recent_menu)
open_recent_menu.addAction(file_action)
menu.addSeparator()

exit_action = QAction(QIcon('xxx.png'), '退出', menu)
exit_action.triggered.connect(lambda: print('退出程序'))
menu.addAction(exit_action)
btn.setMenu(menu)
# 菜单对象是QWidget的子类，可以独立显示
# btn.showMenu()
# 展示控件

def show_menu(point):
    # 实现右键菜单的上下文的另一种方法，设置policy之后将不会触发上下文event
    # window.setContextMenuPolicy(Qt.CustomContextMenu)
    # 内置方法会传递一个QPoint参数, 此参数是相对于控件的相对坐标, 需要进行global映射
    # window.customContextMenuRequested.connect(show_menu)
    print('自定义上下文菜单')
    menu = QMenu()

    new_action = QAction()
    new_action.setText('新建')
    new_action.setIcon(QIcon('setting-100.png'))
    new_action.triggered.connect(lambda: print('new file'))

    menu.addAction(new_action)

    open_action = QAction(QIcon('xxx.png'), '打开', menu)
    open_action.triggered.connect(lambda: print('打开文件'))
    open_recent_menu = QMenu('最近打开', menu)

    file_action = QAction('111222--333')

    menu.addAction(open_action)
    menu.addMenu(open_recent_menu)
    open_recent_menu.addAction(file_action)
    menu.addSeparator()

    exit_action = QAction(QIcon('xxx.png'), '退出', menu)
    exit_action.triggered.connect(lambda: print('退出程序'))
    menu.addAction(exit_action)

    # 运行菜单控件，传入桌面的globalPos()
    # point 处理相对坐标为桌面绝对坐标
    dest_point = window.mapToGlobal(point)
    menu.exec_(dest_point)


window.setContextMenuPolicy(Qt.CustomContextMenu)
# 内置方法会传递一个QPoint参数, 此参数是相对于控件的相对坐标
window.customContextMenuRequested.connect(show_menu)
window.show()
# 执行应用程序，进入消息循环
sys.exit(app.exec())