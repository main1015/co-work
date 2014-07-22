# -*- coding: utf-8 -*-
from sqlalchemy import Enum


__author__ = 'myth'


class BaseCode(Enum):

    #成功
    SUCCESS = 200
    #错误
    ERROR = 500
    #未知
    UNKNOWN = 60001


class ResultCode(BaseCode):
    #缺少参数
    LACK_PARAM = 50001
    #登录
    LOGIN = 301


class Result(object):

    def __init__(self, code, msg=None, data=None, **kwargs):

        self.code = code
        self.msg = msg if msg else ''
        self.data = data if data else []
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def recall(self):
        return {"code": self.code, "data": self.data, "msg": self.msg}