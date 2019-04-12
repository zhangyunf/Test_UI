#-*- endcoding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.util.log import log
import time
import os

findElementTimes = 1

class MySelenium(object):
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url, url_title=None):
        '''
        打开网址，并验证是否正确
        :param url: 网址
        :param url_title: 网站的title
        :return:
        '''
        try:
            js = 'window.open("%s");' % url
            self.driver.execute_script(js)
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            # config = True if url_title != None and url_title == self.driver.title else False
            # if config:
            #     log("打开网址%s成功" % url)
            # else:
            #     log("打开网址%s失败" % url)
            #     self.get_screenshot
            #     log("案例结束")
            #     self.close_webpage()
        except:
            log("打开网址%s失败" % url)
            self.get_screenshot
            log("案例结束")
            self.close_webpage()

    def set_max(self):
        '''
        设置浏览器窗口最大化
        '''
        self.driver.maximize_window()

    def close_browser(self):
        '''
        关闭浏览器
        '''
        self.driver.quit()

    def close_webpage(self):
        '''
        关闭单个网页
        :return:
        '''
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    def refresh(self):
        '''
        刷新页面
        '''
        self.driver.refresh()
        log("刷新页面成功")

    @property
    def get_current_title(self):
        '''获取标题'''
        return self.driver.title

    @property
    def get_current_url(self):
        '''获取当前网页的网址'''
        return self.driver.current_url

    @property
    def get_screenshot(self):
        '''
        截图
        '''
        try:
            image_path = os.curdir + "/data/screenshot/" + time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + '.png'
            self.driver.get_screenshot_as_file(image_path)
            log("截图成功")
        except:
            log("截图失败！")

    def find_element(self, element_path):
        '''
        定位元素，并且返回
        :param elementBy: 定位元素的方式，包括（"By.XPATH"、""）
        :param elementContent: 路径
        :return: 元素
        '''

        for i in range(0, findElementTimes):
            try:
                element = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((eval(element_path[1]), element_path[2])))
                return element
                break
            except:
                if i == findElementTimes - 1:
                    log("获取【%s-%s】失败" % (element_path[0], element_path[1]))
                    self.close_webpage()
                    log("案例结束")

    def click(self, element_path):
        '''
        点击元素
        '''
        try:
            element = self.find_element(element_path)
            ActionChains(self.driver).click(element).perform()
            log("点击元素【%s】成功" % element_path[0])
        except:
            log("点击元素【%s】失败" % element_path[0])
            self.close_webpage()
            log("案例结束")

    def send_keys(self, element_path, content):
        try:
            element = self.find_element(element_path)
            element.clear()
            element.send_keys(content)
            log("填写元素【%s-%s】成功" % (element_path[0], content))
        except:
            log("填写元素【%s-%s】失败" % (element_path[0], content))
            self.close_webpage()
            log("案例结束")


    def double_click(self, element_path):
        try:
            element = self.find_element(element_path)
            ActionChains(self.driver).double_click(element).perform()
            log("双击元素【%s】成功" % element_path[0])
        except:
            log("双击元素【%s】失败" % element_path[0])
            self.close_webpage()
            log("案例结束")

    def move_to_element(self, element_path):
        try:
            element = self.find_element(element_path)
            ActionChains(self.driver).move_to_element(element).perform()
            log("悬停元素【%s】成功" % element_path[0])
        except:
            log("悬停元素【%s】失败" % element_path[0])
            self.close_webpage()
            log("案例结束")


    def get_element_context(self, element_path):
        '''
        获取文本内容
        '''
        try:
            element = self.find_element(element_path)
            content = element.text
            log("获取文本【%s】内容成功---%s" % (element_path[0], content))
            return content
        except:
            log("获取元素【%s】内容失败" % element_path[0])
            return False

    def get_attribute_context(self, attribute, element_path):
        '''
        获取元素的文本内容
        :param element: 元素
        :param attribute: 需要获取的元素属性值
        :param element_path: 文件page_element相对应的东西
        :return: 元素属性的值
        '''
        try:
          content = self.find_element(element_path).get_attribute(attribute)
          return content
        except:
            log("获取元素【%s】内容失败" % element_path[0])
            self.close_webpage()
            log("案例结束")
    def get_cookie(self, cookie_name):
        try:
            cookie = self.driver.get_cookie(cookie_name)
            log("获取cookie-%s成功：%s" % (cookie_name, cookie))
        except:
            log("获取cookie-%s失败" % cookie_name)
            self.close_webpage()
            log("案例结束")

    def delete_cookie(self, cookie_name):
        self.driver.delete_cookie(cookie_name)
        # log("删除cookie-%s成功：%s" % cookie_name)
        # try:
        #     self.driver.delete_cookie(cookie_name)
        #     log("删除cookie-%s成功：%s" % cookie_name)
        # except:
        #     log("删除cookie-%s失败" % cookie_name)
        #     self.close_webpage()
        #     log("案例结束")

    def add_cookie(self, cookie_name, cookie_value):
        try:
            self.driver.add_cookie({"name": cookie_name,
                                    "value": cookie_value})
            log("添加cookie-%s成功" % cookie_name)
        except:
            log("获取cookie-%s失败" % cookie_name)
            self.close_webpage()
            log("案例结束")

