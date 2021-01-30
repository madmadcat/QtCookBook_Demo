#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021年1月31日
@author: Golden
@site:
@email: 12919662@qq.com
@file:
@description: 两个窗口交互的实验
"""

import sys
from PyQt5.Qt import *


class ControllerWindow(QWidget):

    def __init__(self):
        super(ControllerWindow, self).__init__()
        self.setWindowTitle('主窗口')
        self.resize(400, 400)
        self.sub_window = SubWindow()

        btn1 = QPushButton('OPEN副窗口')
        btn1.clicked.connect(self.update_view)

        btn2 = QPushButton('Close')
        btn2.clicked.connect(self.close)

        btn3 = QPushButton('print')
        btn3.clicked.connect(self.print_text)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)
        self.update_view()

    def update_view(self):
        text = self.sub_window.get_text()
        print(text)
        self.sub_window.show()

    def print_text(self):
        print(self.sub_window.get_text())
    
    def closeEvent(self, a0) -> None:
        sys.exit(0) # 主窗口关闭时 会关闭所有子窗口
        return super(ControllerWindow, self).closeEvent(a0)

class SubWindow(QWidget):

    def __init__(self, parent=None):
        super(SubWindow, self).__init__(parent)

        self.lineedit = QLineEdit()

        btn = QPushButton('close')
        btn.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.lineedit)
        layout.addStretch()
        layout.addWidget(btn, 0, alignment=Qt.AlignBottom)
        self.setLayout(layout)

    def get_text(self):
        return self.lineedit.text()

    def set_text(self, info):
        self.lineedit.setText(info)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = ControllerWindow()
    w.show()
    sys.exit(app.exec_())
