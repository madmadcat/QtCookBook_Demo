#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/3
@author: xdong
@site:
@email: 12919662@qq.com
@file:
@description: $描述$
"""
import sys


from login_pane import LoginPane
from register_pane import RegisterPane
from calculator_pane import CalculatorPane

from my_tool import *


if __name__ == '__main__':

    app = QApplication(sys.argv)
    login_pane = LoginPane()
    login_pane.show()

    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()

    calculator_pane = CalculatorPane()

    # slot functions
    def _slot_show_register_pan():
        in_anima = AnimationTool.animation_pos_generator(register_pane,
                                                         register_pane.pos(),
                                                         QPoint(0, 0),
                                                         register_pane)
        in_anima.start(QAbstractAnimation.DeleteWhenStopped)

    def _slot_hide_register_pan():
        out_anima = AnimationTool.animation_pos_generator(register_pane,
                                                          register_pane.pos(),
                                                          QPoint(login_pane.width(), 0),
                                                          register_pane)
        out_anima.start(QAbstractAnimation.DeleteWhenStopped)

        # register_pan.hide()

    def _slot_register_handler(account, pwd):
        print('*' * 10, '\n', account, pwd)

    def _slot_check_login(account, pwd):
        print(account, pwd)
        if account == '12345' and pwd == '66666':
            print('验证通过')
            calculator_pane.show()
            login_pane.hide()

            return True
        else:
            print('密码错误')
            login_pane.show_animation()
            return False

    # 连接信号
    login_pane.signal_show_register_pan.connect(_slot_show_register_pan)
    login_pane.signal_account_verify.connect(_slot_check_login)
    register_pane.signal_exit.connect(_slot_hide_register_pan)
    register_pane.signal_register.connect(_slot_register_handler)




    sys.exit(app.exec_())
