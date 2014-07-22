# -*- coding: utf-8 -*-
from functools import wraps
import platform
import traceback
import ujson as json
import time
from flask import g, make_response, redirect, url_for, request
from werkzeug.wrappers import Response
from setting import DEV_MACHINES
from worker.lib.cookie import delete_user_login_cookie
from worker.result import ResultCode, Result

__author__ = 'myth'


# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):

    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        _func = func(*args, **kwargs)
        end = time.time()
        if platform.node() in DEV_MACHINES:
            print '%r: "%s" methods of running time->%r' % (func.func_code, func.func_name, end - start)
        return _func

    # 将包装后的函数返回
    return wrapper


#返回json的装饰器
def rjson(func):
    """
    Decorator to make view ret to json.
    """

    @wraps(func)
    def _(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
            if isinstance(ret, Response):
                if ret.status_code == 302:
                    result = Result(ResultCode.LOGIN, msg=u'请先登录！！').recall()
                    # result = jsonify(result)
                    result = json.dumps(result)
                else:
                    result = ret
            else:
                # result = jsonify(ret)
                result = json.dumps(ret)
        except:
            if platform.node() in DEV_MACHINES:
                print traceback.format_exc()

            ret = Result(ResultCode.ERROR, msg=u'服务器错误').recall()
            result = json.dumps(ret)

        return result

    return _


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if g.curr_user is None:
            _next = get_next_url()
            data = {}
            response = make_response(redirect(url_for('user_page.user_login_page', next=_next, **data)))
            delete_user_login_cookie(response)
            return response
            # return redirect(url_for('account_page.login', next=_next, **data))
        return f(*args, **kwargs)
    return decorated_function


def get_next_url():
    _next = request.url
    isNext = request.args.get("n")
    _referer = request.referrer
    if _referer and isNext == '1':
        _next = _referer
    return _next