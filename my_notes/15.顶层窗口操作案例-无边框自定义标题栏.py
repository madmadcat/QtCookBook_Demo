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
        self.setMouseTracking(True)
        self.move_flag = False
        print(self.hasMouseTracking())
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

    # QtCore.QEvent
    # def event(self, evt) -> bool:
    #     # print(evt)
    #     return super(MyFramelessWidget, self).event(evt)

    # def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
    #     pass

    def mousePressEvent(self, a0) -> None:
        # 判定点击的时候是鼠标左键
        # 在此处设置一个标记， 用作判定是否需要移动
        # 窗口的原始坐标
        # 鼠标按下的点
        # QMouseEvent
        if a0.button() == Qt.LeftButton:
            self.move_flag = True
            self.start_pos = a0.pos()
        a0.accept()
        # self.x_start = a0.localPos().x()
        # self.y_start = a0.localPos().y()
        # self.window_x_s = self.pos().x()
        # self.window_y_s = self.pos().y()
        # print(self.x_start, self.y_start)
        # print(self.window_x_s, self.window_y_s)

        # return super(MyFramelessWidget, self).mousePressEvent(a0)

    def mouseMoveEvent(self, a0) -> None:
        # if 窗口的移动标记 == True
        # 根据鼠标按下的点 计算移动向量
        # 根据移动向量，和窗口的原始坐标 = 最新坐标
        # 移动整个窗口的位置
        # Qpoint 坐标系统系统可以直接相减，性能更好
        if self.move_flag:
            # self.x_end = a0.localPos().x()
            # self.y_end = a0.localPos().y()
            #
            # x_dis = self.x_end - self.x_start
            # y_dis = self.y_end - self.y_start
            #
            # window_x_e = self.window_x_s + x_dis
            # window_y_e = self.window_y_s + y_dis
            Qpoint_window_end = self.pos() + a0.pos() - self.start_pos
            self.move(Qpoint_window_end)
        a0.accept()

        # return super(MyFramelessWidget, self).mouseMoveEvent(a0)

    def mouseReleaseEvent(self, a0) -> None:
        # 把这个标记，进行重置 False
        self.move_flag = False
        # return super(MyFramelessWidget, self).mouseReleaseEvent(a0)
        a0.accept()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # QWidget()
    window = MyFramelessWidget()
    window.show()
    sys.exit(app.exec_())
