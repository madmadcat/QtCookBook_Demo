#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/30
   Change Activity:
                   2021/1/30:
"""

from PyQt5.QtWidgets import *


class PosionTool(QWidget):
    """
    实时更新坐标系，通过重写moveevent和resizeevent事件实现
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt位置提示工具')
        # self.setup_ui()

    def setup_ui(self):

        # layout
        top_layout = QVBoxLayout()
        left_layoht = QVBoxLayout()
        right_layout = QVBoxLayout()
        mid_layout = QHBoxLayout()
        gri_layout = QGridLayout()
        # x,y,pos
        self.lable_x = QLabel(self)
        self.lable_y = QLabel(self)
        self.lable_pos = QLabel(self)
        self.lable_geometry = QLabel(self)
        self.lable_frame_geo = QLabel(self)

        self.lable_x.setText('X: ' + str(self.x()))
        self.lable_y.setText('Y: ' + str(self.y()))
        self.lable_pos.setText('Pos: ' + str(self.pos())[19:])
        self.lable_geometry.setText('Geometry: ' + str(self.geometry())[18:])
        self.lable_frame_geo.setText('FrameGeometry: ' + str(self.frameGeometry())[18:])

        self.lable_width = QLabel(self)
        self.lable_height = QLabel(self)
        self.lable_size = QLabel(self)
        self.lable_fra_size = QLabel(self)

        self.lable_width.setText('Width: ' + str(self.width()))
        self.lable_height.setText('Height: ' + str(self.height()))
        self.lable_size.setText('Size: ' + str(self.size())[18:])
        self.lable_fra_size.setText('FrameSize: ' + str(self.frameSize())[18:])

        left_layoht.addWidget(self.lable_x)
        left_layoht.addWidget(self.lable_y)
        left_layoht.addWidget(self.lable_pos)
        left_layoht.addWidget(self.lable_geometry)
        left_layoht.addWidget(self.lable_frame_geo)

        right_layout.addWidget(self.lable_width)
        right_layout.addWidget(self.lable_height)
        right_layout.addWidget(self.lable_size)
        right_layout.addWidget(self.lable_fra_size)

        mid_layout.addLayout(left_layoht)
        mid_layout.addLayout(right_layout)

        self.btn1 = QPushButton('Move(0,0)', self)
        self.btn2 = QPushButton('Resize(450,350)', self)
        self.btn3 = QPushButton('setGeometry(0, 0, 400, 400)', self)
        self.btn4 = QPushButton('保留', self)
        self.btn4.setStyleSheet('background-color: red; border: 1px solid')

        self.btn1.clicked.connect(self.slot_move)
        self.btn2.clicked.connect(self.slot_resize)
        self.btn3.clicked.connect(self.slot_set_geometry)


        gri_layout.addWidget(self.btn1, 0, 0)
        gri_layout.addWidget(self.btn2, 0, 1)
        gri_layout.addWidget(self.btn3, 1, 0, 1, 2)
        gri_layout.addWidget(self.btn4, 2, 0, 1, 2)

        top_layout.addLayout(mid_layout, 3)
        top_layout.addLayout(gri_layout, 0)

        self.setLayout(top_layout)

    def slot_move(self):
        self.move(0, 0)

    def slot_resize(self):
        self.resize(450, 350)

    def slot_set_geometry(self):
        self.setGeometry(0, 0, 400, 400)

        
    def event(self, QEvent):
        #print(QEvent)
        return super(PosionTool, self).event(QEvent)

    def resizeEvent(self, QResizeEvent):
        self.lable_width.setText('Width: ' + str(self.width()))
        self.lable_height.setText('Height: ' + str(self.height()))
        self.lable_size.setText('Size: ' + str(self.size())[18:])
        self.lable_fra_size.setText('FrameSize: ' + str(self.frameSize())[18:])
        return super(PosionTool, self).resizeEvent(QResizeEvent)

    def moveEvent(self, QMoveEvent):
        self.lable_x.setText('X: ' + str(self.x()))
        self.lable_y.setText('Y: ' + str(self.y()))
        self.lable_pos.setText('Pos: ' + str(self.pos())[19:])
        self.lable_geometry.setText('Geometry: ' + str(self.geometry())[18:])
        self.lable_frame_geo.setText('FrameGeometry: ' + str(self.frameGeometry())[18:])
        return super(PosionTool, self).moveEvent(QMoveEvent)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = PosionTool()
    window.resize(450, 350)
    window.move(100, 100)
    window.setup_ui()
    window.show()
    sys.exit(app.exec_())
