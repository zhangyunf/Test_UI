#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from dataclasses import dataclass

@dataclass
class UntilNoElementOrTimeoutError(Exception):
    timeout: float
    element: str

    def __str__(self):
        return f'元素:{self.element} 在{self.timeout}s 未出现'

