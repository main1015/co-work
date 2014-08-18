# -*- coding: utf-8 -*-
import platform
from setting import DEV_MACHINES, STAG_MACHINES, PRO_MACHINES

__author__ = 'myth'


COOKIE_PATH = '/'

COOKIE_SPLIT_KEY = '_'
COOKIE_LOGIN_NAME = 'gy'

if platform.node() in DEV_MACHINES:
    COOKIE_DOMAIN = '192.168.4.191'
    COOKIE_SECRET_KEY = '1234567890123456'
elif platform.node() in STAG_MACHINES:
    COOKIE_DOMAIN = ''
    COOKIE_SECRET_KEY = '9989567890abc456'
elif platform.node() in PRO_MACHINES:
    COOKIE_DOMAIN = ''
    COOKIE_SECRET_KEY = 'dbca568790coi456'
else:
    COOKIE_DOMAIN = ''
    COOKIE_SECRET_KEY = '9997777890123456'