# -*- coding: utf-8 -*-
import platform
from setting import DEV_MACHINES

__author__ = 'myth'

if platform.node() in DEV_MACHINES:
    S_DOMAIN = '/static'
else:
    S_DOMAIN = '/static'