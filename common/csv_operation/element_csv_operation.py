#-*- endcoding:utf-8 -*-
from common.util.csv_operation import csvOperation
from common.util.path_config import pathConfig

class elementCsvOperation(csvOperation):
    def __init__(self, caseL):
        pathcon = pathConfig()
        path = pathcon.elementPath + caseL[0][1:] + "Element.csv"
        super(elementCsvOperation, self).__init__(path)

    def get_control(self, control):
        cont_list = self.reader[control.name]
        control.set_find_element_type(cont_list[1])
        control.set_find_element_value(cont_list[2])

if __name__ == '__main__':
    a = elementCsvOperation("1")
    a.get_control()