# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFormLayout, QWidget, QApplication, QTabWidget

class TabDemo(QTabWidget):


    def __init__(self, parent = None):

        # 超类的两种写法
        # TODO： 验证有效性
        super(TabDemo, self).__init__(parent)
        # super().__init__()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "标签1")
        self.addTab(self.tab2, "标签2")
        self.addTab(self.tab3, "标签3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("Tab 例子")

    def tab1UI(self):
        layout = QFormLayout()
        layout.addWidget(QLabel('Tab1 content'))
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        layout.addWidget(QLabel('Tab2 content'))
        self.setTabText(1, "seText to change name")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Tab3 content"))
        self.tab3.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = TabDemo()
    mw.show()
    sys.exit(app.exec_())