#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/1
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  22.LineEdit控件案例_剥离登录验证的方法
@description: 案例描述
创建一个窗口，两个LineEdit，一个按钮，两行都有内容时，按钮可用，密码输入框后有小图标可以控制显示密码
然后将账号验证操作独立出来。界面与逻辑分离
"""
from PyQt5.Qt import *
import sys


class AccountTool:
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    SUCCESS = 3

    @staticmethod
    def check_login(account, pwd):
        if account != 'dx':
            return AccountTool.ACCOUNT_ERROR
        if pwd != '123':
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS


class MyForm(QWidget):

    def __init__(self):
        super(MyForm, self).__init__()
        self.setWindowTitle('登录')
        # self.resize(500, 500)
        self.setFixedSize(600, 350)
        self.init_ui()

    def init_ui(self):

        self.le1 = QLineEdit(self)
        self.le2 = QLineEdit(self)
        self.le1.move(300,100)
        self.le2.move(300,150)
        self.le2.setEchoMode(QLineEdit.Password)

        self.label1 = QLabel('用户名', self)
        self.label2 = QLabel('密码', self)
        self.label1.move(200, 100)
        self.label2.move(200, 150)

        # self.show_pwd_btn = QToolButton(self)
        # self.show_pwd_btn.setIcon(QIcon('close.png'))
        # self.show_pwd_btn.move(450, self.le2.pos().y())

        self.login_btn = QPushButton('Login', self)
        self.login_btn.move(250, 300)
        self.login_btn.setEnabled(False)

        self.le1.setPlaceholderText('请输入账号')
        self.le2.setPlaceholderText('请输入密码')

        self.login_btn.clicked.connect(self._slot_login_btn_on_click)
        self.le2.textChanged.connect(self._slot_enable_login_btn)
        self.le1.textChanged.connect(self._slot_enable_login_btn)
        # self.show_pwd_btn.pressed.connect(self._slot_showpwd)
        # self.show_pwd_btn.released.connect(self._slot_hidepwd)

        # 给QLineEdit 添加自定义行为


        self.action = QAction(self.le2)
        self.action.setIcon(QIcon('close.png'))
        self.le2.addAction(self.action, QLineEdit.TrailingPosition)
        self.action.triggered.connect(self.change)

        # 自动补全
        completer = QCompleter(['dx', 'wangzha', 'ghost'], self)
        self.le1.setCompleter(completer)

    def change(self):
        print('Toggle 秘文')
        if self.le2.echoMode() == QLineEdit.Normal:
            self.le2.setEchoMode(QLineEdit.Password)
            self.action.setIcon(QIcon('close.png'))
        else:
            self.le2.setEchoMode(QLineEdit.Normal)
            self.action.setIcon(QIcon('open.png'))



    def _slot_login_btn_on_click(self):

        account = self.le1.text()
        pwd = self.le2.text()

        state = AccountTool.check_login(account, pwd)
        print(state)

        if state == AccountTool.ACCOUNT_ERROR:
            QMessageBox.warning(self, '提醒', '用户名错误')
            self.le1.setText('')
            self.le1.setFocus()
            return None

        if state == AccountTool.PWD_ERROR:
            QMessageBox.warning(self, '提醒', '用户密码错误')
            self.le2.setText('')
            self.le2.setFocus()
            return None

        if state == AccountTool.SUCCESS:
            QMessageBox.information(self, '登录成功', '登录成功')

        # if self.le1.text() != 'dx':
        #     print('username fail')
        #     self.le1.setText('')
        #     self.le1.setFocus()
        #     QMessageBox.warning(self, '提醒', '用户名错误')
        #     return None
        #
        # if self.le2.text() != '123':
        #     print('pwd fail')
        #     self.le2.setText('')
        #     self.le2.setFocus()
        #     QMessageBox.warning(self, '提醒', '用户密码错误')
        #     return None
        #
        # msg = QMessageBox(self)
        # msg.setText('成功')
        # msg.show()

    def _slot_enable_login_btn(self):
        if self.le1.text() and self.le2.text():
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)



    def _slot_showpwd(self):
        # curr_text = self.le2.text()
        # self.le2.displayText(curr_text)
        self.le2.setEchoMode(QLineEdit.Normal)

    def _slot_hidepwd(self):
        self.le2.setEchoMode(QLineEdit.Password)

app = QApplication(sys.argv)

# 控件操作
# 创建控件
window = MyForm()
# 设置控件


# 展示控件
window.show()
# 执行应用程序，进入消息循环
sys.exit(app.exec())