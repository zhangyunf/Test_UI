#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from model.BaseModel import BaseModel


class ControlsModel(BaseModel):

    def __init__(self):
        super(ControlsModel, self).__init__()
        # 控件名称
        self.name = ""

        # 填写内容
        self.value = ""

        # 定位方式
        self.find_element_type = ""

        # 定位方式所需内容
        self.find_element_value = ""

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def set_find_element_type(self, find_element_type):
        self.find_element_type = find_element_type

    def set_find_element_value(self, find_element_value):
        self.find_element_value = find_element_value

    def description(self):
        super(ControlsModel, self).description()
        pass