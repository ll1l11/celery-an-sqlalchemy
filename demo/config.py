# -*- coding: utf-8 -*-
DEBUG = True
SECRET_KEY = 'super-secret-key'

SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1/demo'

CACHE_TYPE = 'memcached'
CACHE_DEFAULT_TIMEOUT = 500
CACHE_KEY_PREFIX = 'demo_'
CACHE_MEMCACHED_SERVERS = '127.0.0.1:11211'
