"""
自定义日志
Author : chengyao
Email : chengy_work@163.com
"""
import logging
import time
import os
from config.settings import LOG_NAME


class Log(object):
    """
    封装好的日志系统，只需要在配置文件中定义日志名，并在上方导入（替换from config.settings import LOG_NAME）即可
    """

    def __init__(self, logger=None, log_cate=LOG_NAME):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.log_time = time.strftime("%Y_%m_%d")  # 创建一个handler，用于写入日志文件
        # file_dir = os.getcwd() + '/../log'#在项目目录的上级目录记录log
        file_dir = os.getcwd() + '/log'
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        self.log_path = file_dir
        self.log_name = self.log_path + "/" + log_cate + "." + self.log_time + '.log'
        # fh = logging.FileHandler(self.log_name, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()  # 再创建一个handler，用于输出到控制台
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger
