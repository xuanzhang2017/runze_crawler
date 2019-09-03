# coding=utf8
import logging
import os
from logging.handlers import TimedRotatingFileHandler


class LogUtil(object):
    _logger = None

    def __init__(self):
        log_dir = '../log'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_prefix = '%s/%s' % (log_dir, 'app_crawler',)
        DEFAULT_FORMAT = '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'
        DEFAULT_DATE_FORMAT = '%y%m%d %H:%M:%S'
        formatter = logging.Formatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT)
        fileHandler = TimedRotatingFileHandler(log_file_prefix + ".log", when='midnight', interval=1, backupCount=7)
        fileHandler.setFormatter(formatter)
        self._logger = logging.getLogger(log_file_prefix)
        self._logger.addHandler(fileHandler)
        self._logger.setLevel(logging.DEBUG)

    @property
    def logger(self):
        return self._logger


logger = LogUtil().logger
