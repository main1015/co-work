# -*- coding: utf-8 -*-
from setting.config import COOKIE_SECRET_KEY
from worker.controllers import pages
from worker.controllers import *

__author__ = 'myth'


# Register all blueprint page.
def register_blueprint(app):
    # app.register_blueprint(user_page)
    # app.register_blueprint(note_page)
    # app.register_blueprint(company_page)

    for _page in pages:
        page = globals().get(_page)
        if page:
            app.register_blueprint(page)


# app配置信息
def app_config(app):
    app.config['SECRET_KEY'] = COOKIE_SECRET_KEY
