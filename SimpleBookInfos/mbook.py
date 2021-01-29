# -*- coding: utf-8 -*-

"""
Module implementing Mbook.
"""

from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QComboBox, QMessageBox, QMenu, QAction, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIcon, QPixmap

from Ui__mainUI import Ui_MainWindow
from createbook import CreateBook

from datamanagement import DataManagement

class Mbook(QMainWindow, Ui_MainWindow):
    """
    图书管理
    """
    bookdb = DataManagement()
    booklist = []
    def __init__(self, parent=None):
        """
        设置一些表格样式
        """
        super(Mbook, self).__init__(parent)
        self.setupUi(self)
        self.initUi() 
    
    def initUi(self):
        searchkey = ["ISBN", "书名", "作者"]
        self.comboBox.addItems(searchkey)
        self.tableWidget.setIconSize(QSize(55,25))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.showtable()

    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        双击修改
        """
        if column == 0:
            countries = ["中", "英", "日", "俄", "美"]
            com_country = QComboBox()
            old_classification = self.booklist[row]["country"]
            com_country.addItem(QIcon("./res/countries/china.png"),"中")
            com_country.addItem(QIcon("./res/countries/english.png"),"英")
            com_country.addItem(QIcon("./res/countries/japan.png"),"日")
            com_country.addItem(QIcon("./res/countries/russian.png"),"俄")
            com_country.addItem(QIcon("./res/countries/usa.png"),"美")
            if old_classification not in countries:
                com_country.addItem(QIcon("./res/countries/default.png"), old_classification)

            com_country.setCurrentText(old_classification)
            self.tableWidget.setCellWidget(row, 0, com_country)

        if column == 5:
            com = QComboBox()
            classifications = ["", "马克思主义、列宁主义、毛泽东思想、邓小平理论", "哲学、宗教", "社会科学总论", 
            "政治、法律", "军事", "经济", "文化、科学、教育、体育", "语言、文字", "文学", 
            "艺术", "历史、地理", "自然科学总论", "数理科学和化学", "天文学、地球科学", "生物科学", 
            "医药、卫生", "农业科学", "工业技术", "交通运输", "航空、航天", "环境科学、劳动保护科学（安全科学）", 
            "综合性图书"]
            com.addItems(classifications)
            com.setEditable(True)
            old_classification = self.booklist[row]["classification"]
            com.setCurrentText(old_classification)
            self.tableWidget.setCellWidget(row, 5, com)
        
        self.pushButton_save.setEnabled(True)

    @pyqtSlot(QTableWidgetItem)
    def on_tableWidget_itemActivated(self, item):
        """
        按住Enter键时
        """    
        row = self.tableWidget.row(item)
        column = self.tableWidget.column(item)
        totalrow = self.tableWidget.rowCount()
        if row + 1 < totalrow:
            row = self.tableWidget.row(item) + 1
            self.tableWidget.setCurrentCell(row, column)
        elif row + 2 == totalrow:
            self.tableWidget.setCurrentCell(totalrow, column)

    @pyqtSlot(int, int, int, int)
    def on_tableWidget_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        """
        当前单元格改变
        """

        if previousColumn == 1:
            isbn = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["isbn"] = isbn
        if previousColumn == 2:
            bookname = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["subtitle"] = bookname
        if previousColumn == 3:
            author = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["author"] = author
        if previousColumn == 4:
            publisher = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["publisher"] = publisher
        if previousColumn == 6:
            price = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["price"] = price
        else:
            previous_item = self.tableWidget.cellWidget(previousRow, previousColumn)
            if previous_item:
                text = previous_item.currentText()
                self.tableWidget.removeCellWidget(previousRow, previousColumn)
                if previousColumn == 5:
                    cl = QTableWidgetItem(text)
                    cl.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(previousRow, 5, cl)
                    self.booklist[previousRow]["classification"] = text
                if previousColumn == 0:
                    if text == "中":
                        countryIcon = QIcon("./res/countries/china.png")
                    elif text == "英":
                        countryIcon = QIcon("./res/countries/english.png")
                    elif text == "日":
                        countryIcon = QIcon("./res/countries/japan.png")
                    elif text == "俄":
                        countryIcon = QIcon("./res/countries/russian.png")
                    elif text == "美":
                        countryIcon = QIcon("./res/countries/usa.png")
                    else:
                        countryIcon = QIcon("./res/countries/default.png")
                    country_item = QTableWidgetItem(countryIcon, text)   
                    country_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)       
                    self.tableWidget.setItem(previousRow, 0, country_item)
                    self.booklist[previousRow]["country"] = text

    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        """
        单击显示图书详细信息
        """
        self.label_country.setText(self.booklist[row]["country"])
        self.label_isbn.setText(self.booklist[row]["isbn"])
        self.label_bookname.setText(self.booklist[row]["subtitle"])
        self.label_author.setText(self.booklist[row]["author"])
        self.label_publisher.setText(self.booklist[row]["publisher"])
        self.label_price.setText(self.booklist[row]["price"])
        self.label_pubdate.setText(self.booklist[row]["pubdate"])
        self.label_classification.setText(self.booklist[row]["classification"])           
        self.label_pages.setText(self.booklist[row]["pages"])
        self.textBrowser.setText(self.booklist[row]["summary"])
        img = self.booklist[row]["img"]
        imgname = './res/book/' + img.split("/")[-1]
        self.label.setPixmap(QPixmap(imgname))

    @pyqtSlot()
    def on_pushButton_search_clicked(self):
        """
        查找图书
        """
        searchtext = self.lineEdit.text()
        if searchtext:
            if self.comboBox.currentText() == "ISBN":
                index = self.bookdb.query_db(isbn = searchtext)
            elif self.comboBox.currentText() == "书名":
                index = self.bookdb.query_db(bookname = searchtext)
            elif self.comboBox.currentText() == "作者":
                index = self.bookdb.query_db(author = searchtext)
            if index > -1:
                self.tableWidget.selectRow(index)
            else:
                QMessageBox.information(self, "提示", "Sorry。貌似没有找到你要的书，换个词试试吧！")
        else:
            QMessageBox.information(self, "提示", "没有搜索关键词啊！")

    @pyqtSlot()
    def on_pushButton_createbook_clicked(self):
        """
        新增图书
        """
        bookinfo = CreateBook()
        r = bookinfo.exec_()
        if r > 0:
            self.showtable()

    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        保存修改
        """
        self.bookdb.save_db(self.booklist)
        QMessageBox.information(self, "提示", "保存成功！")
        self.pushButton_save.setEnabled(False)

    def showtable(self):
        """
        表格呈现
        """
        self.booklist = self.bookdb.load()
        list_rows = len(self.booklist)
        table_rows = self.tableWidget.rowCount()
        if table_rows == 0 and list_rows > 0:
            self.selectTable(self.booklist, table_rows)
        elif table_rows > 0 and list_rows > 0:
            self.removeRows(table_rows)
            self.selectTable(self.booklist, table_rows)
            
    def selectTable(self, booklist, table_rows):
        """
        表格呈现具体的数据
        """
        for i, book in enumerate(booklist):
            country = book["country"]
            isbn = book["isbn"]
            subtitle = book["subtitle"]
            author = book["author"]
            publisher = book["publisher"]
            price = book["price"]
            classification = book["classification"]   
            # row = i

            self.tableWidget.insertRow(i)

            if country == "中":
                countryIcon = QIcon("./res/countries/china.png")
            elif country == "英":
                countryIcon = QIcon("./res/countries/english.png")
            elif country == "日":
                countryIcon = QIcon("./res/countries/japan.png")
            elif country == "俄":
                countryIcon = QIcon("./res/countries/russian.png")
            elif country == "美":
                countryIcon = QIcon("./res/countries/usa.png")
            else:
                countryIcon = QIcon("./res/countries/default.png")

            country_item = QTableWidgetItem(countryIcon,country)   
            country_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)       
            self.tableWidget.setItem(i, 0, country_item)

            isbn_item = QTableWidgetItem(isbn)
            isbn_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            bookname_item = QTableWidgetItem(subtitle)
            bookname_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            author_item = QTableWidgetItem(author)
            author_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            publisher_item = QTableWidgetItem(publisher)
            publisher_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            classification_item = QTableWidgetItem(classification)
            classification_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            price_item = QTableWidgetItem(price)
            price_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget.setItem(i, 1, isbn_item)
            self.tableWidget.setItem(i, 2, bookname_item)
            self.tableWidget.setItem(i, 3, author_item)
            self.tableWidget.setItem(i, 4, publisher_item)
            self.tableWidget.setItem(i, 5, classification_item)
            self.tableWidget.setItem(i, 6, price_item)

    def contextMenuEvent(self, event):
        """
        右键菜单
        """
        pmenu = QMenu(self)
        pDeleteAct = QAction('删除行',self.tableWidget)
        pmenu.addAction(pDeleteAct)
        pDeleteAct.triggered.connect(self.deleterows)
        pmenu.popup(self.mapToGlobal(event.pos()))
    
    def closeEvent(self, event):
        """
        提示保存
        """
        if self.pushButton_save.isEnabled():
            r = QMessageBox.warning(self, "注意", "你是不是没有保存啊，现在保存下？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if r == QMessageBox.No:
                event.accept()
            else:
                event.ignore()

    def deleterows(self):
        """
        删除行
        """
        rr = QMessageBox.warning(self, "注意", "删除可不能恢复了哦！", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if rr == QMessageBox.Yes:
            curow = self.tableWidget.currentRow()
            selections = self.tableWidget.selectionModel()
            selectedsList = selections.selectedRows()
            rows = []
            for r in selectedsList:
                rows.append(r.row())
            if len(rows) == 0:
                rows.append(curow)
                self.removeRows(rows, isdel_list = 1)
            else:
                self.removeRows(rows, isdel_list = 1)
    
    def removeRows(self, rows, isdel_list = 0):
        """
        删除单元格
        """
        if isdel_list != 0:
            rows.reverse()
            for i in rows:
                self.tableWidget.removeRow(i)
                del self.booklist[i]
            self.bookdb.save_db(self.booklist)
        else:
            for i in range(rows-1, -1, -1):
                self.tableWidget.removeRow(i)