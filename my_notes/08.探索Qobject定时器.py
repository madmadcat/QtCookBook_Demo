from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyLable(QLabel):
    """
    封装一个倒计时的QLabel类
    """

    def __init__(self, *args, **kwargs):
        super(MyLable, self).__init__(*args, **kwargs)
        self.move(100, 100)
        self.setStyleSheet("font-size:22px")

    def set_sec(self, sec):

        self.setText(str(sec))

    def start_my_timer(self, ms):

        self.timer_id = self.startTimer(1000)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        # 每次事件触发就改写QLable的Text
        curr_sec = int(self.text())
        curr_sec -= 1
        self.setText(str(curr_sec))
        if curr_sec == 0:
            # timer_id
            self.killTimer(self.timer_id)

        return super(MyLable, self).timerEvent(a0)



class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    label = MyLable(window)
    label.set_sec(8)
    label.start_my_timer(500)

    window.show()
    sys.exit(app.exec_())

