#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/4
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  31.mainwindow 和 dialog 和 widget
@description: 验证QMianWindow和QDialog的模态，以及类属性的生命周期
应用程序存在期间，Api的类属性都存在，不会被回收
"""
import sys

from PyQt5.Qt import *


class DialogWindow(QWidget):
    pass

class Dog(object):

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

class Api(QObject):

    session = None

    def __init__(self, parent=None, *args, **kwargs):
        super(Api, self).__init__(parent, *args, **kwargs)

    @classmethod
    def set_session(cls, name):
        cls.session = Dog(name)
        print(cls.session)

    @classmethod
    def get_dog_age(cls, name):
        print ('{} 的年龄是{}'.format(cls.session.name, cls.session.age))
        return cls.session.age

    @classmethod
    def get_session(cls):
        return cls.session

class MyDialog(QDialog):
    """
    自定义dialog类，实现状态栏和statustip，重写event,绘制状态栏
    """
    def __init__(self, parent=None, *args, **kwargs):
        super(MyDialog, self).__init__(parent, *args, **kwargs)

        self.setWindowTitle('Dialog')
        self.resize(300, 400)
        self.move(400, 400)

        l = QVBoxLayout(self)
        bb = QPushButton('set molly name')
        bb2 = QPushButton('get molly age')
        bb3 = QPushButton('get session')
        bb.setStatusTip('This is a button')
        lbl = QLabel('text')
        self.lbl = lbl
        l.addWidget(bb)
        l.addWidget(bb2)
        l.addWidget(bb3)
        l.addWidget(lbl)
        b = QStatusBar()
        l.addStretch(1)
        l.addWidget(b)
        b.showMessage('text')
        l.setContentsMargins( 10, 10 , 0, 0)
        l.setSpacing(0)
        print(l.getContentsMargins(),'get content margin')

        self.bar = b

        bb.clicked.connect(self.set_name)
        bb2.clicked.connect(self.get_age)
        bb3.clicked.connect(self.get_session)

        self.add_menubar()

    def add_menubar(self):
        layout = QVBoxLayout(self)
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 400, 24))
        menu = menubar.addMenu('File')
        actionNew = menu.addAction('New')
        layout.setMenuBar((menubar))
        self.setLayout(layout)

    def slot_show_text(self, text):
        self.lbl.setText(text)
        print('刷新标签内容')

    def set_name(self):
        Api.set_session('Molly')
        print('创建session')


    def get_age(self):
        r = Api.get_dog_age('Molly')
        print(r)

    def get_session(self):
        r = Api.get_session()
        print('session is ', str(r))

    def event(self, evt) -> bool:
        if evt.type() == QEvent.StatusTip:
            self.bar.showMessage(evt.tip())
            return True

        return super(MyDialog, self).event(evt)





class MyWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(MyWidget, self).__init__(parent, *args, **kwargs)

        self.setWindowTitle('Widget')
        self.resize(400,200)
        self.move(200, 200)

class MainWindow2(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow2, self).__init__(parent, *args, **kwargs)

        self.setWindowTitle('Widget')
        self.resize(400,200)
        self.move(500, 500)

        btn = QPushButton('close', self)
        btn.clicked.connect(lambda : self.close())
        # btn.clicked.connect(lambda : self.hide())

        le = QLineEdit(self)
        le.move(50, 50)
        self.le = le
        label = QLabel(self)
        text = '没有父亲' if self.parent() is None else str(self.parent())
        print(str(self.parent()))
        label.setText(text)
        label.adjustSize()
        label.move(100, 100)

    def slot_show_text(self, text):
        self.le.setText(text)



class MainWindow(QMainWindow):

    signal_label_text = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('main window')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        btn1 = QPushButton('open dialog')
        btn2 = QPushButton('hide dialog')

        btn3 = QPushButton('open widget')
        btn4 = QPushButton('hide widget')

        btn5 = QPushButton('打印对话框内容')
        btn6 = QPushButton('打印控件内容')

        btn7 = QPushButton('open mainwindow2')
        btn8 = QPushButton('hide mainwindow2')

        lb1 = QLabel()
        lb1.adjustSize()
        self.lb1 = lb1

        timer = QTimer(self)
        timer.timeout.connect(self.refresh_label_content)
        timer.start(3000)

        layout = QGridLayout()

        layout.addWidget(btn1, 0, 0)
        layout.addWidget(btn2, 0, 1)
        layout.addWidget(btn3, 1, 0)
        layout.addWidget(btn4, 1, 1)
        layout.addWidget(btn5, 2, 0)
        layout.addWidget(btn6, 2, 1)
        layout.addWidget(btn7, 3, 0)
        layout.addWidget(btn8, 3, 1)
        layout.addWidget(lb1, 4, 0, 1, 1)


        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.w_dialog = MyDialog(self)
        # self.w_dialog.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.w_widget = MyWidget()

        self.w_mainwindow2 = MainWindow2(self)

        btn1.clicked.connect(self.open_dialog)
        btn2.clicked.connect(self.close_dialog)

        btn3.clicked.connect(self.open_widget)
        btn4.clicked.connect(self.close_widget)

        btn7.clicked.connect(self.open_mainwindow2)
        btn8.clicked.connect(self.close_mainwindow2)
        self.signal_label_text.connect(self.w_dialog.slot_show_text)
        self.signal_label_text.connect(self.w_mainwindow2.slot_show_text)

    def refresh_label_content(self):
        import random
        r = random.random()
        self.lb1.setText(str(r))
        self.signal_label_text.emit(str(r))


    def open_dialog(self):

        # 结合show()方法，可以定义dialog是一个模态对话框
        # self.w_dialog.setModal(True)
        # self.w_dialog.show()

        # 对话框的open()方法将打开一个半模态对话框，即只会阻塞父窗口、父窗口的父窗口及兄弟窗口
        # ---------------------------------------------------------------------------
        # 相当于一个QWidget窗口的这样操作
        # ---------------------------------------------------------------------------
        # w = QWidget(parent_window)
        # w.setWindowModality(Qt.WindowModal)
        # w.show()
        # self.w_dialog.setModal(True)
        # self.w_dialog.open()
        print(self.w_dialog.isModal())



        self.w_dialog.exec()

    def close_dialog(self):
        self.w_dialog.hide()

    def open_widget(self):
        # widget没有open方法去创建模态窗口 和 setModal方法
        print(self.w_widget.isModal())
        self.w_widget.setWindowModality(Qt.WindowModal)
        self.w_widget.show()
        print(self.w_widget.isModal())

    def close_widget(self):
        self.w_widget.hide()

    def open_mainwindow2(self):

        # self.w_mainwindow2.setWindowModality(Qt.ApplicationModal)
        # ---------------------------------------------------------------------------
        # mainwindow控件，设置ApplicationModal 后用show方法可以实现带标题栏的模态窗口
        # 也可以设置父控件
        # ---------------------------------------------------------------------------
        self.w_mainwindow2.setWindowModality(Qt.ApplicationModal)
        self.w_mainwindow2.show()
        print(self.w_mainwindow2.isModal())

    def close_mainwindow2(self):
        self.w_mainwindow2.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
