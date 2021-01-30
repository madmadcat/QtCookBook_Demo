#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/30
   Change Activity:
                   2021/1/30:

    没有父控件的窗口默认是顶层窗口，拥有一个特定操作。

    setWindowTitle
    windowTitle
    setWindowIcon
    windoIcon

    WindowState
    Qt.WindowNoState , Qt.WindowActive , Qt.Min.. , Qt.Max..

    最大化 最小化 状态显示和控制
    showFullScreen() isFullScreen() / min / max
"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

# 控件操作
# 创建控件
window = QWidget()
# 设置控件
window.resize(500, 500)

icon = QIcon('setting-100.png')
window.setWindowIcon(icon)

window.setWindowOpacity(0.8)

# 展示控件
# window.showFullScreen()
window.show()
# 执行应用程序，进入消息循环
sys.exit(app.exec())
