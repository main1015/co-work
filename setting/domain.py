# -*- coding: utf-8 -*-
from setting import DEV_MACHINES, PLATFORM

__author__ = 'myth'

if PLATFORM in DEV_MACHINES:
    S_DOMAIN = '/static'
else:
    S_DOMAIN = '/static'