#-*- endcoding:utf-8 -*-
from selenium import webdriver
from page.base_page import basePage
from common.excel_operation.lane_excel_operation import laneExcelOperation
from common.util.log import *
from common.data.global_value import colorSingleton

class main(object):

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.testP = basePage(self.browser)
        self.lane = laneExcelOperation()
        self.lane.get_datas("Sheet1")
        self.colorSingleton = colorSingleton()

    def run(self):
        '''
        运行需要执行的泳道
        '''
        for lanNum, caseList in self.lane.reader.items():
            # 表头不执行
            if self.lane.get_value(lanNum) != "laneNum":
                # 判断该泳道是否执行
                if self.lane.is_run(caseList):
                    log("泳道%s开始执行" % self.lane.get_value(lanNum))
                    for test in caseList[3:]:
                        #初始化案例背景颜色
                        self.colorSingleton.change_success()
                        # 判断是否为空
                        if self.lane.get_value(test) != None:
                            try:
                                self.testP.test_progress(self.lane.get_value(test), lanNum)
                                self.lane.set_cell_color(test)
                            except Exception:
                                log("案例%s执行失败" % self.lane.get_value(test))
                                self.lane.set_cell_color(test)
                                break
                    log("泳道%s结束执行" % lanNum.value)
        self.browser.quit()

if __name__ == "__main__":
    run = main()
    run.run()

# mySelenium = my_selenium.MySelenium(browser)
# mySelenium.open_url("http://www.qb.com/", "QB.com-全球优质数字资产交易平台")
# mySelenium.set_max()
# mySelenium.get_cookie("userToken")
# mySelenium.delete_cookie("userToken")
# mySelenium.add_cookie("userToken",
#                       '{"value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA3OTY3NjIyNjQ3OTE0NDk2LCJwaCI6IiIsImVtIjoiMzBAZi5jb20iLCJjIjoiIiwiZGUiOiJXaW5kb3dzIDEwL0Nocm9tZTcxLjAuMzU3OC45OCIsImlwIjoiMTkyLjE2OC4xMTMuNDIiLCJvcyI6M30.Etuwc8A-OH3pyXFV4eL-mc_IhL_lpDOc8fz8aZQ0wjY","domain":".qb.com","path":"/","time":false}')
# mySelenium.refresh()
# time.sleep(30)
# mySelenium.get_screenshot()
# browser.quit()

