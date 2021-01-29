import time
import sys

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QWidget, QLineEdit, QListWidget, QPushButton,\
    QVBoxLayout, QLabel

class addItemThread(QThread):

    add_item = pyqtSignal(str)
    show_time = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(addItemThread, self).__init__(*args, **kwargs)
        self.num = 0

    def run(self, *args, **kwargs):
        while True:
            file_str = 'File index{0}'.format(self.num, *args, **kwargs)
            self.num += 1

            self.add_item.emit(file_str)

            date = QDateTime.currentDateTime()
            currtime = date.toString('yyyy-MM-dd hh:mm:ss')
            print(currtime)
            self.show_time.emit(str(currtime))

            time.sleep(1)

class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)    
        self.setWindowTitle('多线程动态添加控件')
        self.setGeometry(800, 100, 500, 750)
        self.listWidget = QListWidget()
        self.btn = QPushButton('开始', self)
        self.btn_stop = QPushButton('终止', self)
        self.btn_stop.setEnabled(False)
        self.lb = QLabel('显示时间',self)
        self.vlayout = QVBoxLayout()
        
        self.vlayout.addWidget(self.btn)
        self.vlayout.addWidget(self.btn_stop)
        self.vlayout.addWidget(self.lb)
        self.vlayout.addWidget(self.listWidget)
        
        self.setLayout(self.vlayout)
        
        self.btn.clicked.connect(self.startThread)
        self.btn_stop.clicked.connect(self.terminate_thread)
        
        self.additemthread = addItemThread()
        
        self.additemthread.add_item.connect(self.addItem)
        self.additemthread.show_time.connect(self.showTime)

    def terminate_thread(self):

        self.btn_stop.setEnabled(False)
        self.btn.setEnabled(True)
        self.additemthread.quit()
        self.additemthread.wait()
        self.additemthread.deleteLater()

    def startThread(self):
        
        self.btn.setEnabled(False)
        self.btn_stop.setEnabled(True)
        self.additemthread.start()
        
    def addItem(self, file_str):
        self.listWidget.addItem(file_str)
        
    def showTime(self, time):
        self.lb.setText(time)
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())