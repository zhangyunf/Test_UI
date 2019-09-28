#-*- endcoding:utf-8 -*-
from selenium import webdriver
from common.util.screen_shot import *
from page.base_page import basePage
from common.excel_operation.set_excel_operation import laneExcelOperation
from common.util.log import *
from common.data.global_value import colorSingleton


class main(object):

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.baseP = basePage(self.browser)
        self.lane = laneExcelOperation()
        self.lane.get_datas()
        self.colorSingleton = colorSingleton()

    def run(self):
        '''
        运行需要执行的泳道
        '''
        # 清空截图
        clear_screenshot()
        for set in self.lane.set_list:
            log("开始执行%s测试集" % set.name)
            self.run_set(set)

    def run_set(self, set):
        try:
            for scene in set.scene_list:
                log("开始执行%s泳道" % scene.name)
                self.run_case(scene)
                set.case_num += scene.case_num
                set.case_success += scene.case_success
                set.case_false += scene.case_false
                set.non_execution += scene.non_execution

        finally:
            self.browser.quit()

    def run_case(self, scene):
        case_list = scene.case_list
        scene.case_num = len(case_list)
        line_num = scene.name
        for case in case_list:

            # 初始化案例背景颜色
            self.colorSingleton.change_success()
            # 判断是否为空
            if case != None:
                self.baseP.test_progress(case, line_num, self.browser)
                if case.result == True:
                    scene.case_success += 1
                elif case.result == False:
                    scene.case_false += 1
                    break
        scene.non_execution = scene.case_num - scene.case_success - scene.case_false

if __name__ == "__main__":
    run = main()
    run.run()

