#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/30
   Change Activity:
                   2021/1/30:

    案例描述：
    创建一个窗口，无边框，无标题栏，窗口半透明，自定义最大化最小化关闭按钮，支持拖拽用户区移动
"""

import sys

from PyQt5.Qt import *

import my_enum


class MyFramelessWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('无边框窗口实践')
        self.setWindowOpacity(0.9)
        self.resize(400, 400)
        self.setWindowFlag(Qt.FramelessWindowHint, on=True)
        self.y = 0
        self.btn_w = 69

        self.setup_ui()

    def setup_ui(self):
        # 设置窗口标志为无边框

        # 设置窗口标志为显示最大最小化按钮
        # self.setWindowFlags(Qt.WindowMinMaxButtonsHint)

        # 为窗口添加标题栏和一个关闭按钮
        # self.setWindowFlags(Qt.WindowTitleHint)

        # 添加三个子控件按钮 右上角
        # self.icon_close = QApplication.style().standardIcon(my_enum.SPIcon.SP_TitleBarCloseButton.value)
        # self.icon_max = QApplication.style().standardIcon(my_enum.SPIcon.SP_TitleBarMaxButton.value)
        # self.icon_min = QApplication.style().standardIcon(my_enum.SPIcon.SP_TitleBarMinButton.value)


        # self.btn_close = QPushButton(QIcon(self.icon_close), '', self)
        self.btn_close = QPushButton('关闭', self)

        # self.btn_max = QPushButton(QIcon(self.icon_max), '', self)
        self.btn_max = QPushButton('最大化', self)

        # self.btn_min = QPushButton(QIcon(self.icon_min), '', self)
        self.btn_min = QPushButton('最小化', self)

        self.btn_close.clicked.connect(self.close)
        self.btn_max.clicked.connect(self.slot_max)
        self.btn_min.clicked.connect(self.showMinimized)

    def slot_max(self):
        if self.isMaximized():
            self.showNormal()
            self.btn_max.setText('最大化')
        else:
            self.showMaximized()
            self.btn_max.setText('恢复')
    
    def resizeEvent(self, QResizeEvent) -> None:
        window_w = self.width()
        
        btn_close_x = window_w - self.btn_w
        self.btn_close.move(btn_close_x, self.y)

        btn_max_x = btn_close_x - self.btn_w
        self.btn_max.move(btn_max_x, self.y)

        btn_min_x = btn_max_x - self.btn_w
        self.btn_min.move(btn_min_x, self.y)
        return super(MyFramelessWidget, self).resizeEvent(QResizeEvent)
        pass
    

    def mousePressEvent(self, QMouseEvent) -> None:
        # 判定点击的时候是鼠标左键
        # 在此处设置一个标记， 用作判定是否需要移动
        # 窗口的原始坐标
        # 鼠标按下的点
        print(QMouseEvent.__dict__)
        pass

    def mouseMoveEvent(self, QMouseEvent) -> None:
        # if 窗口的移动标记 == True
        # 根据鼠标按下的点 计算移动向量
        # 根据移动向量，和窗口的原始坐标 = 最新坐标
        # 移动整个窗口的位置
        pass

    def mouseReleaseEvent(self, QMouseEvent) -> None:
        # 把这个标记，进行重置 False
        pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # QWidget()
    window = MyFramelessWidget()
    window.show()
    sys.exit(app.exec_())
