import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
from myPostman import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 调试默认url
        self.ui.lineEditURL.setPlaceholderText('https://api.github.com/events')
        self.ui.lineEditURL.setText('https://api.github.com/events')

        #combobox select
        self.ui.comboBoxRequestType.currentIndexChanged.connect(self.
                                                                getRequestType)
        self.ui.pushButtonSendURL.clicked.connect(self.
                                                   sendRequest)
        self.ui.pushButtonClear.clicked.connect(self.clearTextBrowser)
        self.ui.pushButtonAddrow.clicked.connect(self.addRow)
        self.ui.pushButtonDelrow.clicked.connect(self.delRow)

    def getRequestType(self):
        #获得下拉菜单所选中的文本
        print(self.ui.comboBoxRequestType.currentText())

    def sendRequest(self):
        # request = requests.get(url,headers={dict})
        # 发送request请求，在text浏览框中显示log

        type = self.ui.comboBoxRequestType.currentText()
        url = self.ui.lineEditURL.text()
        params = self.ui.textEditContents.toPlainText()
        headers = {}

        for i in range(self.ui.tableWidgetHeader.rowCount()):
            if self.ui.tableWidgetHeader.item(i,0):
                k = self.ui.tableWidgetHeader.item(i,0).text()
                v = self.ui.tableWidgetHeader.item(i,1).text()
                headers[k] = v

        if type == 'GET':
             r = requests.get(url, headers=headers, params=params)
        elif type == 'POST':
             r = requests.post(url, headers=headers, params=params)
        elif type == 'PUT':
             r = requests.put(url, headers=headers, params=params)
        elif type == 'DELETE':
             r = requests.delete(url, headers=headers, params=params)

        # 在文本展示框体处理信息
        self.ui.textBrowser.append('--------发送请求--------\n\n'
                                    +type + ' ' + r.url)
        for k, v in headers.items():
            self.ui.textBrowser.append(k + ': ' + v)

        self.ui.textBrowser.append('\n\n--------得到响应--------\n')
        for k, v in r.headers.items():
            self.ui.textBrowser.append(k + ': ' + v)

        self.ui.textBrowser.append('\n' + r.text)

        # print(self.ui.tableWidgetHeader.rowCount())
        # print(self.ui.tableWidgetHeader.currentRow())
        # print(headers)

    def clearTextBrowser(self):
        self.ui.textBrowser.clear()

    def addRow(self):
        self.ui.tableWidgetHeader.insertRow(0)

    def delRow(self):
        currow = self.ui.tableWidgetHeader.currentRow()
        self.ui.tableWidgetHeader.removeRow(currow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())