# -*- endcoding:utf-8 -*-
import webbrowser
import time
import os
from dataclasses import dataclass
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .log import log
from model.MyExecption import UntilNoElementOrTimeoutError
# 重复定位一个元素次数
FINDELELMENTTIMES = 3

@dataclass
class _ElementDisplayWaiting(object):
    """
    该类定义元素各种显示等待
    """
    driver: webbrowser
    timeout: float
    detection: float
    execption: EC

    def __post_init__(self):
        self.wait = Wait(driver=self.driver, timeout=self.timeout, poll_frequency=self.detection, ignored_exceptions=self.execption)

    def show_element(self, element):
        """
        判断单个元素在规定时间内是否出现
        :param element: 定位元素的方式
        :return: 已经出现的元素
        """
        return self.wait.until(EC.presence_of_element_located(element), message=UntilNoElementOrTimeoutError(self.timeout, element))

    def show_elemets(self, elements):
        """
        判断一组元素在规定时间内是否出现
        :param elements:
        :return:
        """
        return self.wait.until(EC.presence_of_all_elements_located(elements), message=UntilNoElementOrTimeoutError(self.timeout, elements))

    def display_element(self, element):
        """
        判断单个元素是否在规定时间内是否消失
        :param element:
        :return:
        """
        return self.wait.until_not(EC.presence_of_element_located(element), message=UntilNoElementOrTimeoutError(self.timeout, element))

    def display_elements(self, elements):
        """"
        判断一组元素在规定时间内是否消失
        :param elements:
        :return:
        """
        return self.wait.until_not(EC.presence_of_all_elements_located(elements), message=UntilNoElementOrTimeoutError(self.timeout, elements))

@dataclass
class _MouseToOperations(_ElementDisplayWaiting):
    """
    该类定义鼠标操作元素
    """
    def __post_init__(self):
        super(_MouseToOperations, self)
class MySelenium(object):

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """
        打开网址，并验证是否正确
        :param url: 网址
        :param url_title: 网站的title
        :return:
        """
        try:
            js = 'window.open("%s");' % url
            self.driver.execute_script(js)
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
        except:
            log("打开网址%s失败" % url)
            self.get_screenshot
            log("案例结束")
            self.close_webpage()

    def set_max(self):
        """
        设置浏览器窗口最大化
        """
        self.driver.maximize_window()

    def close_browser(self):
        """
        关闭浏览器
        """
        self.driver.quit()

    def close_webpage(self):
        """
        关闭单个网页
        :return:

        """
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    def refresh(self):
        """
        刷新页面
        """
        self.driver.refresh()
        log("刷新页面成功")

    @property
    def get_current_title(self):
        """获取标题"""
        return self.driver.title

    @property
    def get_current_url(self):
        """获取当前网页的网址"""
        return self.driver.current_url


    def get_screenshot(self, line_num):
        """
        截图
        :param line_num: 案例名称

        """
        image_path = os.curdir + "/screenshot/" + line_num + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + '.png'
        self.driver.get_screenshot_as_file(image_path)
        log("截图成功")



    def find_element(self, control):
        """
        定位元素，并且返回
        :param control: 操作的控件
        :return: 元素
        """

        for i in range(0, FINDELELMENTTIMES):
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((eval(control.find_element_type), control.find_element_value)))
            return element



    def click(self, control):
        """
        点击元素
        """
        element = self.find_element(control)
        ActionChains(self.driver).click(element).perform()
        log("点击元素【%s】成功" % control.name)



    def send_keys(self,  control):
        """
        向文本框填写数据
        :param control: 控件
        :return:
        """
        element = self.find_element(control)
        element.clear()
        element.send_keys(control.value)
        log("填写元素【%s-%s】成功" % (control.name, control.value))





    def double_click(self, control):
        element = self.find_element(control)
        ActionChains(self.driver).double_click(element).perform()
        log("双击元素【%s】成功" % control.name)


    def move_to_element(self, control):
        element = self.find_element(control)
        ActionChains(self.driver).move_to_element(element).perform()
        log("悬停元素【%s】成功" % control.name)



    def get_element_context(self, control):
        """
        获取文本内容
        """
        element = self.find_element(control)
        content = element.text
        log("获取文本【%s】内容成功---%s" % (control.name, control.value))
        return content

    def get_attribute_context(self, attribute, element_path):
        """
        获取元素的文本内容
        :param attribute: 需要获取的元素属性值
        :param element_path: 文件page_element相对应的东西
        :return: 元素属性的值
        """
        content = self.find_element(element_path).get_attribute(attribute)
        return content


    def get_cookie(self, cookie_name):
        """
        操作cookie
        :param cookie_name:
        :return:
        """
        cookie = self.driver.get_cookie(cookie_name)
        log("获取cookie-%s成功：%s" % (cookie_name, cookie))


    def delete_cookie(self, cookie_name):
        self.driver.delete_cookie(cookie_name)


    def add_cookie(self, cookie_name, cookie_value):
        self.driver.add_cookie({"name": cookie_name,
                                "value": cookie_value})
        log("添加cookie-%s成功" % cookie_name)



