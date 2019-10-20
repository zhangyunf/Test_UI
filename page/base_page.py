# -*- endcoding :utf-8 -*-
from common.util import my_selenium
from common.util.log import *
from common.data.global_value import colorSingleton
from common.util.slider_verification import CrackSlider
import time
class basePage(object):
    def __init__(self, browser):
        self.mySelenium = my_selenium.MySelenium(browser)
        self.colorSingleton = colorSingleton()

    def open_url(self, url):
        self.mySelenium.open_url(url)
        self.mySelenium.set_max()

    def sendkeys_control(self, control):
        if control.value:
            self.mySelenium.send_keys(control)

    def click_control(self, control):
        '''按钮控件，如果是YES的话执行，否则不执行'''
        if control.value == "YES":
            self.mySelenium.click(control)


    def save_control(self, control, line_num):
        '''如果是保存的话，进行保存。否则不执行'''
        if control.value == "保存":
            element_content = self.mySelenium.get_element_context(control)
            self.colorSingleton.add_value(line_num, element_content)

    def verity_hint(self, case, control, line_num):

        if control.value:
            current_hint = self.mySelenium.get_element_context(control)
            if current_hint == control.value:
                log("%s提示语正确" % control.value)
            else:
                case.result = False
                log("%s提示语不正确" % control.value)
                self.mySelenium.get_screenshot(line_num)

    def crack_slider(self, control, driver):
        if(control.value):
            c = CrackSlider(driver)
            c.crack_slider()


    def operation_controls(self, case, line_num, driver):
        '''
        遍历所以控件
        '''
        for control in case.controls_list:
            try:
                if "文本框" in control.name:
                    self.sendkeys_control(control)
                    time.sleep(0.2)
                elif "按钮" in control.name:
                    self.click_control(control)
                    time.sleep(0.2)
                elif "显示框" in control.name:
                    self.save_control(control, line_num)
                    time.sleep(0.2)
                elif "滑块验证码" in control.name:
                    self.crack_slider(control, driver)
                elif "提示元素" in control.name:
                    self.verity_hint(case, control, line_num)
                elif "比较" in control.name:
                    self.verity_hint(case, control, line_num)
                elif "sleep" in control.name:
                    if control.value:
                        time.sleep(int(control.value))
            except:
                case.false_log = "获取【%s】的定位信息失败" % control.name
                log(case.false_log)
                self.mySelenium.get_screenshot(case.name)
                case.result = False
                time.sleep(1)
                log("执行案例%s失败" % case.name)
                break

    def test_progress(self, case, line_num, driver):
        '''
        执行案例的步骤
        :param caseNum: 案例编号
        :param url: 网址
        :param url_title: 网页标题
        :param element_file_path: 定位元素需要的csv文件的路径
        :param case_file_path: 案例csv路径
        '''
        self.open_url(case.url)
        log("开始执行%s案例" % case.name)
        self.operation_controls(case, line_num, driver)

        if case.result == None:
            case.result = True
        if case.result != False and case.result != None:
            self.mySelenium.get_screenshot(case.name)

        self.close_webpage()

        log("结束执行%s案例" % case.name)

    def close_webpage(self):
        self.mySelenium.close_webpage()

    def close_browser(self):
        self.mySelenium.close_browser()

