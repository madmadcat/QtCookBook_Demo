#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from GUI.connect_dialog import *

class ConnectDialog(QDialog):

    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)
        self.ui = Ui_connect_Dialog()
        self.ui.setupUi(self)
        # 选中全部文本
        self.ui.lineEdit_VIAS_addr.selectAll()
        # 设置焦点在输入框内
        self.ui.lineEdit_VIAS_addr.setFocus()

    def VISA_addr(self):
        """返回文本框输入内容"""
        return self.ui.lineEdit_VIAS_addr.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ConnectDialog()
    w.show()
    sys.exit(app.exec_())