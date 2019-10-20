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
        self.action = Wait(driver=self.driver, timeout=self.timeout, poll_frequency=self.detection, ignored_exceptions=self.execption)

    def show_element(self, element):
        """
        判断单个元素在规定时间内是否出现
        :param element: 定位元素的方式
        :return: 已经出现的元素
        """
        return self.action.until(EC.presence_of_element_located((eval(element.find_element_type), element.find_element_value)), message=UntilNoElementOrTimeoutError(self.timeout, element))

    def show_elemets(self, elements):
        """
        判断一组元素在规定时间内是否出现
        :param elements:
        :return:
        """
        return self.action.until(EC.presence_of_all_elements_located(elements), message=UntilNoElementOrTimeoutError(self.timeout, elements))

    def display_element(self, element):
        """
        判断单个元素是否在规定时间内是否消失
        :param element:
        :return:
        """
        return self.action.until_not(EC.presence_of_element_located(element), message=UntilNoElementOrTimeoutError(self.timeout, element))

    def display_elements(self, elements):
        """"
        判断一组元素在规定时间内是否消失
        :param elements:
        :return:
        """
        return self.action.until_not(EC.presence_of_all_elements_located(elements), message=UntilNoElementOrTimeoutError(self.timeout, elements))

@dataclass
class _MouseToOperations(_ElementDisplayWaiting):
    """
    该类定义鼠标操作元素
    * 点击
    * 右击
    * 双击
    * 拖拽
    * 悬浮
    * 填写内容
    """
    def __post_init__(self):
        super(_MouseToOperations, self).__post_init__()
        self.mouse_suppert = ActionChains(self.driver)


    def click(self, element):
        """鼠标单击"""
        ele = self.show_element(element)
        self.mouse_suppert.click(ele).perform()
        log("点击元素【%s】成功" % element.name)

    def context_click(self, element):
        """鼠标右击元素"""
        ele = self.show_element(element)
        self.mouse_suppert.context_click(on_element=ele).perform()
        log("右击元素【%s】成功" % element.name)

    def double_click(self, element):
        """
        鼠标双击
        :param element: 操作的元素
        """
        ele = self.show_element(element)
        self.mouse_suppert.double_click(on_element=ele).perform()
        log("双击元素【%s】成功" % element.name)

    def drag_and_drop(self, source, target):
        """
        拖拽元素
        :param source: 需要拖拽的元素
        :param target: 目标元素
        """
        source_ele = self.show_element(source)
        target_ele = self.show_element(target)
        self.mouse_suppert.drag_and_drop(source=source_ele, target=target_ele).perform()

    def move_to_element(self, element):
        """
        悬浮
        :param element: 操作元素
        """
        ele = self.show_element(element=element)
        self.mouse_suppert.move_to_element(ele).perform()
        log("悬停元素【%s】成功" % element.name)


    def send_keys_to_element(self, element, *keys_to_send):
        """
        填写内容
        :param element: 操作元素
        :param keys_to_send: 填写内容
        """
        ele = self.show_element(element=element)
        ele.clear()
        self.mouse_suppert.send_keys_to_element(element=ele, *keys_to_send)

@dataclass
class _OtherBrowserOperationClass(_MouseToOperations):
    """
    * 刷新浏览器        refresh()
    * 请求访问的地址    open_url(url)
    """
    def __post_init__(self):
        super(_OtherBrowserOperationClass, self).__post_init__()

    def refresh(self):
        # 刷新浏览器
        self.driver.refresh()

    def open_url(self, url: str):
        # 请求访问的地址
        js = 'window.open("%s");' % url
        self.driver.execute_script(js)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def maximize_window(self):
        # 设置浏览器窗口最大化
        self.driver.maximize_window()

    def quit(self):
        # 关闭浏览器
        self.driver.quit()

    def close(self):
        # 关闭单个网页
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    @property
    def title(self):
        # 获取浏览器网页标题
        return self.driver.title

    @property
    def current_url(self):
        # 获取当前网址
        return self.driver.current_url

    def get_scrrenshot_as_file(self, path: str):
        # 截图
        self.driver.get_screenshot_as_file(path)

    def execute_js(self, js: str, *args):
        # 使用js操作浏览器
        return self.driver.execute_script(js, *args)

    def current_window(self):
        # 获取浏览器中当前操作窗口的句柄
        return self.driver.current_window_handle

    def more_window(self):
        # 获取浏览器全部操作窗口句柄
        return self.driver.window_handles

    def switch_window(self, index: int):
        # 切换浏览器窗口句柄
        window = self.more_window()
        return self.driver.switch_to.window(window[index])

    def forward(self):
        # 前进
        self.driver.forward()

    def back(self):
        # 后退
        self.driver.back()


class MySelenium(_OtherBrowserOperationClass):

    def __init__(self, driver, timeout=5, detection=0.2, execption=EC.NoSuchElementException):
        super(MySelenium, self).__init__(driver=driver, timeout=timeout, detection=detection, execption=execption)

    def set_max(self):
        self.maximize_window()

    def close_browser(self):
        self.quit()

    def close_webpage(self):
        self.close()


    def refresh(self):
        self.refresh()

    @property
    def get_current_title(self):
        """获取标题"""
        return self.title

    @property
    def get_current_url(self):
        """获取当前网页的网址"""
        return self.current_url


    def get_screenshot(self, line_num):
        """
        截图
        :param line_num: 案例名称
        """
        image_path = os.curdir + "/screenshot/" + line_num + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + '.png'
        self.get_scrrenshot_as_file(image_path)
        log("截图成功")


    def send_keys(self, control):
        """
        向文本框填写数据
        :param control: 控件
        :return:
        """
        self.send_keys_to_element(control, control.value)
        log("填写元素【%s-%s】成功" % (control.name, control.value))

    def get_element_context(self, control):
        """
        获取文本内容
        """
        element = self.show_element(control)
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
        content = self.show_element(element_path).get_attribute(attribute)
        return content


