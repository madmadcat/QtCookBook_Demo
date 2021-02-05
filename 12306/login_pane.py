#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/4
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  login_pane
@description: $描述$
"""
import sys

from PyQt5.Qt import *
from resource.login_pane_ui import Ui_Form

from api.api_tool import ApiTool


class LoginPane(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self._slot_refresh_captcha()

    def _slot_refresh_captcha(self):
        # print('刷新验证码')
        url = ApiTool.download_captcha()
        pixmap = QPixmap(url)
        self.captcha_label.setPixmap(pixmap)
        self.captcha_label.clear_all_points()


    def _slot_auto_captcha(self):
        print('自动打码')
        QMessageBox.warning(self, '自动打码暂不支持', '自动打码暂不支持\n>....<')

    def _slot_login_check(self):
        # print('登录验证')
        r = self.captcha_label.get_points()
        if ApiTool.check_captcha(r):
            print('验证码校验成功')
        else:
            print('验证码校验失败')
            self._slot_refresh_captcha()
        # ApiTool 这个类的类属性
        print(ApiTool.session)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()

    sys.exit(app.exec_())
