# -*- coding: utf-8 -*-
from setting.config import COOKIE_SECRET_KEY
from worker.company.views import company_page
from worker.note.views import note_page
from worker.user.views import user_page

__author__ = 'myth'


# Register all blueprint page.
def register_blueprint(app):
    app.register_blueprint(user_page)
    app.register_blueprint(note_page)
    app.register_blueprint(company_page)


#app配置信息
def app_config(app):
    app.config['SECRET_KEY'] = COOKIE_SECRET_KEY