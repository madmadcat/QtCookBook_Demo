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


class Calculator(QObject):

    signal_calc_result = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        # 数字键位 num 运算符 operator
        self.key_models = []


    def calculate(self):

        expression = ''

        # if self.key_models[-1]['role'] == 'operator'
        if len(self.key_models) <= 2:
            return self.key_models[0]['title']
        elif self.key_models[-1]['role'] == 'number':
            for model in self.key_models:
                expression += model['title']
        else:
            for model in self.key_models[:-1]:
                expression += model['title']

        # self.key_models = []
        print(expression)
        result = eval(expression)
        return result

    def parse_key_model(self, key_model):
        """
        1. 每次点击的键位都存入列表
        2. 如果role是clear ，清空列表
        3. 如果role是操作符，且操作符是第一个item，清空列表，否则确定第一个number。存入结果列表。
            如果连续出现操作符，则替代上一个操作符
        4. 如果是num，且是数字1-9 ，构造一个number， 如果下一个还是num，则按照十进制构造number
        5. 如果是calculate。则遍历结果列表。进行计算

        :param key_model:
        :return:
        """
        # print(key_model)
        if key_model['role'] == 'clear':
            print('clear all data!')
            self.key_models = []
            self.signal_calc_result.emit('0.0')
            return None

        if key_model['role'] == 'calculate':
            self.signal_calc_result.emit(str(self.calculate()))
            return None

        if len(self.key_models) == 0:
            if key_model['role'] == 'number':
                if key_model['title'] == '.':
                    key_model['title'] = '0.'

                if key_model['title'] in ('%', "+/-"):
                    return None

                self.key_models.append(key_model)
                print(self.key_models)
                self.signal_calc_result.emit(self.key_models[-1]['title'])

            return None

        if key_model['title'] in ('%', "+/-"):
            if self.key_models[-1]['role'] != 'number':
                return None
            else:
                if key_model['title'] == '%':
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) / 100)
                    print(self.key_models)
                    self.signal_calc_result.emit(self.key_models[-1]['title'])

                    return None
                else:
                    self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) * -1)
                    print(self.key_models)
                    self.signal_calc_result.emit(self.key_models[-1]['title'])

                    return None

        if key_model['role'] == self.key_models[-1]['role']:
            if key_model['role'] == 'number':
                if key_model['title'] == '.' and self.key_models[-1]['title'].__contains__('.'):
                    return None

                if self.key_models[-1]['title'] != '0':
                    self.key_models[-1]['title'] += key_model['title']
                    print(self.key_models)
                else:
                    self.key_models[-1] = key_model
                    print(self.key_models)

                self.signal_calc_result.emit(self.key_models[-1]['title'])

            if key_model['role'] == 'operator':
                self.key_models.pop()
                self.key_models.append(key_model)
                print(self.key_models)
                #
                self.signal_calc_result.emit(str(self.calculate()))
        else:
            self.key_models.append(key_model)
            if key_model['role'] == 'operator':
                self.signal_calc_result.emit(str(self.calculate()))
            else:
                self.signal_calc_result.emit(key_model['title'])


class CalculatorPane(QWidget, Ui_Form):

    signal_calc_result = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        print(self.lineEdit.layoutDirection())
        # TODO: LE控件显示文本的方向问题没有解决
        # self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        print(self.lineEdit.layoutDirection())

        self.calculator = Calculator(self)

        self.calculator.signal_calc_result.connect(self.slot_calc_result_relay)

    def slot_calc_result_relay(self, result):
        # self.signal_calc_result.emit(result)
        self.lineEdit.setText(result)

    def get_key(self, title, role):
        self.calculator.parse_key_model({'title' : title, 'role' : role})


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = CalculatorPane()
    window.show()
    sys.exit(app.exec_())