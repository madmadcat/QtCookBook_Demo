#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  30.QBoxLayout功能作用
@description: $描述$
"""
import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QBboxLayout')
        self.resize(500, 500)
        self.setup_ui()
        pass

    def setup_ui(self):
        lb1 = QLabel('Label1')
        lb2 = QLabel('Label2')
        lb3 = QLabel('Label3')
        lb4 = QLabel('Label4')
        lb1.setStyleSheet('background-color:cyan')
        lb2.setStyleSheet('background-color:green')
        lb3.setStyleSheet('background-color:red')
        lb4.setStyleSheet('background-color:yellow')

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(lb1)
        # layout.addSpacing(100)
        layout.addStretch(0)
        layout.addWidget(lb2)
        # layout.addStretch(1)
        # layout.addWidget(lb3, 1 )
        # layout.addWidget(lb4)

        # layout.addWidget(lb4)

        self.setLayout(layout)

        # timer = QTimer(self)
        #
        # lb5 = QLabel('Label5')
        # lb6 = QLabel('Label6')
        # lb7 = QLabel('Label7')
        # lb5.setStyleSheet('background-color:pink')
        # lb6.setStyleSheet('background-color:blue')
        # lb7.setStyleSheet('background-color:gold')
        #
        # sub_layout = QBoxLayout(QBoxLayout.TopToBottom)
        # sub_layout.addWidget(lb5)
        # sub_layout.addWidget(lb6)
        # sub_layout.addWidget(lb7)
        #
        # layout.insertLayout(2, sub_layout)
        # print(layout.indexOf(lb3))
        # layout.insertSpacing(layout.indexOf(lb3), 100)
        # # layout.insertSpacing()
        # # lb2.hide()

        # self.setContentsMargins(20, 20, 20, 20)
        # # ---------------------------------------------------------------------------
        # # 每秒切换一个layout方向
        # # ---------------------------------------------------------------------------
        #
        # def test():
        #     layout.setDirection((layout.direction() + 1) % 4)
        #     pass
        # timer.timeout.connect(test)
        # timer.start(1000)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
