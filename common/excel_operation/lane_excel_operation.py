#-*- endcoding:utf-8 -*-
from common.util.excel_operation import exceOperation
from common.util.path_config import pathConfig

class laneExcelOperation(exceOperation):

    def __init__(self):
        con = pathConfig()
        path = con.lanePath
        super(laneExcelOperation, self).__init__(path)

    def is_run(self, value):
        run_value = value[1]
        if run_value.value != "YES":
            return False
        elif run_value.value == "YES":
            return True



