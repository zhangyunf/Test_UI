# -*- endcoding:utf-8 -*-
import logging
import os
# 获取logger
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
# 获取handler
log_path = os.curdir + '/log/' + "测试日志" + '.log'


if (os.path.exists(log_path)):
    os.remove(log_path)

fh = logging.FileHandler(log_path)
ch = logging.StreamHandler()

# 格式
formatter = logging.Formatter("%(asctime)s  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)



def log(message):
    logger.warning(message)


