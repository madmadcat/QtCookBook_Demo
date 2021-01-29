# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03.多窗口对象传递实验
   Description :
   Author :       xdong
   date：          2021/1/28
-------------------------------------------------
   Change Activity:
                   2021/1/28:
-------------------------------------------------
"""
__author__ = 'xdong'


import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, \
    QVBoxLayout, QLabel, QPushButton, QLineEdit, QStatusBar, \
    QStyle, QDialog, QMessageBox

from PyQt5.QtCore import pyqtSignal, QMargins, Qt

from PyQt5 import QtGui

class SessionFactory(object):

    def create_session(self):
        obj = MySession('SessionInstance')
        return obj

class MySession(object):

    def __init__(self, name):
        self.name = name
        print('创建MySession对象',self.name)

    def show(self):
        print(self.name,'被创建了')


class MyMainWindow(QMainWindow):

    switch_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.__flag = True

        self.setWindowTitle('MainWindow')
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('')

        layout.addWidget(self.label)

        self.show_btn = QPushButton('Show Me')
        self.button = QPushButton('click me')
        self.button2 = QPushButton('show children')
        layout.addWidget(self.button)
        layout.addWidget(self.show_btn)
        layout.addWidget(self.button2)

        self.show_btn.clicked.connect(self.hide_info)
        self.button.clicked.connect(self.switch)
        self.button2.clicked.connect(self.slot_show_children)
        # QMainWindow自带centralWidget部件，无法直接在其中直接setLayout
        # 如果需要自定义小部件和layout，需要创建一个QWidget对象，添加你的小部件，setLayout
        # 然后setCentralWidget(你的QWidget对象)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)

    # 可以证明子对话框在返回后，对象已销毁，只存在与方法调用的时间
    def slot_show_children(self):
        print('Mainwindos child is:', self.children())

    def show_info(self):
        self.label.setText('I am Here')

    def hide_info(self):
        if self.__flag:
           self.label.setText('I am Here')
           self.__flag = False
        else:
            self.label.setText('')
            self.__flag = True

    def switch(self):
        #self.hide()
        w2 = MyQWidget('abc', parent=self)
        w2.exec_()
        self.obj = w2.obj
        print('主窗口 obj id is :', id(self.obj))
        print('主窗口获得子窗口的对象：',self.obj)
        print('obj is :', )
        print('Mainwindos child is:', self.children())


class MyQWidget(QDialog):

    sig = pyqtSignal()
    MARGIN = 1

    def __init__(self, some, parent=None):

        super(MyQWidget, self).__init__(parent)
        self.some = some
        self.obj = '我是一个对象'
        print('MyQWidget some is:', self.some)
        print('obj id is:', id(self.obj))
        self.setWindowTitle('MySubWindow')

        # TODO: QStyle.SP_ComputerIcon
        # TypeError: unable to convert a Python 'StandardPixmap' object to a C++ 'QIcon' instance
        # 需要对原生icon做一下处理
        # self.icon = QStyle.SP_ComputerIcon
        # self.icon = QStyle.standardIcon(QStyle.StandardPixmap)
        layout = QVBoxLayout()

        self.lineedit = QLineEdit('Input sth here...')
        layout.addWidget(self.lineedit,stretch=1)

        self.btn = QPushButton('确认')
        self.btn2 = QPushButton('返回')
        # TODO: alignment
        # alignment的用法
        # alignment = QtCore.Qt.AlignHCenter
        layout.addWidget((self.btn), 0, Qt.AlignHCenter)
        layout.addWidget((self.btn2), 0, Qt.AlignHCenter)

        self.statusbar = QStatusBar()
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.showMessage('Ready')
        layout.addStretch()
        layout.addWidget(self.statusbar, 0, Qt.AlignBottom)
        # 设置窗口边框的大小
        layout.setContentsMargins(QMargins(self.MARGIN, self.MARGIN, self.MARGIN, self.MARGIN))

        self.setLayout(layout)
        print('状态栏的父部件是',self.statusbar.parent())

        self.btn.clicked.connect(self.accept)
        self.btn2.clicked.connect(self.close)
        self.accepted.connect(self.slot_accept)
        # self.rejected.connect(self.slot_reject)

    # 重写closeEvent时要注意。
    # self.close 发射的closeEvent才是正确的类型
    # def closeEvent(self, event: QtGui.QCloseEvent) -> None:
    #     # 我们显示一个消息框,两个按钮:“是”和“不是”。第一个字符串出现在titlebar。
    #     # 第二个字符串消息对话框中显示的文本。第三个参数指定按钮的组合出现在对话框中。
    #     # 最后一个参数是默认按钮，这个是默认的按钮焦点。
    #     print('closeEvent is :')
    #     print(event)
    #     reply = QMessageBox.question(self, 'Message',
    #                                  "Are you sure to quit?", QMessageBox.Yes |
    #                                  QMessageBox.No, QMessageBox.No)
    #     # 处理返回值，如果单击Yes按钮,关闭小部件并终止应用程序。否则我们忽略关闭事件。
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()
    #     pass


    def slot_reject(self):
        pass

    def slot_accept(self):
        # self.hide()
        # self.parent.show()
        print('确认按钮被点击 ，close sub window ,show mainwindow')

    def get_session(self):
        sf = SessionFactory()
        s = sf.create_session()
        pass

def main1():
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    sys.exit(app.exec_())

def main2():
    app = QApplication(sys.argv)
    w = MyQWidget()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main1()

    # sf = SessionFactory()
    # s = sf.create_session()
    # s.show()
    # print(s)

