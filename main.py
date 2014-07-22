# -*- coding: utf-8 -*-
from setting.config import BIND_HOST, BIND_PORT, DEBUG_ENABLED
from worker import app

__author__ = 'myth'

if __name__ == '__main__':
    app.run(host=BIND_HOST, port=BIND_PORT, debug=DEBUG_ENABLED)