#-*- endcoding:utf-8 -*-
import csv

class csvOperation(object):

    def __init__(self, file_path):
        self.reader = {}
        try:
            with open(file_path, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) != 0:
                        self.reader.update({row[0]: row})
        except:
            with open(file_path, "rb", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) != 0:
                        self.reader.update({row[0]: row})

    def get_reader(self):
        return self.reader

    def get_col(self, cloName):
        '''
        获取控件名称
        :param cloName:
        :return:
        '''
        if cloName in self.reader.keys():
            return self.reader[cloName]
        else:
            return False





if __name__ == "__main__":
    c = csvOperation(r"D:\接口\Test_UI\data\caseExcel\testCase.csv")
    v = c.reader["【SY_001】-【test_1】-001"]
    print(v)