# -*- coding: utf-8 -*-
from flask import Blueprint, request
from db.service.company import get_company_list
from util.template import render
from worker.decorator import rjson

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


@company_page.route("/company/list")
@rjson
def company_get_list_page():
    """
    获取集中营的公司
    """
    #todo
    get_company_list()