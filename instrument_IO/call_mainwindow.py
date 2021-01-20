#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pyvisa as visa

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, qApp, QApplication

from GUI.mainwindow import *
from call_connect_dialog import *


class MyForm(QMainWindow):

    def __init__(self):

        super().__init__()
        self.session = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 拒绝菜单栏的 mac 风格
        self.ui.menubar.setNativeMenuBar(False)

        self.ui.actionClose.triggered.connect(qApp.quit)
        self.ui.actionConnect.triggered.connect(self.get_visa_addr)
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

    def get_visa_addr(self, visa_addr=''):
        """开启新的对话子窗口，通过文本输入框获得VIAS_ADDRESS,
        OK: 返回VIAS_ADDRESS，关闭对话框
        Cancel: 关闭对话框
        :return
        """

        dialog = ConnectDialog(self)

        # 调用自定义对话框，获取visa_addr
        if dialog.exec_():
            visa_addr = dialog.VISA_addr()
        dialog.destroy()

        if visa_addr.strip():
            self.session = self.create_session(visa_addr)

    def exception_handler(self, exception):
        """异常处理，格式化后输入到日志
        """
        # text = 'Error information:\n\tAbbreviation: ' \
        #        + str(exception.abbreviation) \
        #        + '\n\tError code: ' + str(exception.error_code) \
        #        + '\n\tDescription: ' + str(exception.description)
        self.update_logging(f'{exception}')

    def create_session(self, visa_addr):
        """建立和设备的通信
        :return 返回所连接设备的会话对象
        """
        res_manager = visa.ResourceManager()
        self.update_status_bar('Connecting to ' + visa_addr)
        session = None
        try:
            self.update_logging('Trying to connect to the instrument '
                                + visa_addr)
            session = res_manager.open_resource(visa_addr)

        except visa.VisaIOError as ex:
            self.exception_handler(ex)
        except ValueError as ex:
            self.exception_handler(ex)
        except OSError as ex:
            self.exception_handler(ex)
        return session

    def update_logging(self, info=None):
        """更新日志窗口"""
        self.ui.textBrowser.append(info)

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
