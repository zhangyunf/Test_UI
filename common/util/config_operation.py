#-*- endcoding:utf-8 -*-
import configparser
file_name = r"./data/config/config.ini"
class configOperation(object):
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(file_name)

    def get_value(self, section, option):
        return self.conf.get(section=section, option=option)

if __name__ == "__main__":
    section = "path"
    file_name = r"D:\接口\Test_UI\data\config\config.ini"
    a = configOperation(file_name)
    print(a.get_value(section, "elementPath"))