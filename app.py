import logging
import os
from logging import handlers

base_dir = os.path.dirname(os.path.abspath(__file__))
log_path = base_dir + '/log/ihrm.log'
headers = {}
emp_id = ""

def init_logger():
    logger = logging.getLogger()#创建日志器
    logger.setLevel(logging.INFO)#设置等级

    sh = logging.StreamHandler()#初始化控制台处理器
    #初始化固定位置和时间间隔的处理器
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_path,when="H",interval=2,backupCount=3,encoding="utf-8")
    #创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)
