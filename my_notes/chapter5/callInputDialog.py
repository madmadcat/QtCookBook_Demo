import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
from demoInputDialog import *

class MyForm(QDialog):


    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCountry.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):

        countries = ("Albania", "Algeria", "Andorra", "Angola",
        "Antigua and Barbuda", "Argentina", "Armenia", "Aruba",
        "Australia", "Austria", "Azerbaijan")

        # getItem: 传入列表，自动生成combo box
        # countryName, ok = QInputDialog.getItem(self, "InputDialog", "List of countries", countries, 0, False)
        # getText: 简单的文本输入对话框
        countryName, ok = QInputDialog.getText(self, "Text Input", "VISA ADDR")

        if ok and countryName:
            self.ui.lineEditCountry.setText(countryName)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())