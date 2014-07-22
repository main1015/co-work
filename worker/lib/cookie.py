# -*- coding: utf-8 -*-
from flask import request
import time
from setting.cookie import COOKIE_SPLIT_KEY, COOKIE_LOGIN_NAME, COOKIE_SECRET_KEY, COOKIE_PATH, COOKIE_DOMAIN
from util.strings import encrypt_str, decrypt_str

__author__ = 'myth'


def set_user_login_cookie(user_id, response, expires=None):
    """
    设置用户登录cookie
    """

    # _time = time.time()
    browser = request.user_agent.string.split(' ')[0]
    # expires = int(_time) + 12*60*60
    token = COOKIE_SPLIT_KEY.join([str(user_id), str(expires), browser])

    response.set_cookie(COOKIE_LOGIN_NAME, encrypt_str(token, COOKIE_SECRET_KEY),
                        expires=expires, domain=COOKIE_DOMAIN, path=COOKIE_PATH)


def delete_user_login_cookie(response):
    _time = time.time()
    expires = int(_time)
    response.set_cookie(COOKIE_LOGIN_NAME, '', expires=expires, path=COOKIE_PATH, domain=COOKIE_DOMAIN)


def get_user_id_from_cookie():
    cookie_str = request.cookies.get(COOKIE_LOGIN_NAME)
    user_id = 0
    if cookie_str:
        user_id = user_id_from_cookie(cookie_str, COOKIE_SECRET_KEY, COOKIE_SPLIT_KEY)
    return user_id


def user_id_from_cookie(token, secret_key, split_key):
    """
    Get user id from token, if no valid found return 0.
    :param token: string
    :param secret_key: string
    :return: int
    """

    not_login_in = 0
    try:
        tokens = decrypt_str(token, secret_key).split(split_key)
    except TypeError,e:
        return not_login_in
    if len(tokens) != 3:
        return not_login_in
    else:
        try:
            expires = tokens[1]
            if expires != 'None':
                now = time.time()
                expires = float(tokens[1])
                if now > expires:
                    return not_login_in
            user_id = int(tokens[0])
            if user_id > not_login_in:
                return user_id
            else:
                return not_login_in
        except ValueError:
            return not_login_in