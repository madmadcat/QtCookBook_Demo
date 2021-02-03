#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:
@email: 12919662@qq.com
@file:  24.QDialog-打开文件对话框的应用
@description: $描述$
"""
import sys

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog-打开文件对话框')
        self.resize(500, 500)
        btn = QPushButton('Test', self)
        btn.clicked.connect(self.test)
        self.setup_ui()

    def setup_ui(self):
        # 用静态方法建立文件对话框
        # 打开一个文件
        # result = QFileDialog.getOpenFileName(
        #     self,
        #     "选择一个文件",
        #     "./",
        #     "All(*.*);;Image(*.png);;Python文件(*.py)",
        #     "Python文件(*.py)")

        # 打开多个文件
        # result = QFileDialog.getOpenFileNames(
        #     self,
        #     "选择一个py文件",
        #     "./",
        #     "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)",
        #     "Python文件(*.py)")

        # # 打开1个URL文件地址，需要提前构造QUrl对象
        # url = QUrl('./')
        # result = QFileDialog.getOpenFileUrl(
        #     self,
        #     "选择一个py文件",
        #     url,
        #     "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)",
        #     "Python文件(*.py)")

        # 打开多个URL文件地址，需要提前构造QUrl对象
        # result = QFileDialog.getOpenFileUrls(
        #     self,
        #     "选择一个py文件",
        #     QUrl('./'),
        #     "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)",
        #     "Python文件(*.py)")

        # 保存一个文件
        # result = QFileDialog.getSaveFileName(
        #     self,
        #     "选择一个文件",
        #     "./",
        #     "All(*.*);;Image(*.png);;Python文件(*.py)",
        #     "Python文件(*.py)")

        # 获取文件夹, 返回结果不再是一个元祖，而是一个字符串
        # result = QFileDialog.getExistingDirectory(
        #     self,
        #     "选择一个文件",
        #     "./"
        #     )
        # 获取文件夹URL, 返回一个QUrl对象
        # result = QFileDialog.getExistingDirectoryUrl(
        #     self,
        #     "选择一个文件",
        #     QUrl("./")
        #     )
        pass

    def test(self):
        fd = QFileDialog(
            self,
            '选择一个文件',
            './',
            "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)"
        )

        # 利用内建信号获得文件string
        fd.fileSelected.connect(lambda file:print(file))

        # 设置为保存文件
        # fd.setAcceptMode(QFileDialog.AcceptSave)
        # 设置默认后缀
        # fd.setDefaultSuffix("txt")
        # 选择文件夹
        # fd.setFileMode(QFileDialog.Directory)
        # 自定义按钮Label
        fd.setLabelText(QFileDialog.FileName, "顺哥的文件") #MAC无效
        fd.setLabelText(QFileDialog.Accept, "顺哥的接受")
        fd.setLabelText(QFileDialog.Reject, "顺哥的拒绝")#MAC无效
        fd.open()
        print('xxx')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
