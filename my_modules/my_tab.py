import sys
from PyQt5.QtWidgets import QTabWidget, QFormLayout, QWidget, QApplication, QVBoxLayout
from read_excel_file import ExcelData
from my_table import MyTable


class MyTab(QTabWidget):

    def __init__(self, parent=None):
        super(MyTab, self).__init__(parent)
        self.parent = parent
        self.create_tabwidget()
        self.setWindowTitle('Tab Demo')
        self.resize(900, 300)

    def create_tabwidget(self):
        # load excel file
        # data = ExcelData('./res/student_data.xls', False)
        data = ExcelData('./res/data_format_unified.xls', False)
        table_names = data.get_sheet_names()
        # 去掉numbers转化xls文件带来的无用sheet
        # table_names = table_names[1:]
        for name in table_names:
            table_data = data.get_info_by_name(name)
            nrow = table_data['nrow']
            ncol = table_data['ncol']
            headers = table_data['Data'][0]
            datas = table_data['Data'][1:]
            self.tab = QWidget()
            self.addTab(self.tab, name)
            layout = QVBoxLayout()
            _tmp_table = MyTable(row=nrow, col=ncol, header=headers)
            _tmp_table.insert_data(datas)
            layout.addWidget(_tmp_table)
            self.tab.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MyTab()
    demo.show()
    sys.exit(app.exec_())
