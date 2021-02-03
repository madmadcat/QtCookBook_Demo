#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  28.QMessageBox 模态对话框
@description: $描述$
"""

import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('学习MessageBox')
        self.resize(500, 500)
        self.setup_ui()
        pass

    def setup_ui(self):
        # QMessageBox.about(self, 'xx1', 'xx2')
        # QMessageBox.aboutQt(self, 'xx1')
        # 静态方法
        QMessageBox.question(self, 'xx1', 'xx2', QMessageBox.Ok | QMessageBox.Reset)

    # ---------------------------------------------------------------------------
    # 下面的代码不要
    # ---------------------------------------------------------------------------
    

        return None
        # mb = QMessageBox(self)
        # mb = QMessageBox(QMessageBox.Warning, 'xxx', 'ooo', QMessageBox.Ok | QMessageBox.Discard, self)
        # 可以通过参数设置为非模态对话框
        # mb.setWindowModality(Qt.NonModal)
        # mb.setModal(False)
        mb = QMessageBox(self)
        mb.setWindowTitle('消息提示')
        mb.setIconPixmap(QPixmap('setting-100.png').scaled(50, 50))
        mb.setText('<h3>文件内容已经被修改</h3>')
        mb.setInformativeText('是否直接关闭，不保存？')
        mb.setCheckBox(QCheckBox('下次不在提醒', mb))
        mb.setDetailedText('你修改的内容是给每一行代码加了一个分号')

        # mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # 添加自定义按钮， 两种构造方法演示
        btn1 = QPushButton('Apply123', mb)
        mb.addButton(btn1, QMessageBox.ApplyRole)
        # mb.addButton(QPushButton('sss', mb), QMessageBox.NoRole)
        btn2 = mb.addButton('xx2', QMessageBox.ApplyRole)
        # 绑定默认焦点按钮
        # mb.setDefaultButton(btn2)
        # 绑定ESCAPE健对应的按钮
        mb.setEscapeButton(btn2)

        def test(btn):
            print(btn)
            if btn == btn2:
                print('btn2 is clicked')
            if btn == btn1:
                print('btn1 is clicked')
        mb.buttonClicked.connect(test)



        mb.show()


        pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

