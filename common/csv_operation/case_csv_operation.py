# -*- endcoding:utf-8 -*-
from common.util.csv_operation import csvOperation
from common.csv_operation.element_csv_operation import elementCsvOperation
from common.util.path_config import pathConfig
from model.Case import CaseModel
from model.Controls import ControlsModel

class caseCsvOperation(csvOperation):

    def __init__(self, laneNum):
        pathcon = pathConfig()
        caseList = laneNum.split("-")
        self.laneNum = laneNum
        self.caseL = caseList[1].split("_")
        path = pathcon.casePath + self.caseL[0][1:] + "Case.csv"
        super(caseCsvOperation, self).__init__(path)


    def get_element_index(self, controlName):
        csv_title = self.reader["CaseNum"]
        return csv_title.index(controlName)

    def get_control(self):
        csv_title = self.reader["CaseNum"]
        return csv_title[4:]

    def get_case(self):
        """
        获取对应页面的对应案例的信息
        """
        case_data = self.get_col(self.caseL[1][:len(self.caseL[1]) - 1])
        case = CaseModel(case_data)
        case.name = self.laneNum
        controls_list = self.get_control()
        for i in range(4, len(case_data)):
            control = ControlsModel()
            control.set_value(case_data[i])
            control.set_name(controls_list[i - 4])
            element = elementCsvOperation(self.caseL)
            element.get_control(control)
            case.controls_list.append(control)
        return case
if __name__ == '__main__':
    a = caseCsvOperation("aa")
    case = a.get_case()
    case.description()
