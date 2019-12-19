
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from config.pathes import LOG_PATH, PROJECTINFO, NOW, DAY
from utils.FileReader import YamlReader


class Logger(object):
    def __init__(self, progect):
        self.progect = progect
        self.logger_name = '%stest' % self.progect
        self.logger = logging.getLogger(self.logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = YamlReader(PROJECTINFO).get(progect).get('log')
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else NOW+'test.log'  # 日志文件
        self.backup_count = c.get('backup') if c and c.get('backup') else 5  # 保留的日志数量
        # 日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        # 日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.ft = logging.Formatter(pattern)

    def get_logger(self):
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.ft)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            lf = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, DAY+' '+self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            lf.setFormatter(self.ft)
            lf.setLevel(self.file_output_level)
            self.logger.addHandler(lf)
            # 在控制台输出日志信息
            ls = logging.StreamHandler()
            ls.setFormatter(self.ft)
            ls.setLevel(self.file_output_level)
            self.logger.addHandler(ls)
        return self.logger

if __name__ == '__main__':
    logger = Logger('OA').get_logger()
    logger.info("a")