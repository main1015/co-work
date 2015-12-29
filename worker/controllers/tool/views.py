# -*- coding: utf-8 -*-
from flask import Blueprint
from util.template import render
from worker.decorator import login_required

__author__ = 'myth'
"""
Created by myth on 15-12-25.
"""


tool_page = Blueprint('tool_page', __name__)


@tool_page.route("/tool/")
@tool_page.route("/tool/index")
@login_required
def tool_index_page():
    """
    工具首页
    :return:
    """
    data = {}

    return render("/tool/index.html", **data)
