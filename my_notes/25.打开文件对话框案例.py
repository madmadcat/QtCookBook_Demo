#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  25.打开文件对话框案例
@description: 创建一个窗口，两个按钮，一个打开文件，一个保存文件，创建一个textEdit控件，显示文件内容
"""

import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('打开文件对话框案例')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn_width = 80
        btn_height = 30
        margin = 100

        open_btn = QPushButton('打开文件', self)
        close_btn = QPushButton('保存文件', self)

        open_btn.resize(btn_width, btn_height)
        close_btn.resize(btn_width, btn_height)
        open_btn.move(margin, 20)
        close_btn.move(self.width()- margin - btn_width, 20)

        te = QPlainTextEdit(self)
        te.resize(self.width() - margin * 2, 380)
        te.move(margin, 100)

        self.open_btn = open_btn
        self.close_btn = close_btn
        self.te = te

        self.open_btn.clicked.connect(self._slot_open_file)
        self.close_btn.clicked.connect(self._slot_close_file)

    def _singal_handler(self):

        pass

    def _slot_open_file(self):
        file = None
        (file, f_type) = QFileDialog.getOpenFileName(
            self,
            '打开一个文件',
            './',
            'PythonFile(*.py)'
        )
        if file:
        # 逐行读取文件对象，将内容插入到TextEdit控件
            with open(file, 'r') as f:
                line = f.readline()
                while line:
                    print(line)
                    self.te.insertPlainText(line)
                    line = f.readline()

    def _slot_close_file(self):
        file = None
        (file, f_type) = QFileDialog.getSaveFileName(
            self,
            '文件存储为',
            './',
            'python文件(*.py)'
        )

        # 写入目标文件
        if file:
            with open(file, 'w') as f:
                try:
                    f.write(self.te.toPlainText())
                except:
                    QMessageBox.warning(self, 'Warning', '文件保存失败')
                else:
                    QMessageBox.information(self, 'Info', '文件保存成功')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

