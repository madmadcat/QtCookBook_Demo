#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5.QtWidgets import QApplication, QDialog
from demo_signal_01 import *


class MyForm(QDialog):
    """信号与槽的练习01"""

    def __init__(self):
        """构造函数"""

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
