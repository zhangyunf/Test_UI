#-*- endcoding:utf-8 -*-
from .config_operation import configOperation
section = "path"

class pathConfig(configOperation):

      @property
      def elementPath(self):
            elementPath = self.get_value(section, "elementPath")
            return elementPath

      @property
      def casePath(self):
            casePath = self.get_value(section, "casePath")
            return casePath

      @property
      def lanePath(self):
            lanePath = self.get_value(section, "lanePath")
            return lanePath


if __name__ == "__main__":
      a = pathConfig()
      print(a.elementPath, a.casePath)





