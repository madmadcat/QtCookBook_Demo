#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/30
   Change Activity:
                   2021/1/30:
"""
import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    """创建两个标签，鼠标点击谁，就将谁放置在顶层"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('父控件控制子控件层级关系')
        self.resize(500, 500)

        QMouseEvent

    def mousePressEvent(self, evt) -> None:
        x = evt.x()
        y = evt.y()

        sub_widget = self.childAt(x, y)
        if sub_widget:
            sub_widget.raise_()
        return super(MyWindow, self).mousePressEvent(evt)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()

    label1 = QLabel(window)
    label1.setText('我是绿色')
    label1.resize(200, 200)
    label1.setStyleSheet('background-color: green')
    label1.move(50, 50)

    label2 = QLabel(window)
    label2.setText('我是红色')
    label2.resize(200, 200)
    label2.setStyleSheet('background-color: red')
    label2.move(150, 150)

    w2 = QWidget()
    w2.resize(300, 300)
    w2.move(500, 600)
    w2.show()


    window.show()
    sys.exit(app.exec_())
