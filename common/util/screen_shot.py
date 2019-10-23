#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import os
screenshot_path = './screenshot'
def clear_screenshot(fn):

    def run(*args, **kwargs):
        if (os.path.exists(screenshot_path)):
            ls = os.listdir(screenshot_path)
            for i in ls:
                c_path = os.path.join(screenshot_path, i)
                os.remove(c_path)
        run_case = fn(*args, **kwargs)
        return run_case
    return run

