# -*- coding: utf-8 -*-
from flask import Blueprint
from util.template import render

__author__ = 'myth'


"""
公司控制器
"""
company_page = Blueprint('company_page', __name__)


@company_page.route("/company/")
def company_index_page():
    """
    工作集中营
    """

    return render('/company/index.html')

