# coding: utf-8

import xlrd
from xlrd import xldate_as_tuple
import datetime


class ExcelData(object):
    """Read excel file with extent 'xls'.
    """

    def __init__(self, filepath, output_format=True):
        """Init ExcelData with filepath.

        :param filepath: A string of excel file path.
        :param output_format: A optional bool variable. True for dict, False for
               list.
        """
        self.filepath = filepath
        self.output_format = output_format
        self.workbook = xlrd.open_workbook(self.filepath)
        self.worksheets = self.workbook.sheet_names()

    def get_sheet_names(self):
        """Get sheet names.

        :return: A list consist all sheet names in excel file.
        """
        return self.worksheets

    def get_sheet_number(self):
        """Get numbers of all sheets in a excel file.

        :return: A int number
        """
        return len(self.worksheets)

    def get_info_by_name(self, sheetname):
        """Get detail data in a sheet,indexed by name.

        :param sheetname: A string representing the sheet name of a excel file.
        :return: A dict. For example:
            {'nrow': 2,
             'ncol': 2,
             'data': [
                      {'name': 张三, '性别': male, 'age': 20}
                      {'name': Amy, '性别': female, 'age': 30}
                     ]
            }
        """
        sheet_info = {}
        data = []
        cur_sheet = self.workbook.sheet_by_name(sheetname)
        nrow = cur_sheet.nrows
        ncol = cur_sheet.ncols
        sheet_info['nrow'] = nrow
        sheet_info['ncol'] = ncol
        for i in range(0, nrow):
            if not self.output_format:
                _sheet_data = []
            else:
                _sheet_data = {}
            for j in range(ncol):
                ctype = cur_sheet.cell_type(i, j)
                cvalue = cur_sheet.cell_value(i, j)
                # excel数据类型：(0,empty) (1,text) (2,number) (3,xldate) (4,bool)
                if ctype == 2 and cvalue % 1 == 0:
                    cvalue = int(cvalue)
                elif ctype == 3:
                    # 转化为datetime类型
                    _date = datetime.datetime(xldate_as_tuple(cvalue, 0))
                    cvalue = _date.strftime("%Y/%d/%m %H:%M:%S")
                elif ctype == 4:
                    cvalue = True if cvalue == 1 else False
                if not self.output_format:
                    _sheet_data.append(cvalue)
                else:
                    _sheet_data[cur_sheet.row_values(0)[j]] = cvalue
            data.append(_sheet_data)
        sheet_info['Data'] = data
        return sheet_info

    def get_sheet_info(self):
        """Get all sheets data.

        :return: A list consisting of some dicts representing each single sheet.
        """
        wb_info = []
        for name in self.get_sheet_names():
            _tmp_dict = {}
            sheet_info = self.get_info_by_name(name)
            _tmp_dict['name'] = name
            _tmp_dict['sheet_data'] = sheet_info
            wb_info.append(_tmp_dict)
        return wb_info


if __name__ == '__main__':
    # e = ExcelData('./res/student_data.xls', False)
    e = ExcelData('./res/data_format_unified.xls', False)
    data = e.get_sheet_info()
    print(data[0]['sheet_data']['Data'][0:1])
    print(e.get_sheet_names())
    # print(e.get_info_by_name('sheet1'))