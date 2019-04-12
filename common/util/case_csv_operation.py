# -*- endcoding:utf-8 -*-
from common.util.csv_operation import csvOperation
from common.util.path_config import pathConfig
class caseCsvOperation(csvOperation):

    def __init__(self, laneNum):
        pathcon = pathConfig()
        caseList = laneNum.split("-")
        caseL = caseList[1].split("_")
        path = pathcon.casePath + caseL[0][1:] + "Case.csv"
        super(caseCsvOperation, self).__init__(path)


    def get_element_index(self, controlName):
        csv_title = self.reader["CaseNum"]
        return csv_title.index(controlName)

    def get_control(self):
        csv_title = self.reader["CaseNum"]
        return csv_title[3:]

    def setter_caseData(self, laneNum):
        '''
        获取对应页面的对应案例的信息
        '''
        caseNum = laneNum.split("-")
        caseN = caseNum[1].split("_")
        case_data = self.get_col(caseN[1][:len(caseN[1]) - 1])
        return case_data
