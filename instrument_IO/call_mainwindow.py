#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from PyQt5.QtGui import QIcon
from GUI.mainwindow import *
from call_connect_dialog import *


class MyForm(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 拒绝菜单栏的 mac 风格
        self.ui.menubar.setNativeMenuBar(False)

        self.ui.actionClose.triggered.connect(qApp.quit)
        self.ui.actionConnect.triggered.connect(self.connect_dialog)
        self.update_status_bar()

    def connect_dialog(self):
        """开启新的对话子窗口，通过文本输入框获得VIAS_ADDRESS,
        OK: 返回VIAS_ADDRESS，关闭对话框
        Cancel: 关闭对话框
        :return string of VIAS_ADDRESS
        """
        dialog = ConnectDialog(self)
        dialog.exec_()
        visa_addr = dialog.VISA_addr()
        dialog.destroy()
        self.update_status_bar(visa_addr)
        self.vna_session(visa_addr)

    def vna_session(self, visa_addr):
        """建立和设备的通信"""
        pass

    def update_logging(self):
        """更新日志窗口"""
        pass

    def update_status_bar(self, info='waiting for connect'):

        self.ui.statusbar.showMessage(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = 'res/icon/toolbox-100.png'
    if sys.platform.startswith('dar', 0, 3) and os.path.isfile(path):
        app.setWindowIcon(QIcon(path))
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
