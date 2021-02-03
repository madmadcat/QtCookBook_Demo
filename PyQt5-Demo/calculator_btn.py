#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2021-02-2021/2/3
@author: xdong
@site:  
@email: 12919662@qq.com
@file:  calculator_btn
@description: $描述$
"""

from PyQt5.Qt import *

class CalculatorBtn(QPushButton):

    def __init__(self, parent=None, *args, **kwargs):
        super(CalculatorBtn, self).__init__(parent, *args, **kwargs)

        self.setStyleSheet("""
QPushButton[bg='gray'] {
    color: white;
    background-color: rgb(88, 88, 88);
    border: 1px solid;
}
QPushButton[bg='gray']:hover {
    background-color: rgb(150, 150, 150);
}    
QPushButton[bg='orange'] {
    color: white;
    background-color: rgb(207, 138, 0);
    border: 1px solid;
}    
QPushButton[bg='orange']:hover {
    background-color: rgb(238, 159, 0);
}        
QPushButton[bg='orange']:checked {
    background-color: rgb(207, 100, 0);
} 
QPushButton[bg='lightgray'] {
    color: black;
    background-color: rgb(200, 200, 200);
    border: 1px solid;
}   
QPushButton[bg='lightgray']:hover {
    background-color: rgb(230, 230, 230);
}
QPushButton[bg] {
    border-radius: %dpx;
}
        

        """ % (self.width() / 2))
        print(self.width() / 2)