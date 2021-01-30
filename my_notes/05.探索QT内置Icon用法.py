# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05.探索QT内置Icon用法
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

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QStyle, QGridLayout

from PyQt5.QtGui import QIcon

import my_enum

class Mydialog(QWidget):
    """
    利用QGridLayout,遍历Qt内置Icon，创建按钮对象，绑定图标，共71个Icon
    """
    def __init__(self, parent=None):
        super(Mydialog, self).__init__(parent)

        self.setWindowTitle('PyQt5 BuiltIn Icon')
        self.resize(800, 600)

        layout = QGridLayout()
        self._icon_index = 0
        for row in range(18):
            for col in range(4):
                _qicon = QApplication.style().standardIcon(self._icon_index)
                _name = my_enum.SPIcon(self._icon_index).name
                layout.addWidget(QPushButton(QIcon(_qicon), str(self._icon_index) + ' ' + _name), row, col)
                #print(my_enum.SPIcon(self._icon_index).name)
                self._icon_index += 1
                col += 1
            row += 1

        layout.addWidget(QPushButton(QIcon(QApplication.style().standardIcon(QStyle.SP_LineEditClearButton)), '71'), 7, 0)

        # TODO: 注意addWidget()方法的参数，不同的重载，参数不同。
        # self.desktop_icon = QApplication.style().standardIcon(QStyle.SP_DesktopIcon)
        # self.btn = QPushButton(QIcon(self.desktop_icon), 'TEST')
        # layout.addWidget(QPushButton(QIcon(self.desktop_icon), 'TEST'), 1,1)
        # self.play_button = QPushButton('Play video')
        #
        # # 调用内置QIcon的两种方法
        # # self.play_button.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
        # self.play_button.setIcon(QApplication.style().standardIcon(20))
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.btn)
        # layout.addWidget(self.play_button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mydialog()
    w.show()
    sys.exit(app.exec_())