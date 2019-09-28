#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import cv2
import numpy as np
from io import BytesIO
import time, requests
from common.util.log import *

class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """

    def __init__(self, driver):
        super(CrackSlider, self).__init__()
        # 实际地址
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.zoom = 1

    def get_pic(self):
        time.sleep(2)
        target = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
        template = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_jigsaw')))
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        size_orign = target.size
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        self.zoom = 320 / int(size_loc[0])

    def get_tracks(self, distance):
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3 / 5
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def match(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template, 0)
        run = 1
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2

            if threshold < 0:
                print('Error')
                return None
            loc = np.where(res >= threshold)
            if len(loc[1]) > 1:
                L += (R - L) / 2
            elif len(loc[1]) == 1:
                # print('目标区域起点x坐标为：%d' % loc[1][0])
                break
            elif len(loc[1]) < 1:
                R -= (R - L) / 2

        return loc[1][0]

    def crack_slider(self):
        for i in range(1000):
            target = 'target.jpg'
            template = 'template.png'
            self.get_pic()
            distance = self.match(target, template)
            tracks = self.get_tracks((distance + 7) * self.zoom)  # 对位移的缩放计算
            slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'yidun_slider')))
            ActionChains(self.driver).click_and_hold(slider).perform()
            for track in tracks['forward_tracks']:
                ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

            time.sleep(0.5)
            for back_tracks in tracks['back_tracks']:
                ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

            ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()
            ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()
            time.sleep(0.5)
            ActionChains(self.driver).release().perform()
            failure = False
            try:
                failure = self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'yidun_slider')))
                log("滑块验证成功")
            except:
                log("滑块验证失败，重新验证")


            if failure:
                break

if __name__ == '__main__':
    c = CrackSlider()
    c.crack_slider()

