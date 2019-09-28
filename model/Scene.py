#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from model.BaseModel import BaseModel

class SceneModel(BaseModel):
    # 泳道
    def __init__(self, data):
        # 场景名称
        self.name = data[0]
        # 是否执行
        self.is_run = data[1]
        # 检查点
        self.checkpotion = data[2]
        # 案例
        self.case_list = []
        # 案例总数
        self.case_num = 0
        # 案例成功数
        self.case_success = 0
        # 案例失败数
        self.case_false = 0
        # 案例未执行数量
        self.non_execution = 0

    def description(self):
        super(SceneModel, self).description()
        print("场景名称%s,是否执行%s,检查点%s" % (self.name, self.is_run, self.checkpotion))
