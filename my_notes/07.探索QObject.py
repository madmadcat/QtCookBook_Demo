#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/29
   Change Activity:
                   2021/1/29:
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle('')
        #self.resize(500, 300)
        self.setup_ui()

    def setup_ui(self):
        # 父子关系实验，会影响窗口部件的布局
        # self.Qobject_parent_child_api()
        # 父子关系实验，QSS样式应用场景
        # self.QObject_parent_child_scenario()
        # 信号与槽的API实验
        # self.QObject_signal_slot_apply()
        # 信号与槽在父子关系中的应用
        # self.QObject_signal_slot_scenario()
        # QObject类型判定
        # self.qobject_type()
        # 删除一个对象
        self.delete_qobj()

    def Qobject_parent_child_api(self):
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()

        obj1.setParent(obj2)
        obj3.setParent(obj2)

        print('obj1', obj1)
        print('obj2', obj3)
        print('obj3', obj3)
        print(obj2.children())

    def QObject_parent_child_scenario(self):

        # 创建一个主窗口，包含多个QWidget和QLabel，Qlabel有统一的颜色cyan

        win2 = QWidget()
        win2.move(100, 100)
        win2.setParent(self)
        win2.setStyleSheet("background: red")
        win3 = QWidget()
        win3.move(120, 120)
        win3.setStyleSheet("background: green")
        win3.setParent(self)

        self.objs = []
        for i in range(5):
            name = "btn" + str(i + 1)
            o = QLabel(name, self)
            r = 100 + (i + 1) * 80
            o.move(50, r)
            o.setObjectName(name)
            print('label is created')
            self.objs.append(o)
            i += 1

        # 利用QObject.findChildren() 去遍历所有子控件
        for sub_widget in self.findChildren(QLabel):
            sub_widget.setStyleSheet("color: cyan;background-color:blue")
            print(sub_widget)

        # TODO: 没成功
        # load QSS file and apply
        # with open('qobject_explore.qss', 'r') as f:
        #     #win1.setStyleSheet(f.read())
        #     content = f.read()
        #     app.setStyleSheet("QLable {color:cyan}")
        #     # print(f.read())

    def QObject_signal_slot_apply(self):
        # obj.destroyed
        # obj.objectNameChanged
        # obj.objectNameChanged.disconnect
        # obj.blockSignals
        # self.obj.receivers()
        self.obj = QObject()

        def slot_destroy(obj):
            print('我被释放了', obj)

        def slot_name_changed(name):
            print('名称发生改变',name)

        self.obj.destroyed.connect(slot_destroy)
        self.obj.objectNameChanged.connect(slot_name_changed)

        self.obj.setObjectName('xxXX')
        self.obj.blockSignals(True)
        # self.obj.objectNameChanged.disconnect(slot_name_changed)
        self.obj.setObjectName('ooOO')
        self.obj.blockSignals(False)
        self.obj.setObjectName('XXOO')

    def QObject_signal_slot_scenario(self):

        ###############信号与槽案例###############开始
        # 自动给窗口标题加上前缀, 利用diconnect or block来防止无限递归
        self.setWindowTitle('Hello xDong')
        self.windowTitleChanged.connect(self.slot_title_changed)

        self.setWindowTitle('ABC')
        self.setWindowTitle('DEF')
        ###############信号与槽案例###############结束

    def slot_title_changed(self, title):
        self.blockSignals(True)
        print(f'title is modified to {title} xdong2020')
        self.setWindowTitle(title + 'xdong2020')
        self.blockSignals(False)



        pass

    def qobject_type(self):
        ###############案例###############开始
        lable1 = QLabel('1111', parent=self)
        lable1.move(50, 50)
        lable2 = QLabel('2222', parent=self)
        lable2.move(50, 70)
        lable3 = QLabel('3333', parent=self)
        lable3.move(50, 90)
        btn = QPushButton('button', parent=self)
        sub_widgets = self.children()
        for widget in sub_widgets:
            print(widget)
            if widget.inherits('QLabel'):
                widget.setStyleSheet('color:cyan')
            if widget.inherits('QPushButton'):
                widget.setStyleSheet('background-color:green')
        ###############案例###############结束
        pass

    def delete_qobj(self):
    ###############删除对象的案例###############开始

    ###############删除对象的案例###############结束
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

