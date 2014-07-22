# -*- coding: utf-8 -*-
from flask import render_template

__author__ = 'myth'


def render(template_name_or_list, **context):
    """
    模板渲染方法
    """

    return render_template(template_name_or_list, **context)