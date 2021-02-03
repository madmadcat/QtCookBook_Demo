#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-01-2021/1/31
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  18.窗口交互状态案例
@description: 创建一个登陆窗口，实现标签和按钮的显示状态控制
"""

import sys

from PyQt5.Qt import *


class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('窗口交互状态实验')
        self.resize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.hide()

        self.line_edit = QLineEdit(self)
        self.line_edit.textChanged.connect(self._slot_btn_enable)

        self.btn = QPushButton('Login', self)
        self.btn.setEnabled(False)
        self.btn.clicked.connect(self._slot_btn_onclicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label,alignment=Qt.AlignCenter)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        print(self.children())

    def _slot_btn_enable(self):
        self.btn.setEnabled(True)

    def _slot_btn_onclicked(self):
        if self.line_edit.text() == 'xDong':
            self.label.setVisible(True)
            self.label.setText('登录成功')
        else:
            self.label.setVisible(True)
            self.label.setText('登录失败')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
