#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/30
   Change Activity:
                   2021/1/30:
"""

from PyQt5.QtWidgets import *


class PaintBlocks(QWidget):
    """给定一个窗口，和block个数和列数，将窗口填充满block"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('')

    def setup_ui(self):

        # self.btn = QPushButton(self)
        # self.btn.setText('让我看看效果')

        #self.show()
        pass

    def paint_block(self, count, cols):
        """
        绘制九宫格,注意学习这里的算法，行数/列数/当前行 当前列/
        :parameter count: block个数
        :parameter cols
        """
        counts, c = count, cols
        rows = (counts - 1) // cols + 1   # 计算总行数
        print('总行数', rows)
        width = self.width() / cols # block 宽度
        height =  self.height() / rows # block 高度


        print(rows, height)

        for i in range(counts):
            w = QWidget(self)
            w.resize(width, height)
            curr_row = i // cols # 当前元素位于第几行
            curr_col = i % cols # 当前元素位于第几列

            if i % 2 == 0:
                w.setStyleSheet("background-color: green; border: 1px solid")
            else:
                w.setStyleSheet("background-color: red; border: 2px solid")
            w.move(curr_col * width, curr_row * height)
            i += 1


        pass

    def load_qss(self):
        with open('qobject_explore.qss', 'r') as f:
            self.qss = f.read()
        return self.qss


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)

    window = PaintBlocks()
    window.resize(300, 300)
    window.setup_ui()

    window.paint_block(100, 7)

    # c = window.load_qss()
    # app.setStyleSheet(c)
    # show()方法要放在子控件创建之后
    window.show()

    sys.exit(app.exec_())
