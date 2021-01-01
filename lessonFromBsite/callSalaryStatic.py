import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from demoSalaryStatic import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.disResult)
        self.show()

    def disResult(self):
        info = self.ui.textEdit.toPlainText()
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'
        QMessageBox.about(self,
                               '统计结果',
                               f'''薪资20000 以上的有：\n{salary_above_20k}
                               \n薪资20000 以下的有：\n{salary_below_20k}'''
                               )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())