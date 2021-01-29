# -*- coding: utf-8 -*-

"""
Module implementing Gold.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QPixmap
from Ui_main import Ui_Form
from msgold import MsgGold
from digging import Ore

class Digging_Thread(QThread):
    gold_finish = pyqtSignal(int)

    def __init__(self, sec):
        super().__init__()
        self.sec = sec

    def run(self):
        ore = Ore(self.sec)
        goldcnt = ore.begin_dig()
        self.gold_finish.emit(goldcnt)

    def __del__(self):
        self.wait()

class Gold(QWidget, Ui_Form):
    """
    
    """
    def __init__(self, parent=None):
        """
        
        """
        super(Gold, self).__init__(parent)
        self.setupUi(self)
        self.value = 0
        self.second = 0
        self.movie = QMovie("res/farmer.gif")
        self.goldNum = 0


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        开始挖矿
        """
        self.goldNum = 0
        self.second = self.spinBox.value()
        self.pushButton.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.farm(1)
        self.progressBar.setMaximum(100)
        self.timer = QTimer()
        self.timer.start(self.second * 10)
        print(self.second)
        self.timer.timeout.connect(self.showProgress)
        self.dig = Digging_Thread(self.second)
        self.dig.gold_finish.connect(self.showResult)
        self.dig.start()

    def showProgress(self):
        self.value += 1
        self.progressBar.setValue(self.value)
        if self.value == 100:
            self.pushButton.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.value = 0
            self.timer.stop()
            del self.timer
            self.dig.quit()
            del self.dig
            self.farm(0)
            msgBox = MsgGold(self.goldNum)
            msgBox.exec()
            self.progressBar.setValue(0)
            self.label_farmer.setPixmap(QPixmap("res/ready.png"))

    def showResult(self, r):
        self.goldNum = r

    def farm(self, flag):
        if flag == 1:
            self.label_farmer.setMovie(self.movie)
            self.movie.start()
        if flag == 0:
            self.movie.stop()
            
