#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pyvisa as visa

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, qApp, QApplication
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer
from PyQt5 import QtCore
from GUI.mainwindow import *
from call_dialogs import *


class VisaReadThread(QThread):
    """
    handle vias read IO operation in QThread
    """
    result_sig = pyqtSignal(str)

    def __init__(self, timeout, session):
        """
        Start a thread to perform vias read IO operation

        :param timeout: a int vaule to present read timeout in millisecond
        :param session: a visa resource session object.
        :return str: response message of read IO operation, sended by
        customsize signal
        """
        super(VisaReadThread, self).__init__()
        self.timeout = timeout
        self.session = session

    def run(self):
        try:
            response = self.session.read()
            self.result_sig.emit(response)
        except (visa.VisaIOError, AttributeError) as ex:
            self.exception_handler(ex)

    def __del__(self):
        self.wait()


class MyWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyWindow, self).__init__(parent)

        # 定义visa 设备的 session属性，保证在窗口应用下持续性
        self.session = None
        self.timeout = 2000
        self.termination = '\n'
        self.value = 0
        self.curr_msg = '*IDN?'

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 拒绝菜单栏的 mac 风格
        self.ui.menubar.setNativeMenuBar(False)
        self.ui.lable_status = QtWidgets.QLabel('连接状态: 未连接')
        self.ui.lable_status.setStyleSheet('color: red')
        self.ui.statusbar.addPermanentWidget(self.ui.lable_status, stretch=0)
        self.ui.actionClose.triggered.connect(qApp.quit)
        self.ui.actionConnect.triggered.connect(self.connect_dialog_handler)
        self.ui.actionClear.triggered.connect(self.clear_logging)
        self.ui.actionDisconnect.triggered.connect(self.close_session)
        self.ui.actionConfig.triggered.connect(self.config_dialog_handler)
        self.ui.actionDevice_Clear.triggered.connect(self.device_clear)
        self.ui.actionSYST_ERR_Query.triggered.connect(self.query_syserr)
        # signal and slot ,transfer parameters by lambda
        # self.ui.btn_write.clicked.connect(lambda: self.write_cmd(self.cmd))
        self.ui.btn_write.clicked.connect(self.btn_handler)
        self.ui.btn_read.clicked.connect(self.btn_handler)
        self.ui.btn_query.clicked.connect(self.btn_handler)
        self.update_status_bar()

    def act_stat_toggler(self, stat=1):
        """
        stat = 1 means session 实例已存在
        stat = 0 means seesion 实例为None
        """
        print(stat)
        self.ui.actionConnect.setEnabled(bool(stat - 1))
        self.ui.actionDisconnect.setEnabled(bool(stat))
        self.ui.actionDevice_Clear.setEnabled(bool(stat))
        self.ui.actionSYST_ERR_Query.setEnabled(bool(stat))
        self.ui.actionSYST_ERR_Query.setEnabled(bool(stat))



    def query_syserr(self):
        pass

    def device_clear(self):
        pass

    def config_dialog_handler(self):
        """
        开启对话框，通过自定义信号传递timeout和termination两个参数
        """
        dialog = MyConfigDialog(self)
        dialog.signal_para.connect(self.conf_diag_sign_handler)
        if dialog.exec_():
            dialog.destroy()

    def conf_diag_sign_handler(self, timeout_int, term_str):
        self.timeout = timeout_int
        self.termination = term_str

    def clear_logging(self):
        self.ui.textBrowser.clear()

    def btn_handler(self):

        sender = self.sender()
        self.curr_msg = self.ui.comboBox_cmd_history.currentText()
        if sender.text() == 'Read':
            self.update_logging('<--' + self.curr_msg)
            # 启动子线程任务
            self.ui.btn_read.setEnabled(False)
            self.ui.actionStop_IO_Opertion.setEnabled(True)
            self.ui.progressBar.setMaximum(100)
            self.timer = QTimer()
            self.timer.start(self.session.timeout / 1000 * 11)
            self.timer.timeout.connect(self.show_progress)
            self.read_operation = VisaReadThread(self.session)
            self.read_operation.result_sig.connect(self.resoponse_handler)
            self.read_operation.start()
        elif sender.text() == 'Write':
            self.update_logging('-->' + self.curr_msg)
            try:
                self.session.write(self.curr_msg)
            except (visa.VisaIOError, AttributeError) as ex:
                self.exception_handler(ex)
        elif sender.text() == 'Query':
            self.update_logging('<-->' + self.curr_msg)
            try:
                self.session.query(self.curr_msg)
            except (visa.VisaIOError, AttributeError) as ex:
                self.exception_handler(ex)

    def show_progress(self):
        """
        funtion to handler progressbar which represting Read IO operation
        """
        self.value += 1
        self.ui.progressBar.setValue(self.value)
        if self.value == 100:
            self.abort_read()

    def abort_read(self):

        self.ui.btn_read.setEnabled(True)
        self.ui.actionStop_IO_Opertion.setEnabled(False)
        self.value = 0
        self.timer.stop()
        del self.timer
        self.read_operation.quit()
        del self.read_operation
        self.ui.progressBar.setValue(0)

    def response_handler(self, response):
        """function to handler visa resource response
        """
        self.update_logging(response)

    def connect_dialog_handler(self, visa_addr):
        """开启新的对话子窗口，通过文本输入框获得VIAS_ADDRESS,
        OK: 返回VIAS_ADDRESS，关闭对话框
        Cancel: 关闭对话框
        :return  None
        """
        visa_addr = 'TCPIP0::192.168.1.3::inst0::INSTR'
        dialog = MyConnectDialog(self, address=visa_addr)

        # 调用自定义对话框，获取visa_addr
        if dialog.exec_():
            visa_addr = dialog.VISA_addr()
        dialog.destroy()

        # 创建主窗口visa session对象
        try:
            self.create_session(visa_addr)
        except AttributeError as ex:
            self.exception_handler(ex)
            
    def exception_handler(self, exception):
        """异常处理，格式化后输入到日志
        """
        self.update_logging(f'{exception}')

    def create_session(self, visa_addr):
        """建立和设备的通信
        :return
        """
        res_manager = visa.ResourceManager()
        self.update_status_bar('Connecting to ' + visa_addr)
        try:
            self.update_logging('Trying to connect to the instrument '
                                + visa_addr)
            # self.session = res_manager.open_resource(visa_addr)
            # TODO: debug
            self.session = 'aaa'
            self.update_logging('Connecting is successed...')
            self.update_status_bar('Resource is ready.')
            self.ui.lable_status.setText('连接状态: 已连接')
            self.ui.lable_status.setStyleSheet('color: green')
            self.act_stat_toggler(1)
            print('status toggle done')

        except (visa.VisaIOError, ValueError, OSError) as ex:
            self.exception_handler(ex)
        return

    def close_session(self):
        try:
            self.session.close
            self.act_stat_toggler(0)
        except visa.VisaIOError as ex:
            self.exception_handler(ex)

    def update_logging(self, info=''):
        """更新日志窗口"""
        self.ui.textBrowser.append(info)

    def update_status_bar(self, info='waiting for connect'):

        self.ui.statusbar.showMessage(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = 'res/icon/toolbox-100.png'
    if sys.platform.startswith('dar', 0, 3) and os.path.isfile(path):
        app.setWindowIcon(QIcon(path))
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
