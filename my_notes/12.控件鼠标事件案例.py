#!/usr/bin/env python37
# -*- coding: utf-8 -*-


import sys

from PyQt5.Qt import *


class MyWidget(QWidget):
    """
    创建一个窗口，包含一个标签，使用自定义鼠标外形，并且在移动时使标签跟随鼠标的移动，并显示鼠标的当前位置
    """
    def __init__(self):
        super(MyWidget, self).__init__()
        pixmap = QPixmap('setting-100.png')
        sized_pixmap = pixmap.scaled(30, 30)
        cursor = QCursor(sized_pixmap)
        self.setCursor(cursor)

        self.label = QLabel(self)
        self.label.setText('显示鼠标的当前位置')
        self.label.adjustSize()
        self.label.setStyleSheet("background-color: green")

        self.setMouseTracking(True)

    def mouseMoveEvent(self, a0) -> None:
        print(a0)
        x = a0.localPos().x()
        y = a0.localPos().y()
        self.label.move(x, y)
        self.label.setText(str(x) + ', ' + str(y))
        return super(MyWidget, self).mouseMoveEvent(a0)
    
    def event(self, evt) -> bool:
        print(evt)
        return super(MyWidget, self).event(evt)

    pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWidget()
    window.setWindowTitle('鼠标事件Demo')
    window.resize(400, 400)

    window.show()
    sys.exit(app.exec_())
