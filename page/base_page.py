# -*- endcoding :utf-8 -*-
from common.util import my_selenium
from common.csv_operation.element_csv_operation import elementCsvOperation
from common.util.case_csv_operation import caseCsvOperation
from common.util.log import *
from common.data.global_value import colorSingleton

class basePage(object):
    def __init__(self, browser):
        self.mySelenium = my_selenium.MySelenium(browser)
        self.colorSingleton = colorSingleton()

    def setter_caseData(self, laneNum):
        '''
        获取对应页面的对应案例的信息
        '''
        self.__case_data = self.case_csv_operation.setter_caseData(laneNum)
        log("获取【%s】信息成功" % laneNum)

    def get_caseData(self):
        return self.__case_data

    def get_verify_data(self, laneNum):
        '''
        获取对应页面的对应案例的信息
        '''
        self.__verify_data = self.case_csv_operation.get_col(laneNum)
        log("获取【%s】验证信息成功" % laneNum)

    def open_url(self, caseNum):
        self.element_csv_operation = elementCsvOperation(caseNum)
        self.case_csv_operation = caseCsvOperation(caseNum)
        self.mySelenium.open_url(self.element_csv_operation.get_url, self.element_csv_operation.get_url_title)
        self.mySelenium.delete_cookie("userToken")
        self.mySelenium.add_cookie("userToken", '{"value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkyMDExOTUyNzYxMjE3MDI0LCJwaCI6IiIsImVtIjoiMTNAcS5jb20iLCJjIjoiIiwiZGUiOiJXaW5kb3dzIDEwL0Nocm9tZTcyLjAuMzYyNi4xMjEiLCJpcCI6IjE5Mi4xNjguMTEzLjQyIiwib3MiOjMsImlhdCI6MTU1MzIyNTQxNH0.ngU35LuWR0NFFGA79I8jcR0UvWrZDp43O8Uc695eohc","domain":".qb.com","path":"/","time":false}')
        self.mySelenium.refresh()
        self.mySelenium.open_url(self.element_csv_operation.get_url, self.element_csv_operation.get_url_title)
        self.mySelenium.set_max()

    def sendkeys_control(self, controlName):
        #获取填写的内容
        content = self.__case_data[self.case_csv_operation.get_element_index(controlName)]
        if content:
            try:
                element_message = self.element_csv_operation.get_col(controlName)
                self.mySelenium.send_keys(element_message, content)
            except Exception:
                log("获取【%s】的定位信息失败" % controlName)
                self.mySelenium.get_screenshot
                self.mySelenium.close_browser()

    def click_control(self, controlName):
        '''按钮控件，如果是YES的话执行，否则不执行'''
        content = self.__case_data[self.case_csv_operation.get_element_index(controlName)]
        if content == "YES":
            try:
                element_message = self.element_csv_operation.get_col(controlName)
                self.mySelenium.click(element_message)
            except Exception:
                log("获取【%s】的定位信息失败" % controlName)
                self.mySelenium.get_screenshot
                self.mySelenium.close_browser()

    def save_control(self, controlName, laneNum):
        '''如果是保存的话，进行保存。否则不执行'''
        content = self.__case_data[self.case_csv_operation.get_element_index(controlName)]
        if content == "保存":
            try:
                element_message = self.element_csv_operation.get_col(controlName)
                element_content = self.mySelenium.get_element_context(element_message)
                self.colorSingleton.add_value(laneNum, element_content)
            except Exception:
                log("获取【%s】的文本失败" % controlName)
                self.mySelenium.get_screenshot
                self.mySelenium.close_browser()

    def operation_controls(self, controls, laneNum):
        '''
        遍历所以控件
        '''
        for control in controls:
            if "文本框" in control:
                self.sendkeys_control(control)
                time.sleep(0.5)
            elif "按钮" in control:
                self.click_control(control)
                time.sleep(0.5)
            elif "显示框" in control:
                self.save_control(control, laneNum)
                time.sleep(0.5)

    def verify(self, controlName, laneNum):
        #获取预期结果
        try:
            self.get_verify_data(laneNum)
            content = self.__verify_data[self.case_csv_operation.get_element_index(controlName)]
            if content == self.mySelenium.get_current_title:
                log("实际结果%s等于预期结果%s" % (self.mySelenium.get_current_title, content))
            else:
                if self.colorSingleton.realityColor == self.colorSingleton.successColor:
                    self.colorSingleton.change_failure()
                log("实际结果%s不等于预期结果%s" % (self.mySelenium.get_current_title, content))
        except:
            log("无验证信息")


    def verify_text(self, controlName):
        '''获取文本内容，并与预期结果对比'''
        #获取预期结果
        content = self.__verify_data[self.case_csv_operation.get_element_index(controlName)]
        #获取实际结果
        element_message = self.element_csv_operation.get_col(controlName)
        verify_content = self.mySelenium.get_element_context(element_message)
        if content == verify_content:
            log("实际结果%s等于预期结果%s" % (verify_content, content))
        else:
            if self.colorSingleton.realityColor == self.colorSingleton.successColor:
                self.colorSingleton.change_failure()
            log("实际结果%s不等于预期结果%s" % (verify_content, content))

    def verify_save_data(self, controlName):
        '''获取显示框内容，并与预期结果对比'''
        # 获取预期结果
        cont = self.__verify_data[self.case_csv_operation.get_element_index(controlName)]
        cons = cont.split(",")
        content = self.colorSingleton.get_value(cons[0])
        # 获取实际结果
        element_message = self.element_csv_operation.get_col(controlName)
        verify_content = self.mySelenium.get_element_context(element_message)
        if content == verify_content:
            log("实际结果%s等于预期结果%s" % (verify_content, content))
        else:
            if self.colorSingleton.realityColor == self.colorSingleton.successColor:
                self.colorSingleton.change_failure()
            log("实际结果%s不等于预期结果%s" % (verify_content, content))

    def operation_verify(self, controls, laneNum):
        '''
        遍历所有断言
        '''
        #判断是否有断言如果有执行断言，否则不执行
        self.get_verify_data(laneNum)
        if self.__verify_data:
            for control in controls:
                if "文本框" in control:
                    self.verify_text(control, laneNum)
                elif "显示框" in control:
                    self.verify_save_data(control)
                else:
                    self.verify(control, laneNum)
        else:
            log("无断言")




    def test_progress(self, caseNum, laneNum):
        '''
        执行案例的步骤
        :param caseNum: 案例编号
        :param url: 网址
        :param url_title: 网页标题
        :param element_file_path: 定位元素需要的csv文件的路径
        :param case_file_path: 案例csv路径
        '''
        self.open_url(caseNum)
        log("开始执行%s案例" % caseNum)
        self.setter_caseData(caseNum)
        controls = self.case_csv_operation.get_control()
        self.operation_controls(controls, laneNum)
        log("开始验证断言")
        self.operation_verify(controls, laneNum)
        log("验证完成")
        self.close_webpage()
        time.sleep(2)
        log("结束执行%s案例" % caseNum)

    def close_webpage(self):
        self.mySelenium.close_webpage()

    def close_browser(self):
        self.mySelenium.close_browser()

