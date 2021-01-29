# -*- coding: utf-8 -*-

"""
Module implementing MsgGold.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_digdone import Ui_Dialog


class MsgGold(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, cc, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MsgGold, self).__init__(parent)
        self.setupUi(self)
        if cc < 10:
            self.label_gold.setText("你挖到了" + str(cc) + "块金矿！\n试试挖的时间长点吧！")
        elif cc < 100:
            self.label_gold.setText("恭喜你挖到了" + str(cc) + "块金矿！")
        else:
            self.label_gold.setText("真棒！你挖到了" + str(cc) + "块金矿！")


