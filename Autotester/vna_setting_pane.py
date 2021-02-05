#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/5
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  vna_setting_pane
@description: $描述$
"""

import sys

from PyQt5.Qt import *
from resource.vna_setting_ui import Ui_MainWindow


class VNASettingPane(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = VNASettingPane()
    window.show()

    # window.signal_account_verify.connect(lambda a, b: print(a, b))
    sys.exit(app.exec_())