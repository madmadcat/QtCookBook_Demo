#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/3
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  login_pane
@description: $描述$
"""

import sys

from PyQt5.Qt import *
from resource.login_ui import Ui_loginQWidget


class LoginPane(QWidget, Ui_loginQWidget):

    signal_show_register_pan = pyqtSignal()
    signal_account_verify = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        # QMovie().setScaledSize()
        # add a gif movie to the top label
        movie = QMovie(':/login/images/login_bg.gif')
        self.login_bg_label.setMovie(movie)
        movie.setScaledSize(QSize(478, 198))
        movie.start()

    def show_animation(self):
        anima = QPropertyAnimation(self)
        anima.setTargetObject(self.login_bottom)
        anima.setPropertyName(b"pos")
        anima.setKeyValueAt(0, self.login_bottom.pos())
        anima.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(15, 0))
        anima.setKeyValueAt(0.5, self.login_bottom.pos())
        anima.setKeyValueAt(0.7, self.login_bottom.pos() - QPoint(15, 0))
        anima.setKeyValueAt(1, self.login_bottom.pos())
        anima.setDuration(100)
        anima.setLoopCount(3)
        anima.start(QAbstractAnimation.DeleteWhenStopped)


        pass

    def slot_show_register_pan(self):
        # print('展示注册界面')
        self.signal_show_register_pan.emit()

    def slot_open_link(self):
        link = "https://qm.qq.com/cgi-bin/qm/qr?k=B7kVwdgZ2qvw_8j0KEOYQEPX7eikbjgx&jump_from=webapi"
        QDesktopServices.openUrl(QUrl(link))

    def slot_enable_login_btn(self):
        if len(self.account_cb.currentText()) > 0 and len(self.pwd_le.text()) > 0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def slot_check_login(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.signal_account_verify.emit(account, pwd)

    def slot_auto_login(self, checked):
        print('auto_login is checked', checked)
        if checked:
            self.remember_pwd_checkbox.setChecked(True)

    def slot_rem_pwd(self, checked):
        print('rem pwd is checked', checked)
        if not checked:
            self.auto_login_checkbox.setChecked(False)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()

    window.signal_account_verify.connect(lambda a, b: print(a, b))
    sys.exit(app.exec_())
