# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import IntegerField

__author__ = 'myth'


class PageForm(Form):
    """
    分页表单
    """
    p = IntegerField('p', default=1)
    l = IntegerField('p', default=10)