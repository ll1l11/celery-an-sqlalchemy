# -*- coding: utf-8 -*-
DEBUG = True
SECRET_KEY = 'super-secret-key'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/demo'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

CACHE_TYPE = 'memcached'
CACHE_DEFAULT_TIMEOUT = 500
CACHE_KEY_PREFIX = 'demo_'
CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11211']

# bootstrap
BOOTSTRAP_SERVE_LOCAL = True
