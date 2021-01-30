#!/usr/bin/env python37
# -*- coding: utf-8 -*-

from PyQt5.Qt import *
import sys


class MyWindow(QWidget):

    def mouseMoveEvent(self, a0) -> None:
        # print('我被移动了。。', a0.globalPos())
        print('我被移动了。。', a0.localPos())

        pass


app = QApplication(sys.argv)

# 控件操作
# 创建控件
window = MyWindow()

# 鼠标追踪开关。否则只有按下左键才有mouseMoveEvent()
window.setMouseTracking(True)
# 设置控件
# window.setWindowTitle('QWidget 鼠标事件')
# window.resize(500, 500)
#
# pixmap = QPixmap('setting-100.png')
# print(pixmap)
# new_pixmap = pixmap.scaled(50, 50)
# print(new_pixmap)
# # QCursor对象的用法
# cursor = QCursor(new_pixmap, 0, 0)
# window.setCursor(cursor)
#
# curr_cursor = window.cursor()
# print(curr_cursor.pos())
# curr_cursor.setPos(200, 200)

#window.unsetCursor()
#window.setCursor(Qt.BusyCursor)


# 展示控件
window.show()
# 执行应用程序，进入消息循环
sys.exit(app.exec())