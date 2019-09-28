#-*- endcoding:utf-8 -*-
from common.util.excel_operation import exceOperation
from common.csv_operation.case_csv_operation import caseCsvOperation
from common.util.path_config import pathConfig
from model.Set import SetModel
from model.Scene import SceneModel

class laneExcelOperation(exceOperation):

    def __init__(self):
        con = pathConfig()
        path = con.lanePath
        super(laneExcelOperation, self).__init__(path)
        self.set_list = []

    def get_datas(self):
        self.get_set("首页")

    def get_set(self, sheet_name):
        '''
        获取需要执行的测试集
        :param sheet_name:
        :return:
        '''
        st = self.open_sheet(sheet_name)
        for row in st.rows:
            # 舍去第一行
            if row[0].row != 1:
                data = []
                for i in row:
                    data.append(i.value)
                set = SetModel(data)
                # 不需要执行的不进行添加
                if set.is_run == "YES":
                    self.set_list.append(set)
                # 读取泳道数据
                self.get_scene(set)



    def get_scene(self, set):
        '''
        获取泳道数据
        :param set: 测试集名称
        '''
        st = self.open_sheet(set.name)
        for row in st.rows:
            # 舍去第一行
            if row[0].row != 1:
                data = []
                for i in row:
                    data.append(i.value)
                scene = SceneModel(data)
                # 不需要执行的不进行添加
                if scene.is_run == "YES":
                    set.scene_list.append(scene)
                # 读取案例
                for i in range(3, len(data)):
                    # 获取案例
                    if data[i] != None:
                        case_operation = caseCsvOperation(data[i])
                        case = case_operation.get_case()
                        scene.case_list.append(case)



    def get_readers(self):
        return self.reader

    def is_run(self, value):
        run_value = value[1]
        if run_value.value != "YES":
            return False
        elif run_value.value == "YES":
            return True

if __name__ == '__main__':
    set  = laneExcelOperation()
    set.get_datas("首页")



