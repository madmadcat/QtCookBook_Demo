#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/3
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  calculator_pane
@description: $描述$
"""

import sys

from PyQt5.Qt import *
from resource.calculator_ui import Ui_Form


class CalculatorPane(QWidget, Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = CalculatorPane()
    window.show()
    sys.exit(app.exec_())