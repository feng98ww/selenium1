import xlrd
from xlutils.copy import copy


class ReadExcel(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = '../data/test.xls'
            self.index = 0
        else:
            self.excel_path = excel_path
            self.index = index

        # 打开 excel文件，获取数据库列表
        self.data = xlrd.open_workbook(self.excel_path)
        # 读取第一页 sheet页数据
        self.table = self.data.sheets()[0]

    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != '':
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的值
    def get_cell(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)
        write_data.get_sheet(self.index).write(row, col, value)
        write_data.save("data/test.xls")
        write_data.save(self.excel_path)


if __name__ == "__main__":
    re = ReadExcel()
    print(re.get_data())
    print(re.get_lines())
    print(re.get_cell(0, 0))
    re.write_data(11, 0, 123456)


