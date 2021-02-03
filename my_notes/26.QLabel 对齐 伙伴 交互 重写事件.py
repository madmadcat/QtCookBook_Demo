#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  26.QLabel 对齐 伙伴 交互 实验
@description: QLabel ,重写鼠标事件，通过自定义信号实现clicked功能
"""

import sys

from PyQt5.Qt import *


class MyQLabel(QLabel):
    
    button_clicked_signal = pyqtSignal()
    
    def __init__(self, parent=None, *args, **kwargs):
        super(MyQLabel, self).__init__(parent, *args, **kwargs)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel')
        self.resize(500, 500)
        self.setup_ui()
        pass

    def setup_ui(self):
        label = QLabel('<h1>猫哥</h1>', self)
        label.resize(200, 300)
        label.move(10, 50)
        label.setStyleSheet("background-color:green;")
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        label.setMargin(20)
        print(label.textFormat())
        label.setPixmap(QPixmap('rose.png'))
        print(label.hasScaledContents())
        label.setScaledContents(True)
        print(label.hasScaledContents())
        self.label = label

        label2 = MyQLabel('可以点击的Label', self)
        label2.move(250, 400)
        label2.connect_customized_slot(self.view_control)

    def view_control(self):
        if not self.label.isHidden():
            self.label.hide()
        else:
            self.label.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
