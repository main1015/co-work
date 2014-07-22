# -*- coding: utf-8 -*-
import platform
from setting import DEV_MACHINES

__author__ = 'myth'

if platform.node() in DEV_MACHINES:
    BIND_HOST = '0.0.0.0'
    BIND_PORT = 8688
    DEBUG_ENABLED = True
    COOKIE_SECRET_KEY = '1234567890123456'
else:
    BIND_HOST = '127.0.0.1'
    BIND_PORT = 8688
    DEBUG_ENABLED = False
    COOKIE_SECRET_KEY = '12Ed56gM9cC2f4!6'