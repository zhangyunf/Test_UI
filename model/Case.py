#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from model.BaseModel import BaseModel


class CaseModel(BaseModel):


    def __init__(self, data):
        # 名称
        self.name = ""
        # 测试点
        self.checkpotion = data[1]
        # 预期结果
        self.expected_result = data[2]
        # 网址
        self.url = data[3]
        # 实际结果
        self.result = None
        # 控件
        self.controls_list = []
        # 失败描述
        self.false_log = ""



    def description(self):
        super(CaseModel, self).description()
        print("名称%s,测试点%s,预期结果%s,实际结果%s,控件%s"% (self.name, self.checkpotion, self.expected_result, self.result, self.controls_list))