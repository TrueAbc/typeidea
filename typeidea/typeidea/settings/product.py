from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
        'CONN_MAX_AGE': 5 * 60,
    }
}


ADMINS = MANAGERS = (
    'TrueAbc', '547551933@qq.com',
)

# EMAIL_HOST = 'smtp.163.com'
# EMAIL_HOST_USER = '547551933@qq.com'
# EMAIL_HOST_PASSWORD = 'PASSWORD'
# EMAIL_SUBJECT_PREFIX = 'typeidea-problem'
# DEFAULT_FROM_EMAIL = 'Lenovo@qq.com'
# SERVER_EMAIL = ''

STATIC_ROOT = '/home/abc/venvs/djano-venv/static_files/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%{levelname}s % {asctime}s %{module}s:'
                      '%{funcName}s: %{lineno}d %{message}s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'files': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024*1024,
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': 'test123',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}