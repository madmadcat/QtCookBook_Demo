#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/2
@author: xdong
@site:
@email: 12919662@qq.com
@file:  register_pane
@description: $描述$
"""
import sys

from PyQt5.Qt import *
from resource.register_ui import Ui_RegisterQWidget


class RegisterPane(QWidget, Ui_RegisterQWidget):

    signal_exit = pyqtSignal()
    signal_register = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.animation_targets = [
            self.about_menu_button,
            self.reset_menu_button,
            self.exit_menu_button]

        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

        # TODO：self.register_button跨越了两列,位置有点奇怪
        # print(self.formLayout.getWidgetPosition(self.register_button))

        # 控制register_button的显示逻辑
        self.account_le.textChanged.connect(self.slot_enable_reg_button)
        self.password_le.textChanged.connect(self.slot_enable_reg_button)
        self.confirm_password_le.textChanged.connect(self.slot_enable_reg_button)

    def slot_enable_reg_button(self):
        if len(self.account_le.text()) != 0 and len(self.password_le.text()) != 0 and self.password_le.text() == self.confirm_password_le.text():
            self.register_button.setEnabled(True)
        else:
            self.register_button.setEnabled(False)

    def slot_show_menu(self, checked):
        print('显示和隐藏', checked)
        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if not checked:
                animation.setStartValue(self.main_menu_button.pos())
                animation.setEndValue(self.animation_targets_pos[idx])
            else:
                animation.setEndValue(self.main_menu_button.pos())
                animation.setStartValue(self.animation_targets_pos[idx])
            animation.setDuration(300)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def slot_about(self):
        print('关于')
        QMessageBox.about(self, '关于', '这是一个PyQt5 GUI案例')

    def slot_reset(self):
        self.account_le.setText('')
        self.password_le.setText('')
        self.confirm_password_le.setText('')

    def slot_exit(self):
        print('exit')
        self.signal_exit.emit()

    def slot_register(self):
        print('register')
        self.signal_register.emit(self.account_le.text(), self.password_le.text())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = RegisterPane()
    # 定义好对外部的信号接口，其他界面参照这个部分去实现就可以了
    window.signal_exit.connect(lambda : print('触发了signal_exit'))
    window.signal_register.connect(lambda a, b: print('触发了signal_register',a ,b))
    window.show()
    sys.exit(app.exec_())
