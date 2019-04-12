#-*- endcoding:utf-8 -*-

def singletonDecorator(cls, *args, **kwargs):
    """定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSingleton

@singletonDecorator
class colorSingleton(object):
    """使用单例装饰器修饰一个类"""

    def __init__(self):
        self.failureColor = "FF0000"
        self.successColor = "006400"
        self.realityColor = self.failureColor
        self.global_value_dic = {}

    def change_failure(self):
        self.realityColor = self.failureColor

    def change_success(self):
        self.realityColor = self.successColor

    def add_value(self, key, value):
        self.global_value_dic.update({key: value})

    def get_value(self, key):
        return self.global_value_dic[key]






