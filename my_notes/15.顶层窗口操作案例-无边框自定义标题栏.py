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
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('无边框窗口实践')
        self.setWindowOpacity(0.9)
        self.resize(400, 400)
        # 设置窗口标志为无边框
        self.setWindowFlag(Qt.FramelessWindowHint, on=True)

        # 设置窗口标志为显示最大最小化按钮
        # self.setWindowFlags(Qt.WindowMinMaxButtonsHint)

        # 为窗口添加标题栏和一个关闭按钮
        self.setWindowFlags(Qt.WindowTitleHint)

        # 添加三个子控件按钮 右上角
        icon_close = QApplication.style().standardIcon(my_enum.SPIcon.SP_TitleBarCloseButton.value)
        icon_max = QApplication.style().standardIcon(my_enum.SPIcon.SP_TitleBarMaxButton.value)
        icon_min = QApplication.style().standardIcon(my_enum.SPIcon.SP_TitleBarMinButton.value)

        y = 0
        btn_w = 70
        btn_close = QPushButton(QIcon(icon_close), '', self)
        # btn_close = QPushButton('关闭', self)

        btn_close_w = btn_close.width()
        window_w = self.width()
        # btn_close_x = window_w - btn_close_w
        btn_close_x = window_w - btn_w
        btn_close.move(btn_close_x, y)
        print(btn_close.rect())
        print(btn_close.minimumSizeHint())
        print(btn_close_w)
        print('btnclos x', btn_close_x)
        btn_max = QPushButton(QIcon(icon_max), '', self)
        btn_max_x = btn_close_x - btn_w
        btn_max.move(btn_max_x, y)
        print('btnmax x', btn_max_x)

        btn_min = QPushButton(QIcon(icon_min), '', self)
        btn_min_x = btn_max_x - btn_w
        btn_min.move(btn_min_x, y)
        print('btnmin x', btn_min_x)

        btn_close.clicked.connect(self.close)
        btn_max.clicked.connect(self.showMaximized)
        btn_min.clicked.connect(self.showMinimized)
    pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # QWidget()
    window = MyFramelessWidget()
    window.show()
    sys.exit(app.exec_())
