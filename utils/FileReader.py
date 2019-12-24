import yaml
import os

from xlrd import open_workbook


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data

    def get(self, element, index=0):
        return self.data[index].get(element)


class SheetTypeError(Exception):
    pass


class ExcelReader:
    class ExcelReader:
        """
        如果title_line=True，输出结果：[{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]
        如果title_line=False,输出结果：[[A,B,C], [A1,B1,C1], [A2,B2,C2]]
        通过index或者name：指定sheet
        """

        def __init__(self, excel, sheet=0, title_line=True):
            if os.path.exists(excel):
                self.excel = excel
            else:
                raise FileNotFoundError('文件不存在！')
            self.sheet = sheet
            self.title_line = title_line
            self._data = list()
            self.s = self.open_book()

        def open_book(self):
            if not self._data:
                workbook = open_workbook(self.excel)
                if type(self.sheet) not in [int, str]:
                    raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
                elif type(self.sheet) == int:
                    s = workbook.sheet_by_index(self.sheet)
                else:
                    s = workbook.sheet_by_name(self.sheet)
                return s

        @property
        def data(self):
            if self.title_line:
                title = self.s.row_values(0)  # 首行为title
                for col in range(1, self.s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, self.s.row_values(col))))
            else:
                for col in range(0, self.s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(self.s.row_values(col))
            return self._data

        @property
        def max_rows(self):
            if self.title_line:
                count = int(self.s.nrows) - 1
                return count
            else:
                count = int(self.s.nrows)
                return count


if __name__ == '__main__':
    e = r'F:\PyCharm\py_work\UI_AOTO\data\wxInquiryImportTemplate.xls'



