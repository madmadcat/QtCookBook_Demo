#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal
from GUI.config_dialog import *
from GUI.connect_dialog import *

class MyConfigDialog(QDialog):

    signal_para = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(MyConfigDialog, self).__init__(parent)
        self.ui = Ui_ConfigDialog()
        self.ui.setupUi(self)
        self.ui.lineEditTimeout.setText(str(2000))
        self.ui.lineEditTimeout.selectAll()
        self.ui.lineEditTimeout.setFocus()

        # TODO: 按钮组的accept和reject状态
        # self.ui.buttonBox.clicked.connect(self.btn_clicked)
        # dialog对象的accepted信号连接到自定义信号发射器
        self.accepted.connect(self.btn_clicked)

    def btn_clicked(self):
        timeout_value = int(self.ui.lineEditTimeout.text())
        termination = self.ui.comboBoxTerm.currentText()
        self.signal_para.emit(timeout_value, termination)
        # print('signal emited')


class MyConnectDialog(QDialog):

    def __init__(self, parent=None, address=''):
        super(MyConnectDialog, self).__init__(parent)
        self.ui = Ui_connect_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit_VIAS_addr.setText(address)
        # 选中全部文本
        self.ui.lineEdit_VIAS_addr.selectAll()
        # 设置焦点在输入框内
        self.ui.lineEdit_VIAS_addr.setFocus()

    def VISA_addr(self):
        """返回文本框输入内容"""
        return self.ui.lineEdit_VIAS_addr.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyConfigDialog()
    w.show()
    sys.exit(app.exec_())