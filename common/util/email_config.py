#-*- endcoding:utf-8 -*-
from .config_operation import configOperation
section = "email"

class emailConfig(configOperation):

      @property
      def sender(self):
            sender = self.get_value(section, "sender")
            return sender

      @property
      def receivers(self):
            receivers = self.get_value(section, "receivers")
            return receivers

      @property
      def password(self):
            password = self.get_value(section, "password")
            return password
      @property
      def htmlreportpath(self):
          htmlreportpath = self.get_value(section, "htmlreportpath")
          return htmlreportpath








