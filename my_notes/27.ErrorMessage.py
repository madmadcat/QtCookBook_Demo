#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  27.ErrorMessage
@description: $描述$
"""
import sys

from PyQt5.Qt import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('${NAME}')
        self.resize(500, 500)
        self.setup_ui()
        pass

    def setup_ui(self):

        # QErrorMessage 是非模太对话框
        em = QErrorMessage(self)
        em.setWindowTitle('错误提示')
        em.showMessage('猫哥')
        # em.exec()

        # 可以利用errormessage 输出异常
        QErrorMessage.qtHandler()
        qDebug('xxx')
        qWarning('123445')
        pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
