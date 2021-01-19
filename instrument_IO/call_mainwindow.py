#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pyvisa as visa

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, qApp

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
        self.ui.actionClear.triggered.connect(self.clear_logging)
        self.ui.btn_send_command.clicked.connect(self.write_cmd)
        self.ui.btn_read_response.clicked.connect(self.read_response)
        self.ui.btn_send_then_read.clicked.connect(self.query_cmd)

        self.update_status_bar()

    def clear_logging(self):
        self.ui.textBrowser.clear()

    def write_cmd(self):
        pass

    def read_response(self):
        pass

    def query_cmd(self):
        pass

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
        self.update_status_bar('Connecting to ' + visa_addr)
        self.instr_session(visa_addr)

    def exception_handler(self, exception):
        """异常处理，格式化后输入到日志
        """
        text = 'Error information:\n\tAbbreviation: ' + str(exception.abbreviation) + '\n\tError code: ' + str(exception.error_code) + '\n\tDescription: ' + str(exception.description)
        self.update_logging(text)

    def instr_session(self, visa_addr):
        """建立和设备的通信"""
        text = 'Bad address'
        res_manager = visa.ResourceManager()
        try:
            self.update_logging('Trying to connect to the instrument ' + text)
            session = res_manager.open_resource("BAD ADDRESS")
        except visa.VisaIOError as ex:
            self.update_logging('VISA ERROR - An error has occurred!')
            self.exception_handler(ex)

    def update_logging(self, info=None):
        """更新日志窗口"""
        text = info
        self.ui.textBrowser.append(text)

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
