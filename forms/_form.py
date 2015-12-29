# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import IntegerField

__author__ = 'myth'


class PageForm(Form):
    """
    分页请求from
    """

    # 页数
    page = IntegerField(u'page', default=1)
    # 每页显示条目
    limit = IntegerField(u'limit', default=10)
