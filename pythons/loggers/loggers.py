import logging
import logging.config
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

log_path = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)


dict_config = {
    'version': 1,
    'formatters': {
        'default': {
            'class': 'logging.Formatter',
            'format': '[%(asctime)s] [%(threadName)s] [%(levelname)s] [%(filename)s %(lineno)d] [%(message)s]'
        }
    },
    'filter': {},
    'handlers': {
        'stream': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'files': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': os.path.join(BASE_DIR, 'logs/{} -- {}.log'.format('async_task_cookies', time.strftime("%Y-%m-%d"))),
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 5,
            'encoding': 'utf-8',
        }

    },
    'loggers': {
        'root': {
            'handlers': ['stream', 'files'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'invalidCookie': {
            'handlers': ['stream', 'files'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
logging.config.dictConfig(dict_config)

logger = logging.getLogger("invalidCookie")