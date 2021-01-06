import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHeaderView
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem

d = [['a', 'b', 'c', 'd'],
     ['a1', 23, 66, 78.9],
     ['a2', 343, 54, 56]]

class MyTable(QWidget):

    def __init__(self, row=1, col=1, header=[]):
        super().__init__()
        self.row = row
        self.col = col
        self.header = header
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setColumnCount(self.col)
        layout.addWidget(self.label)
        layout.addWidget(self.tableWidget)
        # 设置表头
        self.tableWidget.setHorizontalHeaderLabels(self.header)
        # 设置表头风格
        self.tableWidget.horizontalHeader().setStyleSheet(
            'QHeadView::section{background:gray}')
        # 设置表头选择行为
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 不显示重复表头
        self.tableWidget.verticalHeader().setVisible(False)
        self.setLayout(layout)

    def insert_data(self, data=None):
        if data:
            for r in range(self.row - 1):
                for c in range(self.col):
                    item = QTableWidgetItem(str(data[r][c]))
                    self.tableWidget.setItem(r, c, item)
            self.label.setText(f'表格行数：{self.row}\n表格列数：{self.col}')
        else:
            self.label.setText('无数据')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = MyTable()
    table.insert_data()
    table.show()
    sys.exit(app.exec_())
