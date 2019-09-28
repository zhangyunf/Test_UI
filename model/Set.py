#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from model.BaseModel import BaseModel

class SetModel(BaseModel):
    # 测试集
    def __init__(self, data):
        # 测试集名称
        self.name = data[0]
        # 是否执行
        self.is_run = data[1]
        # 泳道
        self.scene_list = []
        # 案例总数
        self.case_num = 0
        # 成功数
        self.case_success = 0
        # 失败数
        self.case_false = 0
        # 案例未执行数量
        self.non_execution = 0

    def description(self):
        super(SetModel, self).description()
        print("测试集名称%s,是否执行%s" % (self.name, self.is_run))

