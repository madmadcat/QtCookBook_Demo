#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/28
   Change Activity:
                   2021/1/28
    win1
    通过强耦合的方式实现数据交互。不使用信号和槽
    win2
"""
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DateDialog(QDialog):

    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)

        self.setWindowTitle('DateDialog')

        layout = QVBoxLayout()
        self.datetime = QDateTimeEdit()
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        self.btnbox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        self.btnbox.accepted.connect(self.accept)
        self.btnbox.rejected.connect(self.reject)

        layout.addWidget(self.btnbox)
        self.setLayout(layout)

    def date_time(self):
        return self.datetime.dateTime()

    @staticmethod
    def get_date_time(parent=None):
        """
        父窗口可以直接调用
        :param parent:
        :return:
        """
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.date_time()
        # 返回日期，时间，result
        return (date.date(), date.time(), result == QDialog.Accepted)


class MultiWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('多窗口交互1：不使用信号与槽')

        self.lineedit = QLineEdit()
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        layout = QGridLayout()
        layout.addWidget(self.lineedit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        date = dialog.date_time()
        if result == dialog.Accepted:
            self.lineedit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Click(self):
        date, time, result = DateDialog.get_date_time(self)
        if result == QDialog.Accepted:
            self.lineedit.setText(date.toString())
            print('点击确定按钮')
        else:
            print('点击取消按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MultiWindow()
    w.show()
    sys.exit(app.exec_())
