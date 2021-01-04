import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoLineEdit import *

# 定义MyForm 继承类 QDialog
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        # 创建UI实例
        self.ui = Ui_Dialog()
        # 调用生成的setupUi方法
        self.ui.setupUi(self)
        # singal=clicked() ==> slot=dismessage()
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        self.ui.labelResponse.setText("Hello "
        +self.ui.lineEditName.text())

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())