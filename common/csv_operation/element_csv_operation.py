#-*- endcoding:utf-8 -*-
from common.util.csv_operation import csvOperation
from common.util.path_config import pathConfig

class elementCsvOperation(csvOperation):
    def __init__(self, caseNum):
        pathcon = pathConfig()
        caseList = caseNum.split("-")
        caseL = caseList[1].split("_")
        path = pathcon.elementPath + caseL[0][1:] + "Element.csv"
        super(elementCsvOperation, self).__init__(path)

    @property
    def get_url(self):
        '''
        获取网址
        :return:
        '''
        lis = self.reader["elementName"]
        return lis[-2]

    @property
    def get_url_title(self):
        '''
        获取网址标题
        :return:
        '''
        lis = self.reader["elementName"]
        return lis[-1]
