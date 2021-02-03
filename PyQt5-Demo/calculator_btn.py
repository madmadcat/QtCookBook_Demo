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

    key_pressed = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super(CalculatorBtn, self).__init__(parent, *args, **kwargs)

    def resizeEvent(self, *args, **kwargs) -> None:
        super().resizeEvent(*args, **kwargs)
        self.setStyleSheet("""
        QPushButton[bg='gray'] {
            color: white;
            background-color: rgb(88, 88, 88);
            border: 1px solid;
        }
        QPushButton[bg='gray']:hover {
            background-color: rgb(150, 150, 150);
        }    
        QPushButton[bg='orange'], QPushButton[bg='equal'] {
            color: white;
            background-color: rgb(207, 138, 0);
            border: 1px solid;
        }    
        QPushButton[bg='orange']:hover, QPushButton[bg='equal']:hover {
            background-color: rgb(238, 159, 0);
        }        
        QPushButton[bg='orange']:checked {
            color: white;
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
            font-size: 20dpx
        }


        """ % (min(self.width(), self.height()) / 2))
        # 圆角半径为控件宽或者高其中最小的那个值的一半

    def mousePressEvent(self, *args, **kwargs):
        # 重写mouse事件，发射自定义信号
        super(CalculatorBtn, self).mousePressEvent(*args, **kwargs)
        self.key_pressed.emit(self.text(), self.property('role'))