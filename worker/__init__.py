# -*- coding: utf-8 -*-
import os
from flask import Flask, g, send_from_directory
import time
from werkzeug.contrib.fixers import ProxyFix
from db.database import db_session
from db.model import User
from setting.config import DEBUG_ENABLED
from setting.domain import S_DOMAIN
from worker.controler import register_blueprint, app_config
from worker.lib.cookie import get_user_id_from_cookie
from worker.template_filter import register_filter
from worker.template_global import register_global, clean_resource

__author__ = 'myth'

# Application config.
app = Flask(__name__, static_folder='../static', template_folder='../templates')

app.debug = DEBUG_ENABLED
app.wsgi_app = ProxyFix(app.wsgi_app)

register_blueprint(app)
app_config(app)

register_filter(app.jinja_env)
register_global(app.jinja_env)


@app.before_request
def before_request():
    """
    Do sth before each request.
    """

    clean_resource()

    # var init.
    g.curr_user = None
    g.req_start_time = time.time()

    user_id = get_user_id_from_cookie()
    if user_id > 0:
        # todo(myth) 根据cookie查询数据,获取用户名
        curr_user = User.get(user_id)
        if curr_user:
            g.curr_user = curr_user


@app.teardown_request
def shutdown_session(exception=None):
    """
    Do sth after each request.
    """

    db_session.remove()

    # get page execute time.
    req_pass_time = (time.time() - g.req_start_time) * 1000


@app.context_processor
def inject_global_var():
    """
    Inject global var to app context, it can be used in template.
    """

    return dict(
        curr_user=g.curr_user,
        s_domain=S_DOMAIN,
    )


@app.route('/favicon.ico')
def favicon():
    """
    favicon.ico
    """

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')