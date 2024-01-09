import logging
import sys
import os
import logging.handlers as handlers
from vic_utilities import PACKAGE_PATH

LOG_DIR = os.path.abspath(os.path.join(PACKAGE_PATH, '../log'))

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    print('***** created LOG_DIR [{}] *****'.format(os.path.abspath(LOG_DIR)))


simple_format = '%(message)s'
standard_format = '%(asctime)s [%(levelname)s] - %(message)s'
detail_format = '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s] [%(pathname)s:%(funcName)s:%(lineno)d] [%(levelname)s] - %(message)s'

default_log_level = logging.DEBUG

logger = dict()


def get_logger(name, log_level=None):
    if not log_level:
        log_level = default_log_level
    global logger
    if name in logger:
        pass
    else:
        datefmt = "%Y-%m-%d %H:%M:%S"
        _logger = logging.getLogger(name)
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(log_level)
        sh.setFormatter(logging.Formatter(simple_format))
        _logger.addHandler(sh)
        logfile = '{}/{}.log'.format(LOG_DIR, name)
        fh = handlers.RotatingFileHandler(logfile, encoding='utf-8', maxBytes=10*1024*1024, backupCount=100)
        fh.setLevel(log_level)
        fh.setFormatter(logging.Formatter(standard_format, datefmt))
        _logger.addHandler(fh)
        logger[name] = _logger
    return logger[name]
