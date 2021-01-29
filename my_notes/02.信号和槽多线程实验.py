import time
import sys

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QTimer
from PyQt5.QtWidgets import QWidget, QPushButton,\
    QVBoxLayout, QProgressBar
from PyQt5 import QtCore


class ReadThread(QThread):

    result_sig = pyqtSignal(str)

    def __init__(self, timeout, session):
        super(ReadThread, self).__init__()
        self.timeout = timeout
        self.session = session

    def run(self):
        for i in range(int(self.timeout / 1000)):
            print('第{}秒'.format(i+1))
            print(self.session.name)
            time.sleep(1)
        self.result_sig.emit('超时，timeout={}'.format(self.timeout))

    def __del__(self):
        self.wait()


class ClassA(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.timeout = 5000
        self.second = 0
        self.value = 0
        self.result = ''
        self.setWindowTitle('Qtimer and QThread')
        self.setGeometry(800, 100, 500, 750)
        self.btn = QPushButton('开始', self)
        self.btn.setObjectName('PushButton')
        self.progress = QProgressBar()
        # TODO: orientation??
        # self.progress.setOrientation(Horizontal)
        self.vlayout = QVBoxLayout()
        
        self.vlayout.addWidget(self.btn)
        self.vlayout.addWidget(self.progress)
        self.setLayout(self.vlayout)

        QtCore.QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_PushButton_clicked(self):
        """启动子线程任务
        """
        self.btn.setEnabled(False)
        self.progress.setMaximum(100)
        self.timer = QTimer()
        self.timer.start(self.timeout / 1000 * 11)
        self.timer.timeout.connect(self.showProgress)
        self.session = ClassA('Molly', 9)
        self.read_operation = ReadThread(self.timeout, self.session)
        self.read_operation.result_sig.connect(self.show_result)
        self.read_operation.start()

    def showProgress(self):
        self.value += 1
        self.progress.setValue(self.value)
        if self.value == 100:
            self.btn.setEnabled(True)
            self.value = 0
            self.timer.stop()
            del self.timer
            self.read_operation.quit()
            del self.read_operation
            self.progress.setValue(0)
            print('线程超时为：' + self.result)
    def show_result(self, r):

        self.result = r


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())