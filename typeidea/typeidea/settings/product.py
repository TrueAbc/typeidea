from .base import *

DEBUG = False

# ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
        'CONN_MAX_AGE': 5 * 60,
    }
}


REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'REDIS_URL',
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': 'test123',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}